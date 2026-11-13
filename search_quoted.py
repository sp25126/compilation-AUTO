import subprocess
import json

queries = [
    'lightning strike window "scream"',
    'lightning strike balcony "scream"',
    'lightning strike "porch" "scared"',
    'lightning strike "patio" "scream"',
    'lightning strike tree "scared" "reaction"',
    'lightning strike "car" "jump scare"'
]

candidates = []
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
                candidates.append((views, vid, duration, title))
        except Exception:
            pass

candidates.sort(reverse=True)
for v, vid, dur, title in candidates[:25]:
    print(f"{vid} | {dur}s | views: {v} | {title}")
