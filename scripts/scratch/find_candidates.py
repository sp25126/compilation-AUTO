import subprocess
import json

queries = [
    "squat rack fail gym shorts",
    "squat bail safeties funny shorts",
    "squat fail dumps bar shorts",
    "gym squat fail funny reaction shorts",
    "squat rack bail fail shorts"
]

results = []
for q in queries:
    cmd = ['py', '-3', '-m', 'yt_dlp', '--flat-playlist', '--dump-json', f'ytsearch12:{q}']
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    for line in res.stdout.strip().split('\n'):
        if not line:
            continue
        try:
            d = json.loads(line)
            dur = d.get('duration') or 0
            views = d.get('view_count') or 0
            title = d.get('title') or ''
            vid = d.get('id')
            if 5 <= dur <= 40:
                results.append({'id': vid, 'title': title, 'duration': dur, 'views': views, 'url': f'https://www.youtube.com/watch?v={vid}'})
        except Exception:
            pass

seen = set()
unique = []
for r in results:
    if r['id'] not in seen:
        seen.add(r['id'])
        unique.append(r)

print(f"Total candidates: {len(unique)}")
with open("temp_harvest/squat_rack_blunders/candidates.json", "w", encoding="utf-8") as f:
    json.dump(unique, f, indent=2)

for u in unique[:15]:
    print(f"{u['id']} | {u['duration']}s | views: {u['views']} | {u['title']}")
