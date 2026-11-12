import subprocess
import json
import os
import sys

search_terms = [
    "he accepted his fate",
    "accepted his fate fail",
    "accepting fate meme",
    "this is the end fail",
    "gave up mid fall fail",
    "cat accepted fate",
    "dog accepted fate",
    "sliding on ice accepted fate"
]

found_videos = []
seen_ids = set()

for term in search_terms:
    print(f"\n=== Searching: {term} ===")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        f"ytsearch8:{term} shorts",
        "--dump-json",
        "--no-playlist"
    ]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
        stdout, _ = proc.communicate(timeout=35)
        for line in stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                vid = data.get("id")
                title = data.get("title", "")
                dur = data.get("duration", 0)
                views = data.get("view_count", 0)
                w = data.get("width", 0) or 0
                h = data.get("height", 0) or 0
                
                # Check for vertical or short duration <= 60s
                if vid and vid not in seen_ids and dur and dur <= 60:
                    seen_ids.add(vid)
                    found_videos.append({
                        "id": vid,
                        "title": title,
                        "duration": dur,
                        "views": views,
                        "width": w,
                        "height": h,
                        "url": f"https://www.youtube.com/shorts/{vid}"
                    })
                    print(f"  [FOUND] {vid} ({dur}s, {views:,} views): {title}")
            except Exception:
                pass
    except Exception as e:
        print(f"Error querying {term}: {e}")

print(f"\nTotal Candidates: {len(found_videos)}")
with open("raw_candidates_fate.json", "w", encoding="utf-8") as f:
    json.dump(found_videos, f, indent=2)
