import subprocess
import os

print("--- Step 1: Mastering with loudnorm ---")
master_cmd = [
    'ffmpeg', '-y',
    '-i', 'output/cocky_challengers_raw.mp4',
    '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11',
    '-c:v', 'copy',
    '-c:a', 'aac', '-b:a', '320k',
    'output/cocky_challengers_mastered.mp4'
]
subprocess.run(master_cmd, check=True)

print("--- Step 2: Measuring EBU R128 Loudness ---")
ebur_cmd = [
    'ffmpeg',
    '-i', 'output/cocky_challengers_mastered.mp4',
    '-af', 'ebur128=peak=true',
    '-f', 'null', '-'
]
p = subprocess.run(ebur_cmd, capture_output=True, text=True)
print(p.stderr[-1000:])

print("--- Step 3: Generating 1fps QA Contact Sheet ---")
qa_sheet_cmd = [
    'ffmpeg', '-y',
    '-i', 'output/cocky_challengers_mastered.mp4',
    '-vf', 'fps=1,scale=260:-1,tile=8x6',
    '-frames:v', '1',
    '-q:v', '3',
    'output/cocky_challengers_qa_sheet.jpg'
]
subprocess.run(qa_sheet_cmd, check=True)
print("QA Sheet generated at output/cocky_challengers_qa_sheet.jpg")
