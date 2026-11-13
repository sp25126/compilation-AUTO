import subprocess
import json

# Run 2-pass loudnorm analysis
cmd1 = [
    'ffmpeg', '-y', '-i', 'output/cocky_challengers_raw.mp4',
    '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json',
    '-f', 'null', '-'
]
p1 = subprocess.run(cmd1, capture_output=True, text=True)
output = p1.stderr
json_str = output[output.rfind('{'):output.rfind('}')+1]
stats = json.loads(json_str)
print('Analysis stats:', stats)

# Second pass
cmd2 = [
    'ffmpeg', '-y', '-i', 'output/cocky_challengers_raw.mp4',
    '-af', f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:offset={stats['target_offset']}:linear=true",
    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k',
    'output/cocky_challengers_mastered.mp4'
]
subprocess.run(cmd2, check=True)

# Verify
cmd3 = ['ffmpeg', '-i', 'output/cocky_challengers_mastered.mp4', '-af', 'ebur128=peak=true', '-f', 'null', '-']
p3 = subprocess.run(cmd3, capture_output=True, text=True)
for line in p3.stderr.splitlines()[-20:]:
    print(line)

# Re-generate QA contact sheet
cmd4 = [
    'ffmpeg', '-y',
    '-i', 'output/cocky_challengers_mastered.mp4',
    '-vf', 'fps=1,scale=260:-1,tile=8x6',
    '-frames:v', '1',
    '-q:v', '3',
    'output/cocky_challengers_qa_sheet.jpg'
]
subprocess.run(cmd4, check=True)
print("QA Sheet re-generated.")
