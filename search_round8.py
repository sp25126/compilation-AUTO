import subprocess
import json

queries = [
    "pranking my boyfriend cute shorts",
    "sweet couple prank shorts",
    "couple prank hug shorts",
    "kiss prank on boyfriend cute shorts",
    "prank on husband cute laugh shorts",
    "holding hand prank husband shorts",
    "boyfriend cute reaction prank shorts",
    "wholesome couple prank laugh shorts"
]

results = []
seen = set()

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        "--match-filter", "duration <= 60 & duration >= 7",
        f"ytsearch10:{q}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            vid = d.get("id")
            dur = d.get("duration") or 0
            views = d.get("view_count") or 0
            title = d.get("title") or ""
            low = title.lower()
            if any(b in low for b in ["compilation", "reacting", "minecraft", "roblox"]):
                continue
            if vid and vid not in seen:
                seen.add(vid)
                results.append({"id": vid, "title": title, "duration": dur, "views": views})
        except:
            pass

print(f"Total found: {len(results)}")
for r in sorted(results, key=lambda x: x.get("views") or 0, reverse=True)[:35]:
    print(f"[{r.get('views')} views, {r.get('duration')}s] {r['id']}: {r['title']}")

with open("temp_harvest/couple_pranks_gone_wholesome/search_round8.json", "w") as f:
    json.dump(results, f, indent=2)
