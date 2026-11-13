import subprocess
import json

queries = [
    "lightning strike tree right outside window",
    "lightning strike window guy screams",
    "lightning strikes tree front yard scream",
    "close lightning strike caught on camera jump scare",
    "closest lightning strike reaction shorts"
]

seen = set()
for q in queries:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch8:{q}"
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
                print(f"{vid} | {duration}s | views: {views} | {title}")
        except Exception:
            pass
