import os
import sys
import json
import argparse
import subprocess
import numpy as np

def get_video_duration(video_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_path
    ]
    try:
        res = subprocess.check_output(cmd, text=True).strip()
        return float(res)
    except Exception:
        return 10.0

def detect_motion_apex(video_path: str, fps: int = 6) -> tuple[float, list[tuple[float, float]]]:
    """
    Sample video at 6 fps using FFmpeg piped to stdout as raw grayscale bytes.
    Computes frame differences between adjacent frames to locate peak motion delta.
    Prioritizes peaks in the second half if duration > 20s.
    """
    eval_w = 160
    eval_h = 280
    frame_size = eval_w * eval_h

    cmd = [
        "ffmpeg", "-i", video_path,
        "-vf", f"fps={fps},scale={eval_w}:{eval_h}",
        "-pix_fmt", "gray",
        "-f", "rawvideo",
        "-"
    ]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=frame_size * 10)
    prev_frame = None
    frame_idx = 0
    deltas = []

    while True:
        raw_bytes = proc.stdout.read(frame_size)
        if len(raw_bytes) < frame_size:
            break
        curr_frame = np.frombuffer(raw_bytes, dtype=np.uint8)
        if prev_frame is not None:
            diff = np.abs(curr_frame.astype(np.int16) - prev_frame.astype(np.int16))
            motion_val = float(np.mean(diff))
            timestamp = round(frame_idx / float(fps), 2)
            deltas.append((timestamp, motion_val))
        prev_frame = curr_frame
        frame_idx += 1

    proc.stdout.close()
    proc.wait()

    if not deltas:
        return 0.0, []

    total_dur = deltas[-1][0] if deltas else 10.0

    # If video > 20s, focus on candidate window in 2nd half (> 0.35 * duration)
    if total_dur > 20.0:
        valid_candidates = [d for d in deltas if d[0] >= total_dur * 0.35]
        if valid_candidates:
            best_pair = max(valid_candidates, key=lambda x: x[1])
            return best_pair[0], deltas

    best_pair = max(deltas, key=lambda x: x[1])
    return best_pair[0], deltas

def trim_cause_and_impact(
    input_path: str,
    output_path: str,
    vlm_apex: float | None = None,
    buildup: float = 3.0,
    aftermath: float = 2.0
) -> dict:
    """
    MrPurifiedWater trained trimming engine:
    1. If input duration is short (<= 8.5s), it is already a curated short — preserve the entire action
       and keep the full context so it never cuts off prematurely or staggers.
    2. For longer footage (10s - 60s), locates the exact action apex and trims with:
       - 3.0s buildup (capturing approach)
       - 2.0s aftermath (capturing full physical impact, reaction, and settling)
       - Guarded against abrupt cuts by re-encoding keyframes cleanly.
    """
    total_dur = get_video_duration(input_path)

    if total_dur <= 8.5:
        # Keep entire clip intact to avoid cutting off early or staggering
        t_start = 0.0
        t_end = total_dur
        t_apex = round(total_dur * 0.6, 2)
    else:
        motion_apex, _ = detect_motion_apex(input_path)

        if vlm_apex and vlm_apex > 0:
            if abs(vlm_apex - motion_apex) <= 2.5:
                t_apex = round(vlm_apex * 0.6 + motion_apex * 0.4, 2)
            else:
                t_apex = vlm_apex
        else:
            t_apex = motion_apex if motion_apex > 0 else round(total_dur * 0.5, 2)

        # Calculate exact boundaries
        t_start = max(0.0, round(t_apex - buildup, 2))
        t_end = min(total_dur, round(t_apex + aftermath, 2))

        # Ensure balanced duration between 4.0s and 6.5s
        if (t_end - t_start) < 4.0:
            t_start = max(0.0, t_end - 4.5)
        if (t_end - t_start) > 6.5:
            t_end = t_start + 6.0

    target_duration = round(t_end - t_start, 2)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Frame-accurate clean re-encode to eliminate video stuttering/staggering
    trim_cmd = [
        "ffmpeg", "-y",
        "-ss", f"{t_start:.2f}",
        "-to", f"{t_end:.2f}",
        "-i", input_path,
        "-c:v", "libx264",
        "-crf", "18",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-avoid_negative_ts", "make_zero",
        "-c:a", "aac",
        "-b:a", "192k",
        output_path
    ]

    subprocess.run(trim_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    final_dur = get_video_duration(output_path)
    return {
        "status": "success",
        "input": input_path,
        "output": output_path,
        "t_apex": t_apex,
        "t_start": t_start,
        "t_end": t_end,
        "duration": final_dur
    }

def main():
    parser = argparse.ArgumentParser(description="AI Cause & Impact Trimmer")
    parser.add_argument("--input", required=True, help="Input raw vertical MP4")
    parser.add_argument("--output", required=True, help="Output trimmed MP4")
    parser.add_argument("--vlm-apex", type=float, default=None, help="Optional VLM apex timestamp estimate")
    args = parser.parse_args()

    res = trim_cause_and_impact(args.input, args.output, vlm_apex=args.vlm_apex)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
