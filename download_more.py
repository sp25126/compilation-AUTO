import subprocess
import os

candidates = [
    ("cameron_handshake", "fd-WifC_JYo"),
    ("mazzulla_foster_handshake", "aXX_Tn4gFbs"),
    ("reporter_handshake", "oOzLujqFSzw")
]

out_dir = "temp_harvest/left_hanging_public"
for name, vid in candidates:
    out_tmpl = os.path.join(out_dir, f"{name}_%(id)s.%(ext)s")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", out_tmpl,
        f"https://www.youtube.com/watch?v={vid}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Downloaded {name}")
