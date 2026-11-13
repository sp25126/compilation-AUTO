import subprocess
import json

queries = [
    'josh hart high five fail',
    'awkward news anchor handshake',
    'reporter left hanging handshake',
    'david cameron handshake denied',
    'coach left hanging handshake'
]

results = []
for q in queries:
    cmd = ['py', '-3', '-m', 'yt_dlp', '--flat-playlist', '--dump-json', f'ytsearch5:{q}']
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, check=True)
        for line in p.stdout.splitlines():
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                dur = data.get('duration') or 0
                views = data.get('view_count') or 0
                id_ = data.get('id')
                title = data.get('title', '')
                if 5 <= dur <= 50 and id_:
                    results.append({'id': id_, 'title': title, 'duration': dur, 'views': views, 'url': f'https://www.youtube.com/watch?v={id_}'})
            except Exception:
                pass
    except Exception as e:
        print(f"Error querying {q}: {e}")

seen = set()
unique = []
for r in results:
    if r['id'] not in seen:
        seen.add(r['id'])
        unique.append(r)

print(f"Total candidates: {len(unique)}")
for u in unique:
    print(f"{u['id']} | dur:{u['duration']}s | views:{u['views']} | {u['title']}")
