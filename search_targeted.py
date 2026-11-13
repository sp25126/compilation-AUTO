import subprocess
import json

queries = [
    "lucky golf bounce hole in one shorts",
    "accidental basketball bounce in net shorts",
    "luckiest pool shot ever shorts",
    "accidental beer pong bounce shorts",
    "lucky table tennis bounce shot shorts",
    "unintentional bottle flip land shorts",
    "accidental flip lands perfectly shorts",
    "luckiest bounce into cup shorts"
]

results = []
seen = set()

for q in queries:
    cmd = ["py", "-3", "-m", "yt_dlp", "--flat-playlist", "--dump-json", f"ytsearch6:{q}"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    for line in p.stdout.splitlines():
        if not line.strip():
            continue
        try:
            d = json.loads(line)
            dur = d.get("duration") or 0
            views = d.get("view_count") or 0
            id_ = d.get("id")
            title = d.get("title", "")
            low_t = title.lower()
            if any(bad in low_t for bad in ["gta", "minecraft", "fortnite", "roblox", "2k", "fifa", "animation", "gameplay", "mod"]):
                continue
            if 5 <= dur <= 45 and id_ and id_ not in seen:
                seen.add(id_)
                results.append({
                    "id": id_,
                    "title": title,
                    "duration": dur,
                    "views": views,
                    "url": f"https://www.youtube.com/watch?v={id_}"
                })
        except Exception:
            pass

results.sort(key=lambda x: x["views"] or 0, reverse=True)
print(f"Got {len(results)} targeted candidates:")
for r in results[:20]:
    print(f"[{r['id']}] ({r['duration']}s, {r.get('views', 0):,} views): {r['title']}")

with open("temp_harvest/accidental_trickshots/targeted_candidates.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
