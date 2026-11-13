import subprocess
import re

clips = [
    ("rank_5", "temp_harvest/lightning_jump_scares/yt_-4bogVC22a8.mp4"),
    ("rank_4", "temp_harvest/lightning_jump_scares/r_x0mp6xtmj38f1.mp4"),
    ("rank_3", "temp_harvest/lightning_jump_scares/yt_P3eNzAT7zPE.mp4"),
    ("rank_2", "temp_harvest/lightning_jump_scares/r_ynyg9kurrsa61.mp4"),
    ("rank_1", "temp_harvest/lightning_jump_scares/yt_5xSmGNgC5kc.mp4")
]

for name, path in clips:
    # Use signalstats to find the frame with max Y (luminance) or highest brightness
    cmd = [
        "ffmpeg", "-i", path,
        "-vf", "signalstats,metadata=print:key=lavfi.signalstats.YAVG",
        "-f", "null", "-"
    ]
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, text=True, errors="ignore")
    max_y = 0.0
    max_pts = 0.0
    pts_pattern = re.compile(r"pts_time:([0-9.]+)")
    y_pattern = re.compile(r"lavfi.signalstats.YAVG=([0-9.]+)")
    
    current_pts = 0.0
    for line in p.stderr:
        m_pts = pts_pattern.search(line)
        if m_pts:
            current_pts = float(m_pts.group(1))
        m_y = y_pattern.search(line)
        if m_y:
            y_val = float(m_y.group(1))
            if y_val > max_y:
                max_y = y_val
                max_pts = current_pts
    p.wait()
    print(f"{name}: Flash detected at {max_pts:.2f}s (Y={max_y:.1f})")
