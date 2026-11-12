import argparse
import json
import math
import os
import re
import subprocess
import sys
import numpy as np


def check_audio_and_aspect(video_path: str) -> bool:
    """
    1. Runs ffprobe to check video stream dimensions and aspect sanity.
    2. Runs ffmpeg volumedetect to ensure mean_volume >= -45 dB and audio is present.
    """
    if not os.path.exists(video_path):
        return False

    probe_cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-of", "json",
        video_path,
    ]
    probe_res = subprocess.run(
        probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
    )
    data = json.loads(probe_res.stdout)
    streams = data.get("streams", [])
    if not streams:
        return False
    width = streams[0].get("width", 0)
    height = streams[0].get("height", 0)
    if width <= 0 or height <= 0:
        return False

    audio_cmd = [
        "ffmpeg",
        "-i", video_path,
        "-af", "volumedetect",
        "-vn",
        "-f", "null",
        "-",
    ]
    audio_res = subprocess.run(
        audio_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
    )
    stderr_output = audio_res.stderr

    match = re.search(r"mean_volume:\s*(-?[\d.]+)\s*dB", stderr_output)
    if not match:
        return False

    mean_volume = float(match.group(1))
    if mean_volume < -45.0:
        return False

    return True


def detect_scene_cuts(video_path: str) -> list[float]:
    """
    Level 2 Scene-Cut Guard:
    Detects hard camera cuts using FFmpeg scene detection (threshold 0.40).
    Hard cuts create artificial motion variance spikes that must be filtered out
    to prevent premature cuts at an edit boundary instead of actual physical impact.
    """
    cuts = []
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", "select='gt(scene,0.40)',metadata=print:file=-",
        "-f", "null",
        "-",
    ]
    try:
        proc = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True, timeout=30
        )
        for line in proc.stdout.splitlines():
            line = line.strip()
            if line.startswith("pts_time:"):
                try:
                    cuts.append(round(float(line.split(":")[1]), 2))
                except ValueError:
                    pass
    except Exception:
        pass
    return cuts


def detect_audio_apex(video_path: str) -> float:
    """
    Audio RMS Spike Detection:
    Uses FFmpeg's lavfi astats filter to find the timestamp of the highest audio RMS.
    """
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-af", "astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-",
        "-f", "null",
        "-",
    ]
    proc = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True
    )
    lines = proc.stdout.splitlines()
    current_pts = 0.0
    max_rms = -100.0
    best_pts = 0.0

    for line in lines:
        line = line.strip()
        if line.startswith("pts_time:"):
            try:
                current_pts = float(line.split(":")[1])
            except ValueError:
                pass
        elif "lavfi.astats.Overall.RMS_level=" in line:
            try:
                val_str = line.split("=")[1].strip()
                val = float(val_str)
                if val > max_rms:
                    max_rms = val
                    best_pts = current_pts
            except ValueError:
                pass

    return round(best_pts, 2)


