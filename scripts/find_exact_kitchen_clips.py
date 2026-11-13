import subprocess
import json

queries = [
    "waiter drops food tray cctv",
    "dropping massive soup vat commercial kitchen",
    "chef drops giant pot of soup",
    "chef dropped wedding cake disaster",
    "waiter falls carrying tray",
    "cook slips carrying food cctv",
    "dropping 50 lbs flour kitchen",
    "spilling giant pot beans kitchen",
    "restaurant dishwasher accident",
    "chef drops tray of food"
]

all_vids = []
seen = set()

for q in queries:
    cmd = ["py", "-3", "-m", "yt_dlp", "--flat-playlist", "--dump-json", f"ytsearch6:{q}"]
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
            if vid not in seen and 5 <= dur <= 120:
                seen.add(vid)
                all_vids.append({
                    "id": vid,
                    "title": title,
                    "dur": dur,
                    "views": views,
                    "query": q,
                    "url": f"https://www.youtube.com/watch?v={vid}"
                })
        except Exception:
            pass

print(f"Discovered {len(all_vids)} potential clips:")
for v in all_vids:
    print(f"[{v['id']}] {v['dur']}s | {v['views']} views | {v['title']} (from '{v['query']}')")

with open("temp_harvest/commercial_kitchen_nightmares/exact_candidates.json", "w", encoding="utf-8") as f:
    json.dump(all_vids, f, indent=2)
