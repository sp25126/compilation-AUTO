import subprocess
import json
import os

queries = [
    "car 360 spin save dashcam shorts",
    "highway 360 car spin recovery shorts",
    "insane drift recovery 360 save",
    "driver 360 spin and keeps going shorts",
    "car spin 360 recovery highway",
    "nurburgring 360 save wet track shorts",
    "rally 360 recovery shorts",
    "car hydroplane 360 recovery"
]

results = []
seen_ids = set()

for q in queries:
    print(f"Searching: {q}")
    cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch8:{q}"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            data = json.loads(line)
            vid_id = data.get("id")
            dur = data.get("duration") or 0
            views = data.get("view_count") or 0
            title = data.get("title") or ""
            # Filter games / GTA / Forza
            low_t = title.lower()
            if any(bad in low_t for bad in ["gta", "forza", "beamng", "assetto", "gameplay", "mod"]):
                continue
            if vid_id and vid_id not in seen_ids and 5 <= dur <= 65:
                seen_ids.add(vid_id)
                results.append({
                    "id": vid_id,
                    "title": title,
                    "duration": dur,
                    "views": views,
                    "url": f"https://www.youtube.com/watch?v={vid_id}"
                })
        except Exception:
            pass

print(f"\nTotal clean candidates found: {len(results)}")
with open("temp_harvest/vehicle_360_recoveries/candidates.json", "w") as f:
    json.dump(results, f, indent=2)

for r in sorted(results, key=lambda x: x["views"], reverse=True)[:15]:
    print(f"[{r['views']} views, {r['duration']}s] {r['id']}: {r['title']}")
