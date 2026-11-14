import subprocess
import json

queries = [
    "you're not that guy pal shorts",
    "two people saying excuse me loop shorts",
    "get out of my car uber loop shorts",
    "hit me hit me fight loop shorts",
    "what are you doing what are you doing loop shorts",
    "what's your name ezekiel shorts",
    "have you ever had a dream kid shorts",
    "can i get a waffle waffle house shorts",
    "strangers saying same thing at same time funny shorts",
    "npc repeating same phrase in real life funny shorts",
    "two guys saying what's up loop funny shorts",
    "real life npc loop conversation shorts",
    "saying excuse me back and forth shorts"
]

results = {}
for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch6:{q}"
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
                if vid_id and dur and (5 <= dur <= 50) and (views >= 10000):
                    if vid_id not in results:
                        results[vid_id] = {
                            "id": vid_id,
                            "title": title,
                            "duration": dur,
                            "views": views
                        }
            except Exception:
                pass
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Found {len(results)} viral real-life loop candidates:")
for c in sorted(results.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")

with open("temp_harvest/dialogue_loop_real_life/viral_loops.json", "w", encoding="utf-8") as f:
    json.dump(list(results.values()), f, indent=2)
