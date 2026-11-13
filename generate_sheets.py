import subprocess
import glob
import os

files = glob.glob("temp_harvest/left_hanging_public/*.mp4")
for f in files:
    sheet_name = f.replace(".mp4", "_2fps.jpg")
    cmd = [
        "ffmpeg", "-y", "-i", f,
        "-vf", "fps=2,scale=260:-1,tile=8x6",
        "-frames:v", "1", "-q:v", "3", sheet_name
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Generated sheet: {sheet_name}")
