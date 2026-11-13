import subprocess
import json

queries = [
    "lightning strike window loud scream",
    "lightning strikes tree window jump scare",
    "close lightning strike window reaction",
    "lightning strike porch scream viral",
    "lightning strikes backyard patio jump scare",
    "lightning strike car window reaction",
    "lightning hit tree outside window scream"
]

results = []
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
        if not line: continue
        try:
            d = json.loads(line)
            vid = d.get("id")
            if vid in seen: continue
            seen.add(vid)
            duration = d.get("duration") or 0
            views = d.get("view_count") or 0
            title = d.get("title") or ""
            if 5 <= duration <= 35:
                results.append((views, vid, duration, title))
        except Exception:
            pass

results.sort(reverse=True)
for v, vid, dur, title in results[:30]:
    print(f"{vid} | {dur}s | views: {v} | {title}")
