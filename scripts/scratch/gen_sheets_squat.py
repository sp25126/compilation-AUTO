import subprocess, glob, os

files = glob.glob("temp_harvest/squat_rack_blunders/*.mp4")
print(f"Generating sheets for {len(files)} files...")

for f in files:
    base = os.path.splitext(os.path.basename(f))[0]
    out_sheet = f"temp_harvest/squat_rack_blunders/{base}_sheet.jpg"
    cmd = [
        "ffmpeg", "-y", "-i", f,
        "-vf", "fps=2,scale=260:-1,tile=8x10",
        "-frames:v", "1", "-q:v", "3",
        out_sheet
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Done sheet for {base}")

print("All sheets generated.")
