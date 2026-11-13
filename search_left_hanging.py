import subprocess
import json

queries = [
    'left hanging handshake short',
    'left hanging high five short',
    'left hanging fist bump cringe short',
    'left hanging awkward handshake news short',
    'left hanging celebrity short',
    'left hanging athlete high five short',
    'left hanging handshake recovery short',
    'awkward high five fail short',
    'left hanging sports short',
    'left hanging on live tv short'
]

results = []
for q in queries:
    cmd = ['py', '-3', '-m', 'yt_dlp', '--flat-playlist', '--dump-json', f'ytsearch8:{q}']
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
                if 5 <= dur <= 60 and id_:
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
for u in unique[:50]:
    print(f"{u['id']} | dur:{u['duration']}s | views:{u['views']} | {u['title']}")
