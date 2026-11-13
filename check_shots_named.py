import subprocess
import os

src = "temp_harvest/love_at_first_sight_caught/cand_stare4min.mp4"
os.makedirs("temp_harvest/love_at_first_sight_caught/shots_named", exist_ok=True)

shots_to_check = [
    (25, 49.0, 53.0),
    (26, 53.0, 58.0),
    (27, 58.0, 65.0),
    (28, 65.0, 68.0),
    (29, 68.0, 75.25),
    (30, 75.25, 81.75),
    (31, 81.75, 86.0),
    (32, 86.0, 94.75),
    (40, 99.75, 104.25),
    (43, 109.25, 115.0)
]

for idx, start, end in shots_to_check:
    mid = (start + end) / 2.0
    dur = end - start
    out_file = f"temp_harvest/love_at_first_sight_caught/shots_named/shot_{idx}_{dur:.1f}s.jpg"
    cmd = [
        "ffmpeg", "-y", "-ss", str(mid), "-i", src,
        "-vframes", "1", "-q:v", "3", out_file
    ]
    subprocess.run(cmd, check=True)
    print(f"Shot {idx}: {start}s - {end}s ({dur:.2f}s) -> {out_file}")
