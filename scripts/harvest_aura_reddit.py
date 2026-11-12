import os
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMP_DIR = os.path.join(BASE_DIR, "temp_harvest", "one_million_aura_loss")
os.makedirs(TEMP_DIR, exist_ok=True)

CANDIDATES = [
    ("2jxak26tezo51", "left_hanging_recovery"),
    ("yg40kfivkzx51", "ultimate_failed_handshake"),
    ("kctf7jav87a21", "trying_to_look_cool_price"),
    ("extneulhlgq81", "wcgw_trying_to_look_cool"),
    ("rgiq4ecrvqu11", "hmb_impress_woman"),
    ("733sifcy6q311", "hmb_impress_pool"),
    ("lmumlsvaooi11", "trying_to_be_cool_water"),
    ("5qw7vpamtp751", "trying_to_look_cool_sunglasses"),
    ("zl14729zayze1", "wanting_to_look_cool"),
    ("1hacdjfc7r251", "trying_to_look_cool_work"),
]

def download_and_sheet():
    for vid, tag in CANDIDATES:
        out_mp4 = os.path.join(TEMP_DIR, f"aura_{tag}_{vid}.mp4")
        sheet_jpg = os.path.join(TEMP_DIR, f"sheet_aura_{tag}_{vid}.jpg")
        hls_url = f"https://v.redd.it/{vid}/HLSPlaylist.m3u8"
        print(f"Downloading {tag} ({vid})...")
        proc = subprocess.run(
            [
                "py", "-3", "-m", "yt_dlp", "--js-runtimes", "node",
                "-o", out_mp4,
                hls_url
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=40,
        )
        if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 100000:
            print(f"  Downloaded: {out_mp4} ({os.path.getsize(out_mp4):,} bytes)")
            # Generate 2fps sheet
            subprocess.run(
                [
                    "ffmpeg", "-y", "-i", out_mp4,
                    "-vf", "fps=2,scale=260:-1,tile=8x8",
                    "-frames:v", "1", "-q:v", "3",
                    sheet_jpg
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print(f"  Generated sheet: {sheet_jpg}")
        else:
            print(f"  Failed or too small: {vid}")

if __name__ == "__main__":
    download_and_sheet()
