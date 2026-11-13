import subprocess

cmd = [
    "ffmpeg", "-i", "temp_harvest/lightning_jump_scares/yt_5xSmGNgC5kc.mp4",
    "-vf", "fps=1,scale=160:-1,tile=6x5",
    "-frames:v", "1", "-q:v", "3", "-y",
    "temp_harvest/lightning_jump_scares/qa/yt_5xSmGNgC5kc_first30s.jpg"
]
subprocess.run(cmd)
