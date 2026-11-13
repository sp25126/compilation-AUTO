import subprocess

# We will sample frames every 1 second between 60s and 130s to find the best shots for Pair B and Pair C
src = "temp_harvest/love_at_first_sight_caught/cand_stare4min.mp4"

# Let's extract frames at specific times:
times = [
    (15, 25), # Early
    (45, 58), # Mid 1
    (75, 110), # Mid 2
    (115, 130) # Finales
]

import os
os.makedirs("temp_harvest/love_at_first_sight_caught/pairs_scan", exist_ok=True)

# Generate contact sheet between 10s and 135s at 1 fps
cmd = [
    "ffmpeg", "-y", "-ss", "00:00:10", "-i", src, "-t", "125",
    "-vf", "fps=1,scale=240:-1,tile=10x13",
    "-frames:v", "1", "-q:v", "3",
    "temp_harvest/love_at_first_sight_caught/pairs_scan/full_1fps_scan.jpg"
]
subprocess.run(cmd, check=True)
print("Generated full 1fps scan sheet!")
