import subprocess
import json

queries = [
    "npc repeating same phrase funny shorts",
    "real life npc talking loop funny shorts",
    "two guys saying whats up loop funny",
    "saying excuse me back and forth loop funny",
    "saying hello loop funny shorts",
    "npc glitch talking in real life funny shorts",
    "people stuck in a loop talking funny shorts"
]

all_vids = {}

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
            if 5 <= dur <= 50 and views >= 10000:
                if vid_id not in all_vids:
                    all_vids[vid_id] = {
                        "id": vid_id,
                        "title": title,
                        "duration": dur,
                        "views": views
                    }
    except Exception as e:
        print(e)

print(f"Found {len(all_vids)} candidates:")
for c in sorted(all_vids.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")

with open("temp_harvest/dialogue_loop_real_life/loop_search_final.json", "w", encoding="utf-8") as f:
    json.dump(list(all_vids.values()), f, indent=2)
