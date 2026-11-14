import sys
import subprocess
import json

query = sys.argv[1] if len(sys.argv) > 1 else "ice slip balance fail shorts"
cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch15:{query}"]
proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
for line in proc.stdout.splitlines():
    if not line.strip():
        continue
    try:
        data = json.loads(line)
        duration = data.get("duration") or 0
        views = data.get("view_count") or 0
        vid_id = data.get("id")
        title = data.get("title")
        print(f"{vid_id} | dur:{duration}s | views:{views} | {title}")
    except Exception as e:
        pass
