import os
import subprocess

SFX_MAP = {
    "cartoon_slip.mp3": "https://www.youtube.com/watch?v=R9j0_D2D_eE", # Cartoon slip whistle/boing
    "fail_buzzer.mp3": "https://www.youtube.com/watch?v=1ytCEuuW2_A",  # The Price is Right fail horn / buzzer
    "thud_whack.mp3": "https://www.youtube.com/watch?v=r_7bDoT-y4M",   # Punch / thud impact
    "record_scratch.mp3": "https://www.youtube.com/watch?v=hKQUkg_Xyis", # Record scratch freeze
    "glass_shatter.mp3": "https://www.youtube.com/watch?v=hZ16KqT9wKg", # Glass window shatter
    "siren_short.mp3": "https://www.youtube.com/watch?v=b4d8G1b04jY"    # Police wail chirp
}

out_dir = "public/audio/stems"
os.makedirs(out_dir, exist_ok=True)
python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

for filename, url in SFX_MAP.items():
    dest = os.path.join(out_dir, filename)
    if os.path.exists(dest):
        continue
    print(f"Downloading {filename}...")
    temp_target = os.path.join(out_dir, f"temp_{filename.replace('.mp3', '')}")
    cmd = [
        python_exe, "-m", "yt_dlp",
        "-x", "--audio-format", "mp3",
        "-o", f"{temp_target}.%(ext)s",
        url
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Trim to 2.5s maximum
    downloaded = f"{temp_target}.mp3"
    if os.path.exists(downloaded):
        trim_cmd = [
            "ffmpeg", "-t", "00:00:02.500", "-i", downloaded,
            "-c:a", "libmp3lame", "-b:a", "192k", dest, "-y"
        ]
        subprocess.run(trim_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(downloaded):
            os.remove(downloaded)
        print(f"Ready: {dest}")

print("All audio stems prepared!")
