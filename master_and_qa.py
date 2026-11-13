import subprocess
import re
import sys

raw_mp4 = "output/love_at_first_sight_caught_raw.mp4"
mastered_mp4 = "output/love_at_first_sight_caught_mastered.mp4"
qa_sheet = "output/love_at_first_sight_caught_qa_sheet.jpg"

print("--- Step 1: EBU R128 Mastering ---")
cmd_master = [
    "ffmpeg", "-y", "-i", raw_mp4,
    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
    "-c:v", "copy", "-c:a", "aac", "-b:a", "320k",
    mastered_mp4
]
subprocess.run(cmd_master, check=True)
print("Mastered MP4 written successfully!")

print("\n--- Step 2: Measuring Loudness Metrics ---")
cmd_ebur = [
    "ffmpeg", "-i", mastered_mp4,
    "-filter:a", "ebur128=peak=true",
    "-f", "null", "-"
]
res = subprocess.run(cmd_ebur, capture_output=True, text=True)
stderr = res.stderr

# Parse loudness summary
# Expected format:
#   Integrated loudness:
#     I:         -14.0 LUFS
#     Threshold: -24.0 LUFS
#   Loudness range:
#     LRA:         5.1 LU
#   True peak:
#     Peak:       -1.5 dBFS

i_match = re.search(r"I:\s+([-\d.]+)\s+LUFS", stderr)
lra_match = re.search(r"LRA:\s+([-\d.]+)\s+LU", stderr)
tp_match = re.search(r"Peak:\s+([-\d.]+)\s+dBFS", stderr)

i_val = float(i_match.group(1)) if i_match else None
lra_val = float(lra_match.group(1)) if lra_match else None
tp_val = float(tp_match.group(1)) if tp_match else None

print(f"Integrated Loudness (I): {i_val} LUFS (Target: -14.0 ± 1.0 LUFS)")
print(f"Loudness Range (LRA):   {lra_val} LU")
print(f"True Peak (TP):         {tp_val} dBTP (Target: <= -1.5 dBTP)")

print("\n--- Step 3: Generating 1fps QA Contact Sheet ---")
cmd_sheet = [
    "ffmpeg", "-y", "-i", mastered_mp4,
    "-vf", "fps=1,scale=260:-1,tile=8x6",
    "-frames:v", "1", "-q:v", "3",
    qa_sheet
]
subprocess.run(cmd_sheet, check=True)
print(f"1fps QA Sheet generated at: {qa_sheet}")
