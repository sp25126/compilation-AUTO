import subprocess
import glob
import os

files = glob.glob("temp_harvest/commercial_kitchen_nightmares/cand_*.mp4")
for f in files:
    base = os.path.splitext(f)[0]
    sheet = f"{base}_sheet.jpg"
    if os.path.exists(sheet):
        continue
    cmd = [
        "ffmpeg", "-y", "-i", f,
        "-vf", "fps=2,scale=260:-1,tile=8x8",
        "-frames:v", "1", "-q:v", "3",
        sheet
    ]
    print(f"Generating sheet for {f} -> {sheet}")
    subprocess.run(cmd)

print("All candidate contact sheets generated!")
