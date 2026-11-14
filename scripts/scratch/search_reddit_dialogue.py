import subprocess
import json
import re

queries = [
    "npc glitch v.redd.it",
    "npc dialogue v.redd.it",
    "npc repeating v.redd.it",
    "stuck in a loop v.redd.it",
    "matrix glitch v.redd.it",
    "npc in real life v.redd.it"
]

found_reddits = {}

for q in queries:
    cmd = ["agent-reach", "reddit", "search", q, "--limit", "8"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.stdout:
            data = json.loads(res.stdout)
            for item in data.get("items", []):
                text = item.get("text", "")
                url = item.get("url", "")
                title = item.get("title", "")
                # search for v.redd.it
                matches = re.findall(r"https?://v\.redd\.it/([a-zA-Z0-9]+)", text + " " + url)
                for m in matches:
                    if m not in found_reddits:
                        found_reddits[m] = {
                            "id": m,
                            "title": title,
                            "url": f"https://v.redd.it/{m}/HLSPlaylist.m3u8"
                        }
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Found {len(found_reddits)} v.redd.it clips:")
for r in found_reddits.values():
    print(f"- [r_{r['id']}]: {r['title']}")

with open("temp_harvest/dialogue_loop_real_life/reddit_candidates.json", "w", encoding="utf-8") as f:
    json.dump(list(found_reddits.values()), f, indent=2)
