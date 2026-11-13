import subprocess

# Let's inspect seconds 20 to 32 of yt_5xSmGNgC5kc
cmd = [
    "ffmpeg", "-i", "temp_harvest/lightning_jump_scares/yt_5xSmGNgC5kc.mp4",
    "-ss", "20", "-t", "12",
    "-af", "volumedetect",
    "-f", "null", "-"
]
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stderr[-500:])
