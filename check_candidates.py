import subprocess

videos = [
    "cand_stare4min.mp4",
    "cand_stranger_eye.mp4",
    "cand_london_eye.mp4",
    "cand_eye_experiment.mp4"
]

for v in videos:
    path = f"temp_harvest/love_at_first_sight_caught/{v}"
    out_sheet = f"temp_harvest/love_at_first_sight_caught/overview_{v}.jpg"
    cmd = [
        "ffmpeg", "-y", "-i", path,
        "-vf", "fps=1/5,scale=320:-1,tile=6x6",
        "-frames:v", "1", "-q:v", "3",
        out_sheet
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Generated overview for {v}")
