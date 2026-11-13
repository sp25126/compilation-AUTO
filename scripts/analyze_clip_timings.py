import subprocess
import os

clips = [
    ("cand_bartender_drop.mp4", "bartender"),
    ("cand_waitress_spill_tray.mp4", "waitress_tray"),
    ("cand_slippery_chef.mp4", "slippery_chef"),
    ("cand_worker_drop_food.mp4", "worker_food"),
    ("cand_waitress_slip_floor.mp4", "soup_vat_slip")
]

for filename, tag in clips:
    path = f"temp_harvest/commercial_kitchen_nightmares/{filename}"
    out_dir = f"temp_harvest/commercial_kitchen_nightmares/frames_{tag}"
    os.makedirs(out_dir, exist_ok=True)
    # Extract 1 frame per second with timestamp written on frame
    cmd = [
        "ffmpeg", "-y", "-i", path,
        "-vf", "fps=1,drawtext=text='%{pts\\:hms}':box=1:boxcolor=black@0.6:fontsize=36:fontcolor=white:x=20:y=20",
        f"{out_dir}/frame_%02d.jpg"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Extracted timestamped frames for {tag}")
