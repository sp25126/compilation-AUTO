import subprocess
import json

queries = [
    "lightning strike window scream shorts",
    "lightning strikes tree scream shorts",
    "lightning strikes porch reaction shorts",
    "lightning strike close call scream shorts",
    "closest lightning strike caught on camera shorts",
    "lightning strikes right next to me shorts",
    "insane lightning jump scare shorts",
    "lightning strike boat scream shorts",
    "lightning strike pool scream shorts"
]

candidates = []
seen = set()

for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch10:{q}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            vid = d.get("id")
            if vid in seen:
                continue
            seen.add(vid)
            duration = d.get("duration") or 0
            views = d.get("view_count") or 0
            title = d.get("title") or ""
            # Filter for short videos 5s to 35s
            if 5 <= duration <= 35:
                candidates.append({
                    "id": vid,
                    "duration": duration,
                    "views": views,
                    "title": title,
                    "query": q
                })
        except Exception:
            pass

candidates.sort(key=lambda x: x["views"], reverse=True)
print(f"Total candidates found: {len(candidates)}")
for c in candidates[:25]:
    print(f"{c['id']} | {c['duration']}s | views: {c['views']} | {c['title']}")
