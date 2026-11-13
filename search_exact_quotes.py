import subprocess
import json

queries = [
    "\"prank on my husband\" shorts",
    "\"prank on my boyfriend\" shorts",
    "\"pranking my wife\" shorts",
    "\"couple prank\" laugh shorts",
    "\"prank on girlfriend\" sweet shorts"
]

results = []
seen = set()

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        "--match-filter", "duration <= 60 & duration >= 10",
        f"ytsearch10:{q}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            vid = d.get("id")
            title = d.get("title") or ""
            dur = d.get("duration") or 0
            low = title.lower()
            if any(b in low for b in ["compilation", "reacting", "minecraft", "roblox"]):
                continue
            if vid and vid not in seen:
                seen.add(vid)
                results.append({"id": vid, "title": title, "duration": dur})
                print(f"[{dur}s] {vid}: {title}", flush=True)
        except:
            pass

with open("temp_harvest/couple_pranks_gone_wholesome/exact_quotes.json", "w") as f:
    json.dump(results, f, indent=2)
