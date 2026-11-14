import subprocess
import os

candidates = [
    # Reddit
    ("r_3qykyk9a03nf1", "https://v.redd.it/3qykyk9a03nf1/HLSPlaylist.m3u8"),
    ("r_riwg8w503lq81", "https://v.redd.it/riwg8w503lq81/HLSPlaylist.m3u8"),
    ("r_sqpznu8v6va81", "https://v.redd.it/sqpznu8v6va81/HLSPlaylist.m3u8"),
    ("r_b57an0ytnf261", "https://v.redd.it/b57an0ytnf261/HLSPlaylist.m3u8"),
    ("r_0lp3e3c7frve1", "https://v.redd.it/0lp3e3c7frve1/HLSPlaylist.m3u8"),
    ("r_vtywz6o5xie81", "https://v.redd.it/vtywz6o5xie81/HLSPlaylist.m3u8"),
    ("r_wwc67ducopq71", "https://v.redd.it/wwc67ducopq71/HLSPlaylist.m3u8"),
    ("r_kjpije2kre991", "https://v.redd.it/kjpije2kre991/HLSPlaylist.m3u8"),
    # YouTube
    ("yt_1oI3unCfkBg", "https://www.youtube.com/watch?v=1oI3unCfkBg"),
    ("yt_rqrsecCrC_Q", "https://www.youtube.com/watch?v=rqrsecCrC_Q")
]

out_dir = "temp_harvest/dialogue_loop_real_life"

for cid, url in candidates:
    target = f"{out_dir}/{cid}.mp4"
    if not os.path.exists(target):
        print(f"Downloading {cid}...")
        cmd = [
            "py", "-3", "-m", "yt_dlp",
            "-o", target,
            url
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Finished downloads.")
