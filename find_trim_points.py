import subprocess
import json

clips_info = [
    ("rank_5", "temp_harvest/lightning_jump_scares/yt_-4bogVC22a8.mp4"),
    ("rank_4", "temp_harvest/lightning_jump_scares/r_x0mp6xtmj38f1.mp4"),
    ("rank_3", "temp_harvest/lightning_jump_scares/yt_P3eNzAT7zPE.mp4"),
    ("rank_2", "temp_harvest/lightning_jump_scares/r_ynyg9kurrsa61.mp4"),
    ("rank_1", "temp_harvest/lightning_jump_scares/yt_5xSmGNgC5kc.mp4")
]

for name, path in clips_info:
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", path]
    dur = float(subprocess.check_output(cmd, text=True).strip())
    print(f"{name}: {path} total duration = {dur:.2f}s")
