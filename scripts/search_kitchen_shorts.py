import json
import subprocess

shorts_queries = [
    "kitchen fail soup spill #shorts",
    "chef drops giant pot #shorts",
    "restaurant kitchen slip fail #shorts",
    "spilling huge pot of sauce #shorts",
    "kitchen disaster cctv #shorts",
    "chef dropped flour #shorts",
    "dishwasher tray drop #shorts",
    "waiter falls tray food #shorts",
    "restaurant kitchen disaster #shorts",
    "cook slips carrying food #shorts",
    "kitchen fail cctv #shorts",
    "kitchen accident sauce spill #shorts",
    "cooking disaster huge spill #shorts"
]

candidates = []
seen = set()

for q in shorts_queries:
    cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch10:{q}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            item = json.loads(line)
            vid_id = item.get("id")
            title = item.get("title")
            dur = item.get("duration") or 0
            views = item.get("view_count") or 0
            if vid_id in seen:
                continue
            # Look for 5s to 45s videos
            if 5 <= dur <= 45 and views >= 10000:
                seen.add(vid_id)
                candidates.append({
                    "id": vid_id,
                    "title": title,
                    "duration": dur,
                    "views": views,
                    "url": f"https://www.youtube.com/watch?v={vid_id}"
                })
        except Exception:
            pass

print(f"Total authentic candidates found: {len(candidates)}")
for c in candidates:
    print(f"[{c['id']}] {c['duration']}s | {c['views']} views | {c['title']}")

with open("temp_harvest/commercial_kitchen_nightmares/shorts_candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidates, f, indent=2)
