import subprocess

cmd1 = [
    "ffmpeg", "-y", "-ss", "12", "-t", "16", "-i", "temp_harvest/left_hanging_public/longest_highfive_rejection_Ft41g48Kp-0.mp4",
    "-vf", "fps=1,scale=320:-1", "-q:v", "2", "temp_harvest/left_hanging_public/arcade_%02d.jpg"
]
subprocess.run(cmd1)

cmd2 = [
    "ffmpeg", "-y", "-ss", "6", "-t", "15", "-i", "temp_harvest/left_hanging_public/kobe_phil_hanging_2CBVPTgyZjA.mp4",
    "-vf", "fps=1,scale=320:-1", "-q:v", "2", "temp_harvest/left_hanging_public/kobe_%02d.jpg"
]
subprocess.run(cmd2)

cmd_tile1 = ["ffmpeg", "-y", "-i", "temp_harvest/left_hanging_public/arcade_%02d.jpg", "-vf", "tile=4x4", "temp_harvest/left_hanging_public/sheet_arcade.jpg"]
subprocess.run(cmd_tile1)

cmd_tile2 = ["ffmpeg", "-y", "-i", "temp_harvest/left_hanging_public/kobe_%02d.jpg", "-vf", "tile=5x3", "temp_harvest/left_hanging_public/sheet_kobe.jpg"]
subprocess.run(cmd_tile2)

print("Arcade & Kobe sheets ready.")
