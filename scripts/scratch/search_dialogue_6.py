import subprocess
import json

queries = [
    "people talking like npcs in public funny shorts",
    "real life npc glitch conversation shorts",
    "npc glitch caught on camera talking shorts",
    "strangers say the same thing matrix glitch shorts",
    "real life npc stutter loop shorts",
    "repeating dialogue real life funny shorts",
    "npc dialogue loop funny shorts"
]

all_items = {}
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
            try:
                data = json.loads(line)
                vid_id = data.get("id")
                dur = data.get("duration")
                views = data.get("view_count") or 0
                title = data.get("title", "")
                if vid_id and dur and (5 <= dur <= 45):
                    if vid_id not in all_items:
                        all_items[vid_id] = {
                            "id": vid_id,
                            "title": title,
                            "duration": dur,
                            "views": views
                        }
            except Exception:
                pass
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Found {len(all_items)} results:")
for c in sorted(all_items.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")
