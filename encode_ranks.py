import subprocess
import os

out_dir = r"public/clips/cocky_challengers"
os.makedirs(out_dir, exist_ok=True)

# Rank 5: yt_LGdXphdEbdE.mp4 (19.5s to 27.5s)
print("Encoding Rank 5...")
cmd5 = [
    'ffmpeg', '-y',
    '-ss', '19.5', '-to', '27.5',
    '-i', 'temp_harvest/cocky_challengers/yt_LGdXphdEbdE.mp4',
    '-vf', 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '15', '-keyint_min', '15', '-sc_threshold', '0',
    '-c:a', 'aac', '-ar', '48000', '-b:a', '192k',
    os.path.join(out_dir, 'rank_5.mp4')
]
subprocess.run(cmd5, check=True)

# Rank 4: r_uj7d9xww5ax81.mp4 (5.0s to 13.0s)
print("Encoding Rank 4...")
cmd4 = [
    'ffmpeg', '-y',
    '-ss', '5.0', '-to', '13.0',
    '-i', 'temp_harvest/cocky_challengers/r_uj7d9xww5ax81.mp4',
    '-vf', 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '15', '-keyint_min', '15', '-sc_threshold', '0',
    '-c:a', 'aac', '-ar', '48000', '-b:a', '192k',
    os.path.join(out_dir, 'rank_4.mp4')
]
subprocess.run(cmd4, check=True)

# Rank 3: yt_lLxK7FEJ7o0.mp4 (0.5s to 8.5s)
print("Encoding Rank 3...")
cmd3 = [
    'ffmpeg', '-y',
    '-ss', '0.5', '-to', '8.5',
    '-i', 'temp_harvest/cocky_challengers/yt_lLxK7FEJ7o0.mp4',
    '-vf', 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '15', '-keyint_min', '15', '-sc_threshold', '0',
    '-c:a', 'aac', '-ar', '48000', '-b:a', '192k',
    os.path.join(out_dir, 'rank_3.mp4')
]
subprocess.run(cmd3, check=True)

# Rank 2: 2-part splice: face-off (2.0s to 5.0s) + fight (34.0s to 39.0s)
print("Encoding Rank 2...")
# part A
cmd2_a = [
    'ffmpeg', '-y',
    '-ss', '2.0', '-to', '5.0',
    '-i', 'temp_harvest/cocky_challengers/yt_1LmeQ3Vci_w.mp4',
    '-vf', 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '15', '-keyint_min', '15', '-sc_threshold', '0',
    '-c:a', 'aac', '-ar', '48000', '-b:a', '192k',
    'temp_harvest/cocky_challengers/r2_part_a.mp4'
]
subprocess.run(cmd2_a, check=True)

# part B
cmd2_b = [
    'ffmpeg', '-y',
    '-ss', '34.0', '-to', '39.0',
    '-i', 'temp_harvest/cocky_challengers/yt_1LmeQ3Vci_w.mp4',
    '-vf', 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '15', '-keyint_min', '15', '-sc_threshold', '0',
    '-c:a', 'aac', '-ar', '48000', '-b:a', '192k',
    'temp_harvest/cocky_challengers/r2_part_b.mp4'
]
subprocess.run(cmd2_b, check=True)

# concat list
with open('temp_harvest/cocky_challengers/concat_r2.txt', 'w') as f:
    f.write("file 'r2_part_a.mp4'\nfile 'r2_part_b.mp4'\n")

cmd2_cat = [
    'ffmpeg', '-y',
    '-f', 'concat', '-safe', '0',
    '-i', 'temp_harvest/cocky_challengers/concat_r2.txt',
    '-c', 'copy',
    os.path.join(out_dir, 'rank_2.mp4')
]
subprocess.run(cmd2_cat, check=True)

# Rank 1: yt_BzIJ0bNwgIM.webm (29.5s to 37.5s)
print("Encoding Rank 1...")
cmd1 = [
    'ffmpeg', '-y',
    '-ss', '29.5', '-to', '37.5',
    '-i', 'temp_harvest/cocky_challengers/yt_BzIJ0bNwgIM.webm',
    '-vf', 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '15', '-keyint_min', '15', '-sc_threshold', '0',
    '-c:a', 'aac', '-ar', '48000', '-b:a', '192k',
    os.path.join(out_dir, 'rank_1.mp4')
]
subprocess.run(cmd1, check=True)

print("All 5 ranks successfully encoded!")
