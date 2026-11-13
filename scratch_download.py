import subprocess

ids = [
    "jElsBLT8G6Y",
    "0PO-Zs1nooM",
    "5xSmGNgC5kc",
    "TA_zrvBctH8",
    "Xnyfwbm3Rzg",
    "9X4ny4-l--w"
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