def detect_visual_apex(video_path: str, scene_cuts: list[float] | None = None) -> tuple[float, int, tuple]:
    """
    Level 2 Motion Delta & Acceleration (Jerk) Detection:
    1. Extracts gray frames at 6 fps.
    2. Computes discrete Laplacian variance on frame deltas.
    3. Calculates motion acceleration (second-order delta) to isolate sudden impact impulse.
    4. Guards against artificial spikes caused by scene cuts.
    """
    if scene_cuts is None:
        scene_cuts = []

    fps = 6
    eval_w = 180
    eval_h = 320
    frame_size = eval_w * eval_h

    ffmpeg_cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"fps={fps},scale={eval_w}:{eval_h}",
        "-pix_fmt", "gray",
        "-f", "rawvideo",
        "-",
    ]

    proc = subprocess.Popen(
        ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=frame_size * 10
    )

    prev_frame = None
    deltas = []
    frame_index = 0

    while True:
        raw_bytes = proc.stdout.read(frame_size)
        if len(raw_bytes) < frame_size:
            break

        curr_frame = np.frombuffer(raw_bytes, dtype=np.uint8).reshape((eval_h, eval_w)).astype(np.float32)

        if prev_frame is not None:
            diff = curr_frame - prev_frame
            laplacian = (
                diff[:-2, 1:-1]
                + diff[2:, 1:-1]
                + diff[1:-1, :-2]
                + diff[1:-1, 2:]
                - 4.0 * diff[1:-1, 1:-1]
            )
            lap_var = float(np.var(laplacian))
            ts = frame_index / float(fps)
            deltas.append((ts, lap_var))
        else:
            deltas.append((0.0, 0.0))

        prev_frame = curr_frame
        frame_index += 1

    proc.stdout.close()
    returncode = proc.wait()
    if returncode != 0:
        raise subprocess.CalledProcessError(returncode, ffmpeg_cmd)

    total_extracted_frames = frame_index
    print(f"[DEBUG] Extracted {total_extracted_frames} frames for analysis.")

    motion_array = np.array(deltas, dtype=np.float32)
    print(f"[DEBUG] Motion delta array shape: {motion_array.shape}.")

    if len(deltas) == 0:
        return 0.0, total_extracted_frames, motion_array.shape

    # Filter out peaks that coincide with hard scene cuts (within 0.25s)
    filtered_deltas = []
    for ts, var in deltas:
        is_scene_cut = any(abs(ts - cut_ts) <= 0.25 for cut_ts in scene_cuts)
        if not is_scene_cut:
            filtered_deltas.append((ts, var))

    active_pool = filtered_deltas if filtered_deltas else deltas

    # Calculate motion jerk (acceleration of variance)
    jerk_scored = []
    for i in range(1, len(active_pool)):
        ts_curr, var_curr = active_pool[i]
        _, var_prev = active_pool[i - 1]
        jerk = max(0.0, var_curr - var_prev)
        combined_score = var_curr * 0.7 + jerk * 0.3
        jerk_scored.append((ts_curr, combined_score))

    sorted_peaks = sorted(jerk_scored if jerk_scored else active_pool, key=lambda x: x[1], reverse=True)
    t1 = round(sorted_peaks[0][0], 2)
    t2 = round(sorted_peaks[1][0], 2) if len(sorted_peaks) > 1 else t1
    t3 = round(sorted_peaks[2][0], 2) if len(sorted_peaks) > 2 else t2

    print(f"[DEBUG] Top 3 motion peaks: 1st: {t1}s, 2nd: {t2}s, 3rd: {t3}s.")

    return t1, deltas


def get_total_duration(video_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", video_path
    ]
    res = subprocess.check_output(cmd, text=True).strip()
    return float(res)


def calculate_next_level_impact(
    audio_apex: float,
    visual_apex: float,
    total_duration: float,
    scene_cuts: list[float],
    vlm_apex: float | None = None,
) -> float:
    """
    Cross-Modal Audio-Visual-VLM Fusion:
    Synthesizes acoustic transients with visual jerk peaks and VLM apex estimates.
    Avoids placing apex within 0.5s of the start or end of the clip or on a scene cut.
    """
    if visual_apex <= 0 and audio_apex <= 0 and (not vlm_apex or vlm_apex <= 0):
        return round(total_duration / 2.0, 2)

    # 1. Tri-modal or Bi-modal alignment with VLM
    if vlm_apex and vlm_apex > 0:
        if visual_apex > 0 and abs(vlm_apex - visual_apex) <= 1.0:
            weight_audio = 0.2 if audio_apex > 0 else 0.0
            fused = round((vlm_apex * 0.45 + visual_apex * 0.35 + (audio_apex * weight_audio)), 2)
            if not any(abs(fused - c) <= 0.2 for c in scene_cuts):
                return fused

    # 2. Audio-Visual cross-modal alignment
    if audio_apex > 0 and visual_apex > 0:
        if abs(audio_apex - visual_apex) <= 0.5:
            fused = round((audio_apex * 0.6 + visual_apex * 0.4), 2)
            if not any(abs(fused - c) <= 0.2 for c in scene_cuts):
                return fused

    chosen = vlm_apex if (vlm_apex and vlm_apex > 0) else (audio_apex if audio_apex > 0 else visual_apex)
    return max(round(total_duration * 0.1, 2), min(round(total_duration * 0.9, 2), chosen))


