import subprocess
import os

targets = [
    # Reddit
    ('r_i0wz6pqzak281', 'https://v.redd.it/i0wz6pqzak281/HLSPlaylist.m3u8'),
    ('r_jhetiyp7olr81', 'https://v.redd.it/jhetiyp7olr81/HLSPlaylist.m3u8'),
    ('r_kj55u7objt6d1', 'https://v.redd.it/kj55u7objt6d1/HLSPlaylist.m3u8'),
    # YouTube
    ('yt_1LmeQ3Vci_w', 'https://www.youtube.com/watch?v=1LmeQ3Vci-w'),
    ('yt_IShan26vLQ', 'https://www.youtube.com/watch?v=I-Shan26vLQ'),
    ('yt_lLxK7FEJ7o0', 'https://www.youtube.com/watch?v=lLxK7FEJ7o0'),
    ('yt_ExdD3sLBoTY', 'https://www.youtube.com/watch?v=ExdD3sLBoTY'),
    ('yt_LGdXphdEbdE', 'https://www.youtube.com/watch?v=LGdXphdEbdE'),
    ('yt_0XRZ7N05tTc', 'https://www.youtube.com/watch?v=0XRZ7N05tTc')
]

out_dir = r'temp_harvest/cocky_challengers'
os.makedirs(out_dir, exist_ok=True)

for name, url in targets:
    out_path = os.path.join(out_dir, f"{name}.mp4")
    if os.path.exists(out_path):
        print(f"Already exists: {out_path}")
        continue
    print(f"Downloading {name} from {url}...")
    cmd = [
        'py', '-3', '-m', 'yt_dlp',
        '--no-playlist',
        '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '-o', os.path.join(out_dir, f"{name}.%(ext)s"),
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Success: {name}")
    else:
        print(f"Failed {name}: {res.stderr[:200]}")
