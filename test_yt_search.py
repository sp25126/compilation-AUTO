import subprocess
import json

cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", "ytsearch10:luckiest trickshot shorts"]
p = subprocess.run(cmd, capture_output=True, text=True)
for line in p.stdout.splitlines():
    if not line.strip():
        continue
    try:
        d = json.loads(line)
        print(f"[{d.get('id')}] ({d.get('duration')}s, {d.get('view_count')} views): {d.get('title')}")
    except:
        pass
