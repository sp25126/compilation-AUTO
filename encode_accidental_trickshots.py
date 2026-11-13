import subprocess
import os

clips = [
    {
        "rank": 5,
        "input": "temp_harvest/accidental_trickshots/bottle_flip.mp4",
        "ss": "00:00:00.000",
        "to": "00:00:06.500",  # 6.5s = 195 frames
    },
    {
        "rank": 4,
        "input": "temp_harvest/accidental_trickshots/pool_9ball_accidental.mp4",
        "ss": "00:00:06.000",
        "to": "00:00:13.500",  # 7.5s = 225 frames
    },
    {
        "rank": 3,
        "input": "temp_harvest/accidental_trickshots/tyler_herro_halfcourt.mp4",
        "ss": "00:00:00.000",
        "to": "00:00:07.500",  # 7.5s = 225 frames
    },
    {
        "rank": 2,
        "input": "temp_harvest/accidental_trickshots/sungjae_im_golf_water.mp4",
        "ss": "00:00:03.000",
        "to": "00:00:11.000",  # 8.0s = 240 frames
    },
    {
        "rank": 1,
        "input": "temp_harvest/accidental_trickshots/karlsson_pingpong.mp4",
        "ss": "00:00:02.500",
        "to": "00:00:10.500",  # 8.0s = 240 frames
    }
]

out_dir = "public/clips/accidental_trickshots"
os.makedirs(out_dir, exist_ok=True)

for c in clips:
    rank = c["rank"]
    out_file = f"{out_dir}/rank_{rank}.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-ss", c["ss"],
        "-to", c["to"],
        "-i", c["input"],
        "-vf", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-g", "15",
        "-keyint_min", "15",
        "-sc_threshold", "0",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "48000",
        out_file
    ]
    print(f"Encoding Rank {rank} -> {out_file}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error encoding Rank {rank}: {res.stderr}")
    else:
        print(f"Rank {rank} encoded successfully!")

print("All 5 clips encoded!")
