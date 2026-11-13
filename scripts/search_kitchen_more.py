import subprocess
import json

queries = [
    "cook slips with giant pot",
    "chef drops giant pot of chili",
    "waiter slips drops tray restaurant cctv",
    "restaurant kitchen slip and slide fail",
    "spilled giant pot of food",
    "kitchen staff dropped food cctv",
    "cook drops big pot of soup",
    "chef dropped the beans",
    "spilled curry pot kitchen",
    "waiter drops wedding cake disaster"
]

all_vids = []
seen = set()

for q in queries:
    cmd = ["py", "-3", "-m", "yt_dlp", "--flat-playlist", "--dump-json", f"ytsearch10:{q}"]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in p.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            vid = d.get("id")
            title = d.get("title", "")
            dur = d.get("duration") or 0
            views = d.get("view_count") or 0
            if vid not in seen and 5 <= dur <= 180 and views >= 5000:
                seen.add(vid)
                all_vids.append({
                    "id": vid,
                    "title": title,
                    "dur": dur,
                    "views": views,
                    "url": f"https://www.youtube.com/watch?v={vid}"
                })
        except Exception:
            pass

print(f"Discovered {len(all_vids)} high-quality candidates:")
for v in all_vids:
    print(f"[{v['id']}] {v['dur']}s | {v['views']} views | {v['title']}")

with open("temp_harvest/commercial_kitchen_nightmares/more_candidates.json", "w", encoding="utf-8") as f:
    json.dump(all_vids, f, indent=2)
