import subprocess
import sys

tasks = [
    ("r_8iwjbc0oyqhe1.mp4", "https://v.redd.it/8iwjbc0oyqhe1/HLSPlaylist.m3u8"),
    ("r_e88u66q7mnw81.mp4", "https://v.redd.it/e88u66q7mnw81/HLSPlaylist.m3u8"),
    ("r_sh11v8yjgw4f1.mp4", "https://v.redd.it/sh11v8yjgw4f1/HLSPlaylist.m3u8"),
    ("KDt-9EgvgQM.mp4", "https://www.youtube.com/watch?v=KDt-9EgvgQM"),
    ("MkEJJ4VWWy8.mp4", "https://www.youtube.com/watch?v=MkEJJ4VWWy8"),
    ("71PD2f1ogyk.mp4", "https://www.youtube.com/watch?v=71PD2f1ogyk"),
    ("GVlfzt0J894.mp4", "https://www.youtube.com/watch?v=GVlfzt0J894"),
    ("YE8PTMSFMUg.mp4", "https://www.youtube.com/watch?v=YE8PTMSFMUg"),
    ("A29yy8ntEIc.mp4", "https://www.youtube.com/watch?v=A29yy8ntEIc"),
    ("szt2kWJ8IVA.mp4", "https://www.youtube.com/watch?v=szt2kWJ8IVA"),
    ("FTDYPCCPGS0.mp4", "https://www.youtube.com/watch?v=FTDYPCCPGS0"),
    ("uxtyc1dSZjg.mp4", "https://www.youtube.com/watch?v=uxtyc1dSZjg")
]

for out_name, url in tasks:
    out_path = f"temp_harvest/animals_becoming_scarier/{out_name}"
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", out_path,
        url
    ]
    print(f"Downloading {out_name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Success: {out_name}")
    else:
        print(f"Failed {out_name}: {res.stderr[:200]}")
