import subprocess
import json

queries = [
    "npc repeating lines in real life shorts",
    "customer stuck in a loop funny shorts",
    "drive thru infinite loop funny shorts",
    "saying excuse me loop funny shorts",
    "two people saying the exact same thing at the exact same time shorts",
    "glitch in the matrix people talking at the same time shorts",
    "npc dialogue loop funny in real life"
]

found = {}
for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch8:{q}"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        for line in res.stdout.strip().split("\n"):
            if not line:
                continue
            data = json.loads(line)
            vid_id = data.get("id")
            dur = data.get("duration") or 0
            views = data.get("view_count") or 0
            title = data.get("title", "")
            lower = title.lower()
            if any(w in lower for w in ["gta", "minecraft", "roblox", "fortnite", "tadc"]):
                continue
            if 5 <= dur <= 55 and views >= 10000:
                if vid_id not in found:
                    found[vid_id] = {
                        "id": vid_id,
                        "title": title,
                        "duration": dur,
                        "views": views
                    }
    except Exception as e:
        print(e)

print(f"Total found: {len(found)}")
for c in sorted(found.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")
