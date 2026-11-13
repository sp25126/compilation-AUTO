import json
import subprocess
import os

queries = [
    "commercial kitchen fails slip sauce",
    "chef drops giant pot of soup cctv",
    "kitchen staff drops giant pot",
    "restaurant kitchen floor slip spill",
    "kitchen disaster giant soup spill",
    "chef dropped 50 lbs flour",
    "line cook slips on grease spill",
    "restaurant cctv kitchen fail",
    "dishwasher tray drop kitchen fail",
    "huge pot of beans falls chef",
    "spilled giant pot of chili kitchen",
    "baker dropped giant bowl of dough"
]

results = []
for q in queries:
    cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch8:{q}"]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in p.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            item = json.loads(line)
            dur = item.get("duration") or 0
            views = item.get("view_count") or 0
            vid_id = item.get("id")
            title = item.get("title")
            if 4 <= dur <= 60 and views >= 10000:
                results.append({
                    "id": vid_id,
                    "title": title,
                    "duration": dur,
                    "views": views,
                    "url": f"https://www.youtube.com/watch?v={vid_id}"
                })
        except Exception as e:
            pass

seen = set()
unique = []
for r in results:
    if r["id"] not in seen:
        seen.add(r["id"])
        unique.append(r)

print(f"Found {len(unique)} candidate videos:")
for u in unique:
    print(f"[{u['id']}] {u['duration']}s | {u['views']} views | {u['title']}")

with open("temp_harvest/commercial_kitchen_nightmares/candidates.json", "w", encoding="utf-8") as f:
    json.dump(unique, f, indent=2)
