import subprocess
import json
import os

queries = [
    "ice driveway slide fail shorts",
    "guy sliding on ice hands in pocket shorts",
    "ladder sliding down wall fail shorts",
    "roof snow slide fail shorts",
    "canoe waterfall flip fail shorts",
    "pool slide fail shorts",
    "slip and slide disaster funny shorts",
    "guy accepted fate cctv shorts"
]

results = []
seen = set()

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        f"ytsearch6:{q}",
        "--dump-json",
        "--skip-download",
        "--no-playlist"
    ]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
        stdout, _ = proc.communicate(timeout=25)
        for line in stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
                vid = d.get("id")
                dur = d.get("duration", 0)
                title = d.get("title", "")
                views = d.get("view_count", 0)
                # Filter out obvious gaming/animation keywords
                lower_title = title.lower()
                if any(bad in lower_title for bad in ["roblox", "minecraft", "gameplay", "animation", "fortnite", "gta", "reaction", "podcast"]):
                    continue
                if vid and vid not in seen and dur and dur <= 60:
                    seen.add(vid)
                    results.append({
                        "id": vid,
                        "title": title,
                        "duration": dur,
                        "views": views,
                        "url": f"https://www.youtube.com/shorts/{vid}"
                    })
                    print(f"[{vid}] ({dur}s): {title}")
            except Exception:
                pass
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"\nTotal real-life candidates: {len(results)}")
with open("real_life_fate_candidates.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
