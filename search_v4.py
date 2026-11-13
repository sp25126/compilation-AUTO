import subprocess
import json
import os

queries = [
    "couple prank reaction #shorts",
    "prank on husband #shorts",
    "prank on wife wholesome #shorts",
    "prank on boyfriend cute #shorts",
    "couple prank gone right #shorts",
    "kiss prank boyfriend girlfriend #shorts",
    "pretending to sleep on boyfriend #shorts",
    "cute couple laugh prank #shorts",
    "husband pranking wife cute #shorts"
]

results = []
seen_ids = set()

for q in queries:
    print(f"Running: {q}")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        "--match-filter", "duration <= 65 & duration >= 10",
        f"ytsearch12:{q}"
    ]
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
            if any(bad in low_t for bad in ["compilation", "reacting", "minecraft", "roblox", "podcast"]):
                continue
            if vid_id and vid_id not in seen_ids:
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
with open("temp_harvest/couple_pranks_gone_wholesome/candidates_v4.json", "w") as f:
    json.dump(results, f, indent=2)

for r in sorted(results, key=lambda x: x.get("views") or 0, reverse=True)[:35]:
    print(f"[{r.get('views')} views, {r.get('duration')}s] {r['id']}: {r['title']}")
