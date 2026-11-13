import subprocess
import os

candidates = [
    {"id": "xH2IuXy0XEA", "name": "marker_cap_flip"},
    {"id": "OZRsxQn8tJs", "name": "bottle_flip"},
    {"id": "Ns37ZlKw10I", "name": "pool_9ball_accidental"},
    {"id": "cdHZFu4Pntc", "name": "tyler_herro_halfcourt"},
    {"id": "2nHE-EErdWs", "name": "reporter_halfcourt"},
    {"id": "bcI9nzsCILI", "name": "sungjae_im_golf_water"},
    {"id": "c9Oe9C7-dBE", "name": "karlsson_pingpong"},
    {"id": "t1CKesTyTpI", "name": "darren_clarke_golf"}
]

out_dir = "temp_harvest/accidental_trickshots"
os.makedirs(out_dir, exist_ok=True)

for c in candidates:
    target = os.path.join(out_dir, f"{c['name']}.mp4")
    if os.path.exists(target):
        print(f"Already exists: {target}")
        continue
    print(f"Downloading {c['name']} ({c['id']})...")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best",
        "-o", target,
        f"https://www.youtube.com/watch?v={c['id']}"
    ]
    subprocess.run(cmd)

print("Download script complete!")
