import os
import sys
import json
import argparse
import subprocess
import re

def check_file_format(video_path: str) -> tuple[bool, str, dict]:
    """
    FFprobe check:
    - Aspect ratio: Height / Width >= 1.5 (strict vertical 9:16)
    - Audio presence: mean_volume >= -45 dB
    """
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,duration",
        "-of", "json",
        video_path
    ]
    try:
        res = subprocess.check_output(probe_cmd, text=True)
        data = json.loads(res)
        stream = data.get("streams", [{}])[0]
        w = int(stream.get("width", 0))
        h = int(stream.get("height", 0))
        duration = float(stream.get("duration", 0) or 0)
    except Exception as e:
        return False, f"ffprobe video stream error: {e}", {}

    if w <= 0 or h <= 0:
        return False, "Invalid video dimensions", {}

    ratio = h / float(w)
    if ratio < 1.45:
        return False, f"Non-vertical aspect ratio (H/W={ratio:.2f} < 1.45)", {"width": w, "height": h, "ratio": ratio}

    # Audio presence check
    vol_cmd = [
        "ffmpeg", "-i", video_path,
        "-af", "volumedetect",
        "-vn", "-sn", "-dn",
        "-f", "null", "NUL" if sys.platform == "win32" else "/dev/null"
    ]
    try:
        vol_proc = subprocess.run(vol_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        match = re.search(r"mean_volume:\s*(-?[\d.]+)\s*dB", vol_proc.stderr)
        if not match:
            return False, "No audio stream detected", {"width": w, "height": h, "ratio": ratio}
        mean_vol = float(match.group(1))
        if mean_vol < -45.0:
            return False, f"Audio too quiet (mean_volume={mean_vol} dB < -45 dB)", {"mean_volume": mean_vol}
    except Exception as e:
        return False, f"Audio volumedetect error: {e}", {}

    return True, "Valid vertical video with natural audio", {
        "width": w,
        "height": h,
        "ratio": ratio,
        "duration": duration,
        "mean_volume": mean_vol
    }

def harvest_social_candidates(
    platform: str,
    query: str,
    count: int = 5,
    temp_dir: str = "temp_harvest"
) -> list[dict]:
    """
    Harvests vertical video candidates strictly from TikTok and Instagram Reels using yt-dlp.
    Saves candidates into temp_harvest/{platform}_{video_id}.mp4.
    """
    os.makedirs(temp_dir, exist_ok=True)
    query_slug = query.replace(" ", "")
    
    # Formulate platform URL or ytsearch queries
    search_targets = []
    if platform.lower() == "tiktok":
        search_targets.append(f"https://www.tiktok.com/tag/{query_slug}")
        search_targets.append(f"ytsearch15:{query} tiktok #shorts")
    elif platform.lower() == "instagram":
        search_targets.append(f"https://www.instagram.com/explore/tags/{query_slug}/")
        search_targets.append(f"ytsearch15:{query} instagram reels #shorts")
    else:
        # Generic multi-source fallback
        search_targets.append(f"ytsearch15:{query} viral #shorts")

    approved_candidates = []
    seen_ids = set()

    for target in search_targets:
        if len(approved_candidates) >= count:
            break

        print(f"[SocialHarvester] Querying target: {target}", file=sys.stderr)
        dump_cmd = [
            sys.executable, "-m", "yt_dlp",
            "--dump-json",
            "--no-playlist",
            "--ignore-errors",
            target
        ]

        try:
            proc = subprocess.run(dump_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace", timeout=30)
        except Exception as e:
            print(f"[SocialHarvester] Dump error: {e}", file=sys.stderr)
            continue

        if proc.returncode != 0 or not proc.stdout:
            continue

        for line in proc.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except Exception:
                continue

            vid_id = item.get("id")
            if not vid_id or vid_id in seen_ids:
                continue
            seen_ids.add(vid_id)

            title = item.get("title", "")
            description = item.get("description", "")
            duration = item.get("duration") or 0

            # Only accept raw clips between 8s and 90s
            if duration and (duration < 6.0 or duration > 90.0):
                continue

            target_mp4 = os.path.join(temp_dir, f"{platform}_{vid_id}.mp4")
            video_url = item.get("webpage_url") or item.get("url") or f"https://www.youtube.com/watch?v={vid_id}"

            if not os.path.exists(target_mp4) or os.path.getsize(target_mp4) == 0:
                dl_cmd = [
                    sys.executable, "-m", "yt_dlp",
                    "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                    "--merge-output-format", "mp4",
                    "-o", target_mp4,
                    "--no-playlist",
                    "--quiet",
                    video_url
                ]
                try:
                    dl_proc = subprocess.run(dl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
                    if dl_proc.returncode != 0 or not os.path.exists(target_mp4):
                        continue
                except Exception:
                    continue

            # Strict file checks (9:16 vertical & audio check)
            is_valid, reason, meta = check_file_format(target_mp4)
            if not is_valid:
                print(f"[SocialHarvester] Rejected {vid_id}: {reason}", file=sys.stderr)
                try:
                    os.remove(target_mp4)
                except Exception:
                    pass
                continue

            print(f"[SocialHarvester] Candidate Passed Strict Ingestion: {vid_id} (ratio: {meta.get('ratio'):.2f}, vol: {meta.get('mean_volume'):.1f}dB)", file=sys.stderr)
            approved_candidates.append({
                "id": vid_id,
                "platform": platform,
                "title": title,
                "description": description,
                "file_path": os.path.abspath(target_mp4),
                "duration": meta.get("duration", duration)
            })

            if len(approved_candidates) >= count:
                break

    return approved_candidates

def main():
    parser = argparse.ArgumentParser(description="TikTok & Instagram Reels Raw Harvester")
    parser.add_argument("--platform", default="tiktok", choices=["tiktok", "instagram", "all"], help="Platform to harvest from")
    parser.add_argument("--query", required=True, help="Search query (e.g. car crash instant karma)")
    parser.add_argument("--count", type=int, default=5, help="Number of approved candidates to deliver")
    parser.add_argument("--temp-dir", default="temp_harvest", help="Staging output directory")
    args = parser.parse_args()

    candidates = harvest_social_candidates(
        platform=args.platform,
        query=args.query,
        count=args.count,
        temp_dir=args.temp_dir
    )
    print(json.dumps(candidates))

if __name__ == "__main__":
    main()
