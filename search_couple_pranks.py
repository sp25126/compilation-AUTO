import subprocess
import json
import os

queries = [
    "couple prank wholesome shorts",
    "wholesome couple pranks shorts",
    "invisible string prank couple shorts",
    "lip balm trick boyfriend reaction shorts",
    "prank on boyfriend turned wholesome shorts",
    "prank on girlfriend sweet reaction shorts",
    "couple pranking each other cute shorts",
    "fake spill prank boyfriend girlfriend shorts",
    "cute couple prank hug shorts"
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
            low_t = title.lower()
            if any(bad in low_t for bad in ["compilation", "reacting to", "podcast", "minecraft", "roblox"]):
                continue
            if vid_id and vid_id not in seen_ids and 8 <= dur <= 65:
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
os.makedirs("temp_harvest/couple_pranks_gone_wholesome", exist_ok=True)
with open("temp_harvest/couple_pranks_gone_wholesome/candidates.json", "w") as f:
    json.dump(results, f, indent=2)

for r in sorted(results, key=lambda x: x["views"], reverse=True)[:25]:
    print(f"[{r['views']} views, {r['duration']}s] {r['id']}: {r['title']}")
