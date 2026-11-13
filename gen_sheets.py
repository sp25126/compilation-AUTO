import subprocess
import glob
import os

files = glob.glob('temp_harvest/cocky_challengers/*.*')
for f in files:
    if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.ytdl') or f.endswith('.part'):
        continue
    base = os.path.splitext(os.path.basename(f))[0]
    out_sheet = os.path.join('temp_harvest/cocky_challengers', f"sheet_{base}.jpg")
    cmd = [
        'ffmpeg', '-y', '-i', f,
        '-vf', 'fps=2,scale=260:-1,tile=8x10',
        '-frames:v', '1',
        '-q:v', '3',
        out_sheet
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_sheet):
        print(f"Generated {out_sheet}")
    else:
        print(f"Failed {out_sheet}")