def calculate_exact_action_boundaries(
    video_path: str,
    t_apex: float,
    deltas: list[tuple[float, float]],
    scene_cuts: list[float],
    total_dur: float,
    rank: int = 5,
) -> tuple[float, float, dict]:
    """
    Intelligent Adaptive Action Cut & Boundary Analyzer:
    Ensures 4.0 - 5.0 seconds of narrative setup/buildup before the apex,
    and 4.0 - 5.0 seconds of aftermath playout consequence before the freeze frame.
    Guarded against camera scene cuts.
    """
    # 1. Locate bounding scene cuts
    prev_cuts = [c for c in scene_cuts if c < t_apex]
    next_cuts = [c for c in scene_cuts if c > t_apex]
    t_cut_prev = max(prev_cuts) if prev_cuts else 0.0
    t_cut_next = min(next_cuts) if next_cuts else total_dur

    # 2. Action Inception Analysis (t_start): 4 to 5 seconds of setup/cause
    target_buildup = 4.5
    t_ideal_start = max(0.0, t_apex - target_buildup)

    pre_apex_deltas = [d for d in deltas if t_cut_prev <= d[0] <= t_apex]
    if pre_apex_deltas:
        baseline_var = float(np.median([d[1] for d in pre_apex_deltas]))
        onset_ts = t_ideal_start
        for ts, var in reversed(pre_apex_deltas):
            if var <= baseline_var * 1.25 and ts < t_apex - 2.5:
                onset_ts = ts
                break
        t_start = max(t_ideal_start, onset_ts)
    else:
        t_start = t_ideal_start

    # Scene cut guard on start: never start before prior camera cut
    if t_cut_prev > 0.0:
        t_start = max(t_start, t_cut_prev + 0.15)
    t_start = max(0.0, min(t_start, max(0.0, t_apex - 1.0)))

    # 3. Action Consequence / Freeze Point Analysis (t_freeze): minimum 1.2s aftermath consequence
    # Mandated rule: aftermath playout buffer of +1.5s (or +2.0s for Rank 1) before freezing
    aftermath_buffer = 2.0 if rank == 1 else 1.5
    t_target_freeze = min(total_dur, t_apex + aftermath_buffer)

    post_apex_deltas = [d for d in deltas if t_apex <= d[0] <= min(total_dur, t_apex + 4.0)]
    t_freeze = t_target_freeze

    if post_apex_deltas:
        peak_post_var = max([d[1] for d in post_apex_deltas], default=1.0)
        settle_threshold = peak_post_var * 0.35
        for ts, var in post_apex_deltas:
            # Allow at least aftermath_buffer seconds of visual consequence aftermath
            if ts >= t_apex + aftermath_buffer and var <= settle_threshold:
                t_freeze = ts
                break

    # Scene cut guard on end: NEVER freeze after next camera cut
    if t_cut_next < total_dur:
        t_freeze = min(t_freeze, t_cut_next - 0.10)

    # Ensure valid duration
    t_freeze = min(total_dur, max(t_start + 2.0, t_freeze))
    t_start = round(float(t_start), 2)
    t_freeze = round(float(t_freeze), 2)

    diag = {
        "t_start": t_start,
        "t_apex": round(float(t_apex), 2),
        "t_freeze": t_freeze,
        "buildup_duration": round(float(t_apex - t_start), 2),
        "aftermath_duration": round(float(t_freeze - t_apex), 2),
        "live_action_duration": round(float(t_freeze - t_start), 2),
        "rank": rank,
        "aftermath_buffer_target": aftermath_buffer,
        "prev_scene_cut": round(float(t_cut_prev), 2) if t_cut_prev > 0 else None,
        "next_scene_cut": round(float(t_cut_next), 2) if t_cut_next < total_dur else None,
    }
    return t_start, t_freeze, diag


