import sys, subprocess, json

query = sys.argv[1] if len(sys.argv) > 1 else "can i please get a waffle original vine"
cmd = ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch8:{query}"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
for line in res.stdout.strip().split("\n"):
    if line.strip():
        try:
            d = json.loads(line)
            print(f"{d.get('id')} | {d.get('duration')}s | {d.get('view_count')} views | {d.get('title')}")
        except:
            pass
