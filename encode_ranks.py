import subprocess
import os

src = "temp_harvest/love_at_first_sight_caught/cand_stare4min.mp4"
os.makedirs("public/clips/love_at_first_sight_caught", exist_ok=True)

ranks = [
    (5, "00:01:08.000", "7.000", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (4, "00:01:26.000", "7.500", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (3, "00:01:15.250", "6.500", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (2, "00:00:58.000", "7.000", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (1, "00:02:11.000", "4.500", "setpts=1.25*PTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", "atempo=0.8"),
]

for rank_num, start, dur, vf, af in ranks:
    dst = f"public/clips/love_at_first_sight_caught/rank_{rank_num}.mp4"
    cmd = [
        "ffmpeg", "-y", "-ss", start, "-i", src, "-t", dur,
        "-vf", vf
    ]
    if af:
        cmd.extend(["-af", af])
    cmd.extend([
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", "-g", "15", "-keyint_min", "15", "-sc_threshold", "0",
        "-c:a", "aac", "-ar", "48000", "-b:a", "192k",
        dst
    ])
    print(f"Encoding rank {rank_num}...")
    subprocess.run(cmd, check=True)

print("All 5 clips encoded successfully!")
