import subprocess
import json

raw_path = "output/left_hanging_public_raw.mp4"
mastered_path = "output/left_hanging_public_mastered.mp4"
temp_path = "output/left_hanging_public_temp.mp4"

# Pass 1 measurement
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
print("Measured:", stats)

# Pass 2 application
af = (
    f"loudnorm=I=-14.0:TP=-1.5:LRA=11:"
    f"measured_I={stats['input_i']}:"
    f"measured_TP={stats['input_tp']}:"
    f"measured_LRA={stats['input_lra']}:"
    f"measured_thresh={stats['input_thresh']}:"
    f"offset={stats['target_offset']}:linear=true"
)

cmd2 = [
    'ffmpeg', '-y', '-i', raw_path,
    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k',
    '-af', af, mastered_path
]
subprocess.run(cmd2, check=True)

# Verification
cmd3 = ['ffmpeg', '-i', mastered_path, '-af', 'ebur128=peak=true', '-f', 'null', '-']
res3 = subprocess.run(cmd3, capture_output=True, text=True)
lines = res3.stderr.splitlines()
for i, line in enumerate(lines):
    if 'Summary:' in line:
        print("\n".join(lines[i:i+16]))
        break
