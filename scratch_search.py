import subprocess
import json

queries = [
    "lightning strike window jump scare",
    "lightning strike porch close scream",
    "lightning strike tree close reaction",
    "closest lightning strike caught on camera",
    "lightning strikes right in front of camera shock",
    "lightning strike car windshield scream"
]

results = []
for q in queries:
    cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch8:{q}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            duration = d.get("duration") or 0
            views = d.get("view_count") or 0
            title = d.get("title")
            vid = d.get("id")
            if 5 <= duration <= 45:
                results.append({"id": vid, "duration": duration, "views": views, "title": title, "query": q})
        except Exception:
            pass

seen = set()
for r in results:
    if r["id"] not in seen:
        seen.add(r["id"])
        print(f"{r['id']} | {r['duration']}s | views: {r['views']} | {r['title']}")