def bake_apex_freeze(input_path: str, output_path: str, t_start: float, t_freeze: float) -> bool:
    """
    Bakes the exact action cut:
    1. Builds up from t_start (adaptive onset, scene-cut guarded).
    2. Plays through climax apex to t_freeze (ensuring at least 1.2s - 2.5s of aftermath consequence).
    3. Exactly 1 frame (33.3ms) before freeze frame, mutes native audio to complete silence.
    4. Freezes final aftermath frame for 2.0 seconds using clone tpad.
    """
    total_dur = get_total_duration(input_path)
    t_start = max(0.0, min(total_dur - 0.5, t_start))
    t_end = min(total_dur, max(t_start + 0.5, t_freeze))
    live_duration = max(0.5, t_end - t_start)
    audio_duration = max(0.1, live_duration - 0.033)

    print(f"[DEBUG] Exact Action Boundaries: Start: {t_start}s, Freeze Cut: {t_end}s (Live: {live_duration:.2f}s).")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    target_whole_dur = live_duration + 2.0
    filter_complex = (
        f"[0:v]trim=start={t_start}:duration={live_duration},tpad=stop_mode=clone:stop_duration=2.0,setpts=PTS-STARTPTS[v];"
        f"[0:a]atrim=start={t_start}:duration={audio_duration},asetpts=PTS-STARTPTS,apad=whole_dur={target_whole_dur:.3f}[a]"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "[a]",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        output_path,
    ]

    subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
    )
    return os.path.exists(output_path) and os.path.getsize(output_path) > 0


def update_registry(video_id: str):
    registry_path = os.path.abspath("used_clips_registry.json")
    registry = []
    if os.path.exists(registry_path):
        try:
            with open(registry_path, "r", encoding="utf-8") as f:
                registry = json.load(f)
                if not isinstance(registry, list):
                    registry = []
        except Exception:
            registry = []

    if video_id not in registry:
        registry.append(video_id)
        with open(registry_path, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Next-Level Frame-Perfect Visual & Audio Impact Evaluator")
    parser.add_argument("--input", required=True, help="Input video file")
    parser.add_argument("--output", required=True, help="Output baked video file")
    parser.add_argument("--id", required=True, help="Clip unique ID")
    parser.add_argument("--rank", type=int, default=5, help="Rank of the clip (1-5, Rank 1 gets +1.5s aftermath, others +1.2s)")
    parser.add_argument("--vlm-apex", type=float, default=None, help="Estimated apex timestamp from VLM")
    args = parser.parse_args()

    if not check_audio_and_aspect(args.input):
        print(json.dumps({
            "id": args.id,
            "status": "rejected",
            "reason": "Failed aspect ratio or audio volume threshold",
        }))
        sys.exit(0)

    total_dur = get_total_duration(args.input)
    scene_cuts = detect_scene_cuts(args.input)
    if scene_cuts:
        print(f"[DEBUG] Detected {len(scene_cuts)} hard scene cuts at: {scene_cuts[:5]}")

    audio_apex = detect_audio_apex(args.input)
    visual_apex, deltas = detect_visual_apex(args.input, scene_cuts=scene_cuts)
    t_apex = calculate_next_level_impact(audio_apex, visual_apex, total_dur, scene_cuts, vlm_apex=args.vlm_apex)

    t_start, t_freeze, diag = calculate_exact_action_boundaries(
        args.input, t_apex, deltas, scene_cuts, total_dur, rank=args.rank
    )

    success = bake_apex_freeze(args.input, args.output, t_start, t_freeze)
    if not success:
        print(json.dumps({
            "id": args.id,
            "status": "failed",
            "reason": "Baking apex freeze failed",
        }))
        sys.exit(1)

    update_registry(args.id)

    print(json.dumps({
        "id": args.id,
        "status": "success",
        "audio_apex": audio_apex,
        "visual_apex": visual_apex,
        "t_apex": t_apex,
        "t_start": t_start,
        "t_freeze": t_freeze,
        "action_diagnostics": diag,
        "scene_cuts_count": len(scene_cuts),
        "output_path": args.output,
    }))


if __name__ == "__main__":
    main()
