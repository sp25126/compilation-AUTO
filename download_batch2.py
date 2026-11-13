import subprocess

ids = [
    "9U0mChmrU6M",
    "Qd5Sx--iJpo",
    "gWgKSGVPLJE",
    "lZpxPASuBoQ",
    "pNumTPhxjK0",
    "sDI3x6Fp_Dk"
]

for vid in ids:
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", f"temp_harvest/lightning_jump_scares/yt_{vid}.%(ext)s",
        f"https://www.youtube.com/watch?v={vid}"
    ]
    print(f"Downloading {vid}...")
    subprocess.run(cmd)
