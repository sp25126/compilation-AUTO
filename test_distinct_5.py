import subprocess
import os

os.makedirs("temp_harvest/love_at_first_sight_caught/5_distinct_qa", exist_ok=True)

stare_src = "temp_harvest/love_at_first_sight_caught/cand_stare4min.mp4"
london_src = "temp_harvest/love_at_first_sight_caught/cand_london_eye.mp4"

# Rank 5: Beard guy & Blonde glasses guy: cand_stare4min at 124.5s to 131.0s (6.5s)
# Rank 4: Dark hair girl & tank top girl: cand_stare4min at 118.0s to 124.5s (6.5s)
# Rank 3: Outdoor London Eye: cand_london_eye at 65.0s to 71.5s (6.5s)
# Rank 2: Denim jacket girl & blonde girl: cand_stare4min at 86.5s to 93.5s (7.0s)
# Rank 1: Blue hoodie guy & striped sweater girl Hug: cand_stare4min at 130.8s to 135.5s (4.7s slowed by 1.25x = 5.875s)

clips = [
    (5, stare_src, "00:02:04.500", "6.500", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (4, stare_src, "00:01:58.000", "6.500", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (3, london_src, "00:01:05.000", "6.500", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (2, stare_src, "00:01:26.500", "7.000", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", None),
    (1, stare_src, "00:02:10.800", "4.700", "setpts=1.25*PTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2", "atempo=0.8")
]

for rank_num, src, ss, dur, vf, af in clips:
    out_mp4 = f"temp_harvest/love_at_first_sight_caught/5_distinct_qa/rank_{rank_num}.mp4"
    cmd = [
        "ffmpeg", "-y", "-ss", ss, "-i", src, "-t", dur,
        "-vf", vf
    ]
    if af:
        cmd.extend(["-af", af])
    cmd.extend([
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", "-g", "15", "-keyint_min", "15", "-sc_threshold", "0",
        "-c:a", "aac", "-ar", "48000", "-b:a", "192k",
        out_mp4
    ])
    subprocess.run(cmd, check=True)
    
    # 2fps contact sheet
    out_sheet = f"temp_harvest/love_at_first_sight_caught/5_distinct_qa/sheet_{rank_num}_2fps.jpg"
    cmd_sheet = [
        "ffmpeg", "-y", "-i", out_mp4,
        "-vf", "fps=2,scale=260:-1,tile=6x3",
        "-frames:v", "1", "-q:v", "3",
        out_sheet
    ]
    subprocess.run(cmd_sheet, check=True)
    print(f"Generated rank {rank_num} and sheet {out_sheet}")

print("All 5 distinct test clips & sheets generated!")
