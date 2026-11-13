import subprocess

cmd = [
    "ffmpeg", "-y", "-ss", "0", "-t", "10", "-i", "temp_harvest/left_hanging_public/kobe_phil_hanging_2CBVPTgyZjA.mp4",
    "-vf", "fps=1,scale=320:-1", "-q:v", "2", "temp_harvest/left_hanging_public/kobe_early_%02d.jpg"
]
subprocess.run(cmd)

cmd_tile = ["ffmpeg", "-y", "-i", "temp_harvest/left_hanging_public/kobe_early_%02d.jpg", "-vf", "tile=5x2", "temp_harvest/left_hanging_public/sheet_kobe_early.jpg"]
subprocess.run(cmd_tile)
