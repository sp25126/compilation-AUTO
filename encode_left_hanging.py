import subprocess
import os

clips = [
    {
        "rank": 5,
        "raw": "temp_harvest/left_hanging_public/longest_highfive_rejection_Ft41g48Kp-0.mp4",
        "ss": "13.5",
        "t": "6.5"
    },
    {
        "rank": 4,
        "raw": "temp_harvest/left_hanging_public/mclaurin_handshake_9WalqnrDu08.mp4",
        "ss": "2.5",
        "t": "6.0"
    },
    {
        "rank": 3,
        "raw": "temp_harvest/left_hanging_public/kobe_phil_hanging_2CBVPTgyZjA.mp4",
        "ss": "14.5",
        "t": "6.5"
    },
    {
        "rank": 2,
        "raw": "temp_harvest/left_hanging_public/trump_polish_handshake_PD03pcjKnMw.mp4",
        "ss": "8.0",
        "t": "6.5"
    },
    {
        "rank": 1,
        "raw": "temp_harvest/left_hanging_public/seacrest_blind_highfive_TSdw4MKaxxo.mp4",
        "ss": "17.5",
        "t": "7.0"
    }
]

out_dir = "public/clips/left_hanging_public"
os.makedirs(out_dir, exist_ok=True)

for c in clips:
    out_path = os.path.join(out_dir, f"rank_{c['rank']}.mp4")
    cmd = [
        "ffmpeg", "-y",
        "-ss", c["ss"],
        "-t", c["t"],
        "-i", c["raw"],
        "-vf", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-g", "15",
        "-keyint_min", "15",
        "-sc_threshold", "0",
        "-c:a", "aac",
        "-ar", "48000",
        "-b:a", "192k",
        out_path
    ]
    print(f"Encoding rank_{c['rank']}...")
    subprocess.run(cmd, check=True)
    print(f"Done: {out_path}")

print("All 5 clips encoded with anti-stutter specification.")
