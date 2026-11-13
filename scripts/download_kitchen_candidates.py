import subprocess
import os

candidates = [
    ("GFJXRg7nQVY", "cand_bartender_drop"),
    ("4epIHX3g9nk", "cand_plates_slip"),
    ("q_-szbymzcw", "cand_worker_drop_food"),
    ("0E0S8IsFa1U", "cand_slippery_chef"),
    ("ebPVAEbD1ug", "cand_waitress_slip_floor"),
    ("0kPMvXMtECY", "cand_server_drop_diner"),
    ("EvpSa-d7gM0", "cand_waitress_spill_tray"),
    ("ELSnZYAMimA", "cand_cake_fail")
]

for vid, name in candidates:
    out = f"temp_harvest/commercial_kitchen_nightmares/{name}.mp4"
    if os.path.exists(out):
        print(f"Already exists: {out}")
        continue
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "-f", "bv*[height<=1080]+ba/b[height<=1080]/b",
        "--merge-output-format", "mp4",
        "-o", out,
        f"https://www.youtube.com/watch?v={vid}"
    ]
    print(f"Downloading {name} ({vid})...")
    subprocess.run(cmd)

print("Candidate downloads complete!")
