import subprocess

cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi", "-i",
    "anoisesrc=d=60:c=pink:r=48000:a=0.15[wind];"
    "sine=f=55:d=60[sub1];"
    "sine=f=82.4:d=60[sub2];"
    "sine=f=110:d=60[sub3];"
    "[wind]lowpass=f=240,flanger=delay=15:depth=8:regen=30:width=80:speed=0.2[amb];"
    "[sub1]volume=0.35[s1];"
    "[sub2]volume=0.20[s2];"
    "[sub3]volume=0.15[s3];"
    "[amb][s1][s2][s3]amix=inputs=4:duration=first:dropout_transition=2[mix];"
    "[mix]volume=1.2,highpass=f=35,lowpass=f=3200,afade=t=in:ss=0:d=1.5,afade=t=out:st=57:d=3",
    "-c:a", "libmp3lame", "-b:a", "320k", "-ar", "48000",
    "public/audio/stems/lightning_jump_scares_music_bed.mp3"
]

print("Synthesizing lightning_jump_scares_music_bed.mp3...")
subprocess.run(cmd, check=True)
print("Audio bed created successfully!")
