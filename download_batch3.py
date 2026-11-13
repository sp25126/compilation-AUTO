import subprocess
import os

candidates = [
    ("snoop_smooth_recovery", "6kENMh2qhZ8"),
    ("corbyn_highfive_fail", "aJ0AeArx52g"),
    ("kobe_phil_hanging", "2CBVPTgyZjA"),
    ("chess_handshake_fail", "yh_pieNaNkQ")
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
