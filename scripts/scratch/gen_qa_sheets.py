import glob
import os
import subprocess

files = [f for f in glob.glob("temp_harvest/battling_gravity_losing/*.*") if not f.endswith(".jpg")]
for f in files:
    base, _ = os.path.splitext(f)
    out_jpg = base + "_qa.jpg"
    cmd = [
        "ffmpeg", "-y", "-i", f,
        "-vf", "fps=2,scale=260:-1,tile=8x10",
        "-frames:v", "1", "-q:v", "3", out_jpg
    ]
    subprocess.run(cmd, capture_output=True)
    print("Done:", out_jpg)
