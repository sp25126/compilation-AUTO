import subprocess

src = "temp_harvest/love_at_first_sight_caught/cand_london_eye.mp4"

# Generate 1fps contact sheet for cand_london_eye
cmd = [
    "ffmpeg", "-y", "-ss", "00:00:15", "-i", src, "-t", "85",
    "-vf", "fps=1,scale=240:-1,tile=10x9",
    "-frames:v", "1", "-q:v", "3",
    "temp_harvest/love_at_first_sight_caught/pairs_scan/london_1fps_scan.jpg"
]
subprocess.run(cmd, check=True)
print("Generated london 1fps scan sheet!")
