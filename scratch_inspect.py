import os
import subprocess
import glob

files = glob.glob("temp_harvest/lightning_jump_scares/*.mp4")
os.makedirs("temp_harvest/lightning_jump_scares/qa", exist_ok=True)

for f in files:
    base = os.path.splitext(os.path.basename(f))[0]
    sheet = f"temp_harvest/lightning_jump_scares/qa/{base}_sheet.jpg"
    
    # Get duration
    cmd_dur = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", f]
    dur = subprocess.check_output(cmd_dur, text=True).strip()
    
    # Generate 2fps tile sheet
    cmd_sheet = [
        "ffmpeg", "-y", "-i", f,
        "-vf", "fps=2,scale=260:-1,tile=8x10",
        "-frames:v", "1", "-q:v", "3",
        sheet
    ]
    subprocess.run(cmd_sheet, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"{base}: duration={dur}s, sheet={sheet}")
