import subprocess
import glob
import os

files = [
    "temp_harvest/accidental_trickshots/marker_cap_flip.mp4",
    "temp_harvest/accidental_trickshots/bottle_flip.mp4",
    "temp_harvest/accidental_trickshots/pool_9ball_accidental.mp4",
    "temp_harvest/accidental_trickshots/tyler_herro_halfcourt.mp4",
    "temp_harvest/accidental_trickshots/reporter_halfcourt.mp4",
    "temp_harvest/accidental_trickshots/sungjae_im_golf_water.mp4",
    "temp_harvest/accidental_trickshots/karlsson_pingpong.mp4",
    "temp_harvest/accidental_trickshots/darren_clarke_golf.mp4"
]

for f in files:
    base = os.path.splitext(f)[0]
    sheet = f"{base}_2fps_sheet.jpg"
    cmd = [
        "ffmpeg", "-y", "-i", f,
        "-vf", "fps=2,scale=260:-1,tile=6x6",
        "-frames:v", "1", "-q:v", "3", sheet
    ]
    print(f"Generating sheet: {sheet}")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Contact sheets generated!")
