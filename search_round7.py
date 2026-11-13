import subprocess
import json

queries = [
    "boyfriend takes a video instead of a picture prank shorts",
    "fake picture taking boyfriend reaction shorts",
    "posing for a picture but it's a video prank couple",
    "asking boyfriend for a bite of his food prank shorts",
    "staring at husband until he laughs shorts",
    "putting head on boyfriend shoulder prank shorts",
    "fake sneeze prank boyfriend reaction shorts",
    "asking husband to hold purse prank reaction shorts",
    "ignoring boyfriend until he begs for attention shorts"
]

results = []
seen = set()

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        "--match-filter", "duration <= 65 & duration >= 8",
        f"ytsearch8:{q}"
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

with open("temp_harvest/couple_pranks_gone_wholesome/search_round7.json", "w") as f:
    json.dump(results, f, indent=2)
