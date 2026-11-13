import subprocess
import re

raw = 'output/couple_pranks_gone_wholesome_raw.mp4'
mastered = 'output/couple_pranks_gone_wholesome_mastered.mp4'

# First run standard loudnorm with I=-14.0, TP=-1.6
cmd1 = [
    'ffmpeg', '-y',
    '-i', raw,
    '-af', 'loudnorm=I=-14.0:TP=-1.6:LRA=11',
    '-c:v', 'copy',
    '-c:a', 'aac',
    '-b:a', '320k',
    mastered
]
subprocess.check_call(cmd1)

# Check ebur128
def check_loudness():
    res = subprocess.run(['ffmpeg', '-i', mastered, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                         capture_output=True, text=True)
    out = res.stderr
    i_val = re.search(r'I:\s+([-\d.]+)\s+LUFS', out)
    tp_val = re.search(r'Peak:\s+([-\d.]+)\s+dBFS', out)
    return float(i_val.group(1)) if i_val else None, float(tp_val.group(1)) if tp_val else None

curr_i, curr_tp = check_loudness()
print(f"Pass 1: I={curr_i} LUFS, TP={curr_tp} dBFS")

# If TP > -1.5, reduce gain slightly
if curr_tp > -1.5:
    diff = -1.6 - curr_tp
    print(f"Applying gain adjustment: {diff:.2f} dB")
    temp = 'output/temp_adj.mp4'
    subprocess.check_call([
        'ffmpeg', '-y',
        '-i', mastered,
        '-af', f'volume={diff:.2f}dB',
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-b:a', '320k',
        temp
    ])
    import shutil
    shutil.move(temp, mastered)
    curr_i, curr_tp = check_loudness()
    print(f"After adjustment: I={curr_i} LUFS, TP={curr_tp} dBFS")

print(f"FINAL LOUDNESS: I={curr_i} LUFS, TP={curr_tp} dBFS")
