import subprocess
import glob
import os

os.makedirs("temp_harvest/love_at_first_sight_caught/qa_contact", exist_ok=True)
for rank in range(1, 6):
    clip = f"public/clips/love_at_first_sight_caught/rank_{rank}.mp4"
    out_sheet = f"temp_harvest/love_at_first_sight_caught/qa_contact/rank_{rank}_2fps.jpg"
    cmd = [
        "ffmpeg", "-y", "-i", clip,
        "-vf", "fps=2,scale=260:-1,tile=6x4",
        "-frames:v", "1", "-q:v", "3",
        out_sheet
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated {out_sheet}")
