import subprocess
import json

queries = [
    "taking photo prank boyfriend shorts",
    "taking picture prank boyfriend video shorts",
    "pretending to take picture of my boyfriend shorts",
    "calling boyfriend by first name reaction shorts",
    "calling husband by first name reaction shorts",
    "staring at husband until he laughs shorts",
    "staring at boyfriend until he smiles shorts",
    "fake sneeze prank boyfriend shorts",
    "asking boyfriend for food reaction shorts",
    "sniffing boyfriend reaction shorts"
]

results = []
seen = set()

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch6:{q}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            dur = d.get("duration") or 0
            if dur and not (8 <= dur <= 65):
                continue
            vid = d.get("id")
            title = d.get("title") or ""
            low = title.lower()
            if any(b in low for b in ["compilation", "reacting", "minecraft", "roblox"]):
                continue
            if vid and vid not in seen:
                seen.add(vid)
                results.append({"id": vid, "title": title, "duration": dur})
                print(f"[{dur}s] {vid}: {title}", flush=True)
        except:
            pass

with open("temp_harvest/couple_pranks_gone_wholesome/fast_round2.json", "w") as f:
    json.dump(results, f, indent=2)
