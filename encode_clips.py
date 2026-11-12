import subprocess
import os

clips = [
    {
        "rank": 5,
        "input": "temp_harvest/vehicle_360_recoveries/yt_p3gGMSokWAE.webm",
        "ss": "00:00:03.500",
        "to": "00:00:11.500", # 8.0s
    },
    {
        "rank": 4,
        "input": "temp_harvest/vehicle_360_recoveries/r_wz2q9isjtcqh1.mp4",
        "ss": "00:00:07.500",
        "to": "00:00:14.500", # 7.0s
    },
    {
        "rank": 3,
        "input": "temp_harvest/vehicle_360_recoveries/r_2iwsonmcmide1.mp4",
        "ss": "00:00:08.000",
        "to": "00:00:15.500", # 7.5s
    },
    {
        "rank": 2,
        "input": "temp_harvest/vehicle_360_recoveries/yt_dGu12hNq4DY.mkv",
        "ss": "00:00:10.000",
        "to": "00:00:17.500", # 7.5s
    },
    {
        "rank": 1,
        "input": "temp_harvest/vehicle_360_recoveries/yt_Xz1fjovL4uc.webm",
        "ss": "00:00:00.500",
        "to": "00:00:07.500", # 7.0s
    }
]

out_dir = "public/clips/vehicle_360_recoveries"
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
