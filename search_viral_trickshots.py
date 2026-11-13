import subprocess
import json

queries = [
    "accidental trick shot",
    "luckiest shot caught on camera",
    "accidental bottle flip",
    "luckiest bounce basketball",
    "luckiest trickshot caught on camera",
    "accidental trickshot",
    "unintentional trickshot",
    "pure luck trickshot",
    "impossible lucky bounce",
    "accidental cup shot",
    "accidental basketball half court",
    "luckiest bounce ever"
]

results = []
seen_ids = set()

for q in queries:
    print(f"Searching: {q}")
    cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch15:{q}"]
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
            low_t = title.lower()
            if any(bad in low_t for bad in ["gta", "minecraft", "fortnite", "roblox", "2k", "fifa", "animation", "gameplay", "mod", "compilation", "top 10", "top 5"]):
                continue
            if vid_id and vid_id not in seen_ids and 5 <= dur <= 60 and views >= 10000:
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

print(f"\nFound {len(results)} high-view candidates:")
results.sort(key=lambda x: x["views"] or 0, reverse=True)
for r in results[:30]:
    print(f"ID: {r['id']} | Dur: {r['duration']}s | Views: {r['views']:,} | Title: {r['title']}")

with open("temp_harvest/accidental_trickshots/yt_viral_candidates.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
