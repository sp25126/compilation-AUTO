import subprocess
import json
import shutil
import sys
import os

def master_video(raw_path, mastered_path):
    print(f"Mastering {raw_path} -> {mastered_path}...")
    temp_path = raw_path.replace(".mp4", "_temp_master.mp4")
    
    # 1. First pass measurement
    cmd1 = [
        'ffmpeg', '-y', '-i', raw_path,
        '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json',
        '-f', 'null', '-'
    ]
    res1 = subprocess.run(cmd1, capture_output=True, text=True)
    stderr = res1.stderr
    idx_s = stderr.rfind('{')
    idx_e = stderr.rfind('}') + 1
    stats = json.loads(stderr[idx_s:idx_e])
    print(f"Pass 1: input_i={stats['input_i']}, input_tp={stats['input_tp']}, offset={stats['target_offset']}")
    
    # 2. Second pass normalization
    af_filter = (
        f"loudnorm=I=-14:TP=-1.5:LRA=11:"
        f"measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:"
        f"measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:"
        f"offset={stats['target_offset']}:linear=true"
    )
    cmd2 = [
        'ffmpeg', '-y', '-i', raw_path,
        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k',
        '-af', af_filter, temp_path
    ]
    subprocess.run(cmd2, check=True)
    shutil.move(temp_path, mastered_path)
    
    # 3. Verification
    cmd3 = ['ffmpeg', '-i', mastered_path, '-af', 'ebur128=peak=true', '-f', 'null', '-']
    res3 = subprocess.run(cmd3, capture_output=True, text=True)
    lines = res3.stderr.splitlines()
    for i, line in enumerate(lines):
        if 'Integrated loudness:' in line:
            print("\n".join(lines[i:i+15]))
            break
            
    # 4. Generate 1fps QA contact sheet
    sheet_path = mastered_path.replace("_mastered.mp4", "_qa_sheet.jpg")
    cmd_sheet = [
        'ffmpeg', '-y', '-i', mastered_path,
        '-vf', 'fps=1,scale=180:320,tile=8x6',
        '-frames:v', '1', '-q:v', '2', sheet_path
    ]
    subprocess.run(cmd_sheet, check=True)
    print(f"Generated QA sheet: {sheet_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python master_audio.py <raw_video> <mastered_video>")
        sys.exit(1)
    master_video(sys.argv[1], sys.argv[2])
