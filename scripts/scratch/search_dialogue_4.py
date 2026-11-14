import subprocess
import json

queries = [
    "karen repeating same word loop funny shorts",
    "customer repeating same phrase funny shorts",
    "fast food npc dialogue loop funny shorts",
    "npc stuck saying same word funny shorts",
    "strangers say same phrase at same time funny shorts",
    "talking at same time glitch funny shorts",
    "two people saying the exact same sentence funny shorts",
    "npc dialogue loop funny caught on tape shorts",
    "hilarious dialogue loop real life shorts",
    "npc loop glitch public funny shorts"
]

results = {}
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
                if vid_id and dur and (5 <= dur <= 50):
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

print(f"Found {len(results)} new candidates:")
for c in sorted(results.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")

with open("temp_harvest/dialogue_loop_real_life/loop_candidates.json", "w", encoding="utf-8") as f:
    json.dump(list(results.values()), f, indent=2)
