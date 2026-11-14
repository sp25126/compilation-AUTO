import subprocess
import json

queries = [
    "people repeating the same phrase over and over funny shorts",
    "two people say same thing at same time glitch shorts",
    "npc repeating lines in real life shorts",
    "saying hello to each other in an infinite loop shorts",
    "npc dialogue loop real life shorts",
    "strangers say same thing at same time funny shorts"
]

results = {}
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
                dur = data.get("duration") or 0
                views = data.get("view_count") or 0
                title = data.get("title", "")
                lower = title.lower()
                if any(w in lower for w in ["gta", "minecraft", "roblox", "animation", "fortnite"]):
                    continue
                if 5 <= dur <= 45 and views >= 10000:
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
        print(e)

print(f"Total found: {len(results)}")
for c in sorted(results.values(), key=lambda x: x["views"], reverse=True):
    print(f"- [{c['id']}] ({c['duration']}s, {c['views']} views): {c['title']}")

with open("temp_harvest/dialogue_loop_real_life/more_dialogue_loops.json", "w", encoding="utf-8") as f:
    json.dump(list(results.values()), f, indent=2)
