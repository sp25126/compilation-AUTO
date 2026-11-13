import subprocess
import os

clips = [
    {
        "rank": 5,
        "src": "temp_harvest/lightning_jump_scares/yt_-4bogVC22a8.mp4",
        "ss": "10.5",
        "t": "7.0",
        "out": "public/clips/lightning_jump_scares/rank_5.mp4"
    },
    {
        "rank": 4,
        "src": "temp_harvest/lightning_jump_scares/r_x0mp6xtmj38f1.mp4",
        "ss": "4.5",
        "t": "7.5",
        "out": "public/clips/lightning_jump_scares/rank_4.mp4"
    },
    {
        "rank": 3,
        "src": "temp_harvest/lightning_jump_scares/yt_P3eNzAT7zPE.mp4",
        "ss": "9.5",
        "t": "7.5",
        "out": "public/clips/lightning_jump_scares/rank_3.mp4"
    },
    {
        "rank": 2,
        "src": "temp_harvest/lightning_jump_scares/r_ynyg9kurrsa61.mp4",
        "ss": "10.5",
        "t": "7.5",
        "out": "public/clips/lightning_jump_scares/rank_2.mp4"
    },
    {
        "rank": 1,
        "src": "temp_harvest/lightning_jump_scares/yt_5xSmGNgC5kc.mp4",
        "ss": "21.0",
        "t": "7.5",
        "out": "public/clips/lightning_jump_scares/rank_1.mp4"
    }
]

os.makedirs("public/clips/lightning_jump_scares", exist_ok=True)

for c in clips:
    print(f"Encoding Rank {c['rank']}...")
    cmd = [
        "ffmpeg", "-y",
        "-ss", c["ss"],
        "-t", c["t"],
        "-i", c["src"],
        "-vf", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-g", "15",
        "-keyint_min", "15",
        "-sc_threshold", "0",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "48000",
        c["out"]
    ]
    subprocess.run(cmd, check=True)
    print(f"Rank {c['rank']} encoded successfully!")

print("All 5 clips encoded with ANTI-STUTTER protocol!")
