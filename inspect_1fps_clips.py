import subprocess

# Let's inspect audio and video timestamps of r_x0mp6xtmj38f1
# Check scene luminance per second
cmd = [
    "ffmpeg", "-i", "temp_harvest/lightning_jump_scares/r_x0mp6xtmj38f1.mp4",
    "-vf", "fps=1,scale=160:-1,tile=6x2",
    "-frames:v", "1", "-q:v", "3", "-y",
    "temp_harvest/lightning_jump_scares/qa/r_x0mp6xtmj38f1_1fps.jpg"
]
subprocess.run(cmd)

cmd5 = [
    "ffmpeg", "-i", "temp_harvest/lightning_jump_scares/yt_-4bogVC22a8.mp4",
    "-vf", "fps=1,scale=160:-1,tile=6x3",
    "-frames:v", "1", "-q:v", "3", "-y",
    "temp_harvest/lightning_jump_scares/qa/yt_-4bogVC22a8_1fps.jpg"
]
subprocess.run(cmd5)
