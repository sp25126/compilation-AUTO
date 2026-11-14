import subprocess
import json

targets = [
    "you're not that guy pal original video",
    "you're not that guy pal full clip",
    "what is your name ezekiel original video",
    "fuck you ezekiel original video",
    "two guys saying hello to each other loop funny",
    "saying whats up over and over funny",
    "drive thru prank looping questions funny",
    "karen repeating same sentence over and over",
    "sovereign citizen repeating am i being detained loop",
    "two people say the exact same thing at the exact same time glitch"
]

all_vids = {}

for q in targets:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch5:{q}"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        for line in res.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                data = json.loads(line)
                vid_id = data.get("id")
                dur = data.get("duration")
                views = data.get("view_count") or 0
                title = data.get("title", "")
                if vid_id and dur and (4 <= dur <= 60):
                    if vid_id not in all_vids:
                        all_vids[vid_id] = {
                            "id": vid_id,
                            "title": title,
                            "duration": dur,
                            "views": views
                        }
            except Exception:
                pass
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Found {len(all_vids)} clean targets:")
for c in sorted(all_vids.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")

with open("temp_harvest/dialogue_loop_real_life/clean_targets.json", "w", encoding="utf-8") as f:
    json.dump(list(all_vids.values()), f, indent=2)
