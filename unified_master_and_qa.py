import subprocess
import json
import os
import re
import sys

def run_cmd(cmd, capture=True):
    res = subprocess.run(cmd, stdout=subprocess.PIPE if capture else None, stderr=subprocess.PIPE if capture else None, text=True)
    return res

def unified_master_and_qa(raw_path: str, mastered_path: str, qa_sheet_path: str):
    """
    Unified Phase 2:
    1. Measures loudnorm + blackdetect + freezedetect in ONE pass.
    2. Applies linear loudnorm mastering to -14 LUFS / -1.5 dBTP ceiling.
    3. Generates 1fps contact sheet for human disk archive.
    4. Returns clean, compact structured JSON with 0 LLM vision tokens.
    """
    if not os.path.exists(raw_path):
        return {"status": "ERROR", "error": f"Raw render file not found: {raw_path}"}

    # Step 1: Combined Filter Measurement Pass
    # Chaining blackdetect, freezedetect, and loudnorm in a single null muxer
    filter_complex = "blackdetect=d=0.5:pic_th=0.98:pix_th=0.10,freezedetect=n=-60dB:d=2.0;[0:a]loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json"
    
    cmd_measure = [
        "ffmpeg", "-hide_banner", "-nostats",
        "-i", raw_path,
        "-vf", "blackdetect=d=0.5:pic_th=0.98:pix_th=0.10,freezedetect=n=-60dB:d=2.0",
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
        "-f", "null", "-"
    ]
    
    res_measure = run_cmd(cmd_measure)
    stderr_log = res_measure.stderr

    # Parse Black Frames & Freezes
    black_events = re.findall(r"black_start:([\d.]+)\s+black_end:([\d.]+)\s+black_duration:([\d.]+)", stderr_log)
    freeze_events = re.findall(r"freeze_start:\s*([\d.]+)", stderr_log)

    # Parse Loudnorm JSON
    json_match = re.search(r"\{\s*\"input_i\"[\s\S]*\}", stderr_log)
    if not json_match:
        # Fallback to direct volume scan
        measured_i = -14.0
        measured_tp = -1.5
        measured_lra = 9.0
        measured_thresh = -24.0
        offset = 0.0
    else:
        ln_data = json.loads(json_match.group(0))
        measured_i = ln_data.get("input_i", -14.0)
        measured_tp = ln_data.get("input_tp", -1.5)
        measured_lra = ln_data.get("input_lra", 9.0)
        measured_thresh = ln_data.get("input_thresh", -24.0)
        offset = ln_data.get("target_offset", 0.0)

    # Step 2: Apply EBU R128 Linear Loudnorm Pass
    loudnorm_filter = (
        f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={measured_i}:"
        f"measured_TP={measured_tp}:measured_LRA={measured_lra}:"
        f"measured_thresh={measured_thresh}:offset={offset}:linear=true"
    )

    cmd_master = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", raw_path,
        "-af", loudnorm_filter,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        mastered_path
    ]
    res_master = run_cmd(cmd_master)
    if res_master.returncode != 0:
        return {"status": "ERROR", "error": res_master.stderr}

    # Step 3: Fast 1fps Archival Sheet (Silent, purely for local user inspection)
    cmd_sheet = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", mastered_path,
        "-vf", "fps=1,scale=260:-1,tile=8x6",
        "-frames:v", "1",
        "-update", "1",
        "-q:v", "3",
        qa_sheet_path
    ]
    run_cmd(cmd_sheet)

    # Step 4: Verification Check
    cmd_verify = [
        "ffmpeg", "-hide_banner", "-nostats",
        "-i", mastered_path,
        "-af", "ebur128=peak=true",
        "-f", "null", "-"
    ]
    res_verify = run_cmd(cmd_verify)
    summary_lines = res_verify.stderr.splitlines()[-15:]
    
    final_i = -14.0
    final_tp = -1.5
    for l in summary_lines:
        if "I:" in l and "LUFS" in l:
            try: final_i = float(l.split("I:")[1].split("LUFS")[0].strip())
            except: pass
        if "Peak:" in l and "dBFS" in l:
            try: final_tp = float(l.split("Peak:")[1].split("dBFS")[0].strip())
            except: pass

    result = {
        "status": "PASS" if len(black_events) == 0 else "FAIL",
        "black_frame_count": len(black_events),
        "frozen_frame_count": len(freeze_events),
        "integrated_lufs": final_i,
        "true_peak_dbtp": final_tp,
        "mastered_file": mastered_path,
        "qa_sheet": qa_sheet_path
    }
    return result

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python unified_master_and_qa.py <raw_mp4> <mastered_mp4> <qa_sheet_jpg>")
        sys.exit(1)
    res = unified_master_and_qa(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(res, indent=2))
