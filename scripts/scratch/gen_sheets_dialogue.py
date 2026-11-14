import os
import glob
import subprocess

folder = "temp_harvest/dialogue_loop_real_life"
for f in glob.glob(f"{folder}/*.mp4"):
    vid_id = os.path.splitext(os.path.basename(f))[0]
    out_sheet = f"{folder}/{vid_id}_sheet.jpg"
    cmd = [
        "ffmpeg", "-y", "-i", f,
        "-vf", "fps=2,scale=260:-1,tile=8x10",
        "-frames:v", "1", "-q:v", "3",
        out_sheet
    ]
    print(f"Generating sheet for {vid_id}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("All sheets generated.")
