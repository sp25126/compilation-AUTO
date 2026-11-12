import subprocess
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_VIDEO = os.path.join(BASE_DIR, "output", "one_million_aura_loss_raw.mp4")
MASTERED_VIDEO = os.path.join(BASE_DIR, "output", "one_million_aura_loss_mastered.mp4")
QA_SHEET = os.path.join(BASE_DIR, "output", "one_million_aura_loss_qa_sheet.jpg")

def master_audio():
    print("Mastering audio to EBU R128 (-14 LUFS, True Peak -1.5 dBTP)...")
    cmd_master = [
        "ffmpeg", "-y",
        "-i", RAW_VIDEO,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        MASTERED_VIDEO
    ]
    subprocess.run(cmd_master, check=True)
    print(f"Mastered video saved to: {MASTERED_VIDEO}")

    print("Measuring final integrated loudness...")
    cmd_measure = [
        "ffmpeg", "-i", MASTERED_VIDEO,
        "-af", "ebur128=peak=true",
        "-f", "null", "NUL" if os.name == "nt" else "/dev/null"
    ]
    proc = subprocess.run(cmd_measure, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Parse ebur128 output
    summary = proc.stderr
    i_lufs = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", summary)
    lra = re.search(r"LRA:\s*(-?[\d.]+)\s*LU", summary)
    tp = re.search(r"Peak:\s*(-?[\d.]+)\s*dBFS", summary)
    
    print("\n================== EBU R128 LOUDNESS RESULTS ==================")
    if i_lufs:
        print(f"Integrated Loudness: {i_lufs.group(1)} LUFS (Target: -14.0 ± 1.0 LUFS)")
    if lra:
        print(f"Loudness Range (LRA): {lra.group(1)} LU")
    if tp:
        print(f"True Peak: {tp.group(1)} dBFS (Target <= -1.5 dBTP)")
    print("===============================================================\n")

    print("Generating 1fps QA contact sheet...")
    # Calculate duration
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        MASTERED_VIDEO
    ]
    dur = float(subprocess.check_output(probe_cmd, text=True).strip())
    print(f"Mastered video duration: {dur:.2f}s")
    
    cmd_sheet = [
        "ffmpeg", "-y",
        "-i", MASTERED_VIDEO,
        "-vf", "fps=1,scale=260:-1,tile=6x7",
        "-frames:v", "1",
        "-q:v", "3",
        QA_SHEET
    ]
    subprocess.run(cmd_sheet, check=True)
    print(f"QA sheet generated: {QA_SHEET}")

if __name__ == "__main__":
    master_audio()
