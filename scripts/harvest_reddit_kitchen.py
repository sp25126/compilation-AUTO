import urllib.request
import json
import subprocess
import os

subreddits = [
    "KitchenConfidential",
    "IdiotsInKitchens",
    "AbruptChaos",
    "Wellthatsucks",
    "WatchPeopleDieInside"
]

queries = [
    "kitchen spill",
    "pot of beans",
    "kitchen slip",
    "spilled sauce",
    "dropped soup",
    "dishwasher slip"
]

found = []
seen = set()

for sub in subreddits:
    for q in queries:
        url = f"https://www.reddit.com/r/{sub}/search.json?q={urllib.parse.quote(q)}&restrict_sr=1&limit=15&sort=top"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                children = data.get("data", {}).get("children", [])
                for child in children:
                    p = child.get("data", {})
                    is_vid = p.get("is_video", False)
                    post_url = p.get("url", "")
                    title = p.get("title", "")
                    pid = p.get("id")
                    if pid in seen:
                        continue
                    if is_vid or "v.redd.it" in post_url:
                        seen.add(pid)
                        found.append({
                            "sub": sub,
                            "id": pid,
                            "title": title,
                            "url": post_url,
                            "permalink": "https://reddit.com" + p.get("permalink", "")
                        })
        except Exception as e:
            # print(f"Error {sub} {q}: {e}")
            pass

print(f"Total video posts found from Reddit: {len(found)}")
for f in found[:20]:
    print(f"[{f['sub']}] {f['title']} -> {f['url']}")

with open("temp_harvest/commercial_kitchen_nightmares/reddit_candidates.json", "w", encoding="utf-8") as out:
    json.dump(found, out, indent=2)
