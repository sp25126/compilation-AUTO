import subprocess
import os

candidates = [
    ("mclaurin_handshake", "9WalqnrDu08"),
    ("seacrest_blind_highfive", "TSdw4MKaxxo"),
    ("kennys_sixer_esports", "sdt3UT2w238"),
    ("trump_polish_handshake", "PD03pcjKnMw"),
    ("miley_redcarpet", "7L423aDPbko"),
    ("brady_sideline_highfive", "IHPaAuxnWLI"),
    ("longest_highfive_rejection", "Ft41g48Kp-0"),
    ("no_hand_recovery", "MmPAVRqLV1g")
]

out_dir = "temp_harvest/left_hanging_public"
os.makedirs(out_dir, exist_ok=True)

for name, vid in candidates:
    out_tmpl = os.path.join(out_dir, f"{name}_%(id)s.%(ext)s")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", out_tmpl,
        f"https://www.youtube.com/watch?v={vid}"
    ]
    print(f"Downloading {name} ({vid})...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error {name}: {res.stderr[:200]}")
    else:
        print(f"Downloaded {name} successfully.")
