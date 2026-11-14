import subprocess
import json

queries = [
    "npc stuck in a loop real life funny",
    "real life npc loop funny",
    "real life infinite loop talking funny",
    "people repeating the same thing over and over funny",
    "real life npc dialogue funny caught on camera",
    "npc dialogue in real life funny",
    "real life dialogue loop",
    "real life npc broken loop",
    "matrix glitch people talking same time",
    "npc repeating same phrase in public"
]

all_cands = {}

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch10:{q}"
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
                if vid_id and dur and (5 <= dur <= 60):
                    if vid_id not in all_cands:
                        all_cands[vid_id] = {
                            "id": vid_id,
                            "title": title,
                            "duration": dur,
                            "views": views,
                            "url": f"https://www.youtube.com/watch?v={vid_id}"
                        }
            except Exception:
                pass
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Total found: {len(all_cands)}")
for c in sorted(all_cands.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")

with open("temp_harvest/dialogue_loop_real_life/more_candidates.json", "w", encoding="utf-8") as f:
    json.dump(list(all_cands.values()), f, indent=2)
