import subprocess
import json
import sys

queries = [
    "people repeating same phrase npc glitch funny shorts",
    "real life npc dialogue loop funny shorts",
    "strangers saying same thing at same time funny shorts",
    "npc dialogue loop in public funny cctv shorts",
    "real life glitch npc repeating sentence shorts",
    "real life npc repetition glitch caught on camera shorts",
    "npc repeating dialogue in real life funny shorts",
    "npc dialogue loop real life shorts"
]

all_candidates = {}

for q in queries:
    print(f"Searching: {q}")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch12:{q}"
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
                # filter: 5s <= dur <= 50s, views >= 10000
                if vid_id and dur and (5 <= dur <= 50) and (views >= 10000):
                    if vid_id not in all_candidates:
                        all_candidates[vid_id] = {
                            "id": vid_id,
                            "title": title,
                            "duration": dur,
                            "views": views,
                            "url": f"https://www.youtube.com/watch?v={vid_id}"
                        }
            except Exception as e:
                pass
    except Exception as e:
        print(f"Error querying {q}: {e}")

print(f"\nFound {len(all_candidates)} candidates meeting duration & view filters:")
for c in sorted(all_candidates.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")

with open("temp_harvest/dialogue_loop_real_life/candidates.json", "w", encoding="utf-8") as f:
    json.dump(list(all_candidates.values()), f, indent=2)
