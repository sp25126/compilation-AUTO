import subprocess
import json

queries = [
    "squat fail funny shorts",
    "squat drop bar shorts",
    "squat fail shorts",
    "squat bail safeties shorts",
    "gym squat rack fail shorts"
]
vids = []
seen = set()
for q in queries:
    cmd = ['py', '-3', '-m', 'yt_dlp', '--flat-playlist', '--dump-json', f'ytsearch20:{q}']
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    for line in res.stdout.strip().split('\n'):
        if not line:
            continue
        try:
            d = json.loads(line)
            dur = d.get('duration') or 0
            vid = d.get('id')
            if 6 <= dur <= 35 and vid not in seen:
                seen.add(vid)
                vids.append({'id': vid, 'title': d.get('title',''), 'dur': dur})
        except:
            pass

print(f"Total unique found: {len(vids)}")
with open("temp_harvest/squat_rack_blunders/search_results.json", "w", encoding="utf-8") as f:
    json.dump(vids, f, indent=2)

for v in vids[:30]:
    print(f"{v['id']} | {v['dur']}s | {v['title']}")
