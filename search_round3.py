import subprocess
import json

queries = [
    "girlfriend wont let go of hand reaction shorts",
    "touching boyfriends ear reaction shorts",
    "prank on girlfriend hug reaction shorts",
    "staring at boyfriend without blinking shorts",
    "pretending to sleep on boyfriend lap shorts",
    "whispering to boyfriend while he plays games shorts",
    "giving boyfriend cute surprise reaction shorts",
    "boyfriend reaction girlfriend sitting on his lap shorts"
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
            if dur and not (8 <= dur <= 60):
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

with open("temp_harvest/couple_pranks_gone_wholesome/fast_round3.json", "w") as f:
    json.dump(results, f, indent=2)
