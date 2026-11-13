import subprocess
import json
import os

queries = [
    "sniffing boyfriend prank reaction",
    "cute prank on boyfriend reaction",
    "touching hand prank boyfriend",
    "cute prank on girlfriend sweet reaction",
    "harmless couple pranks funny",
    "holding hands with boyfriend prank cute",
    "putting head on shoulder prank couple",
    "girlfriend kissing boyfriend cheek prank",
    "husband reaction to wife prank wholesome"
]

results = []
seen_ids = set()

for q in queries:
    print(f"Searching: {q}")
    cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch10:{q}"]
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
with open("temp_harvest/couple_pranks_gone_wholesome/candidates_v2.json", "w") as f:
    json.dump(results, f, indent=2)

for r in sorted(results, key=lambda x: x["views"], reverse=True)[:30]:
    print(f"[{r['views']} views, {r['duration']}s] {r['id']}: {r['title']}")
