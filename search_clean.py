import subprocess
import json

queries = [
    "not kissing boyfriend goodbye reaction",
    "forgetting to kiss goodbye prank",
    "leaving without kissing husband reaction",
    "asking boyfriend for food prank",
    "pretending to steal food from boyfriend",
    "boyfriend reaction girlfriend sitting on lap",
    "girlfriend sits on boyfriend lap while gaming",
    "couple eye contact challenge laugh",
    "serious stare challenge couple",
    "whispering random words to boyfriend",
    "sniffing boyfriend reaction cute",
    "hand on leg while driving boyfriend reaction",
    "complimenting boyfriend reaction blushing"
]

results = []
seen = set()

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        "--match-filter", "duration <= 55 & duration >= 8",
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

with open("temp_harvest/couple_pranks_gone_wholesome/clean_candidates.json", "w") as f:
    json.dump(results, f, indent=2)
