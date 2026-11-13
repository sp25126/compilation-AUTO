import subprocess
import os

src = "temp_harvest/love_at_first_sight_caught/cand_stare4min.mp4"
os.makedirs("public/clips/love_at_first_sight_caught", exist_ok=True)
os.makedirs("temp_harvest/love_at_first_sight_caught/final_5_qa", exist_ok=True)

# 5-Rank Benchmark Specification:
# Rank 5: Shot 31 (81.75s to 86.00s = 4.25s) slowed 1.30x -> 5.525s (166 frames)
# Rank 4: Shot 26 (53.00s to 58.00s = 5.00s) slowed 1.15x -> 5.750s (173 frames)
# Rank 3: Shot 29 (68.00s to 75.00s = 7.00s) 1.0x -> 7.000s (210 frames)
# Rank 2: Shot 27 (58.00s to 65.00s = 7.00s) 1.0x -> 7.000s (210 frames)
# Rank 1: Shot 62+63 (130.80s to 135.50s = 4.70s) slowed 1.25x -> 5.875s (176 frames)

ranks = [
    (5, "00:01:21.750", "4.250", "setpts=1.30*PTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", "atempo=0.769"),
    (4, "00:00:53.000", "5.000", "setpts=1.15*PTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", "atempo=0.869"),
    (3, "00:01:08.000", "7.000", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (2, "00:00:58.000", "7.000", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (1, "00:02:10.800", "4.700", "setpts=1.25*PTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", "atempo=0.800"),
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

    # Generate 2fps contact sheet
    sheet = f"temp_harvest/love_at_first_sight_caught/final_5_qa/sheet_rank_{rank_num}_2fps.jpg"
    cmd_sheet = [
        "ffmpeg", "-y", "-i", dst,
        "-vf", "fps=2,scale=260:-1,tile=6x3",
        "-frames:v", "1", "-q:v", "3",
        sheet
    ]
    subprocess.run(cmd_sheet, check=True)
    print(f"Generated QA sheet: {sheet}")

print("All 5 final ranks encoded and sheets generated successfully!")
