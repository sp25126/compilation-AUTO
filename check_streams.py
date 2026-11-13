import subprocess

# Check r_ynyg9kurrsa61.mp4 exact audio and video streams
cmd1 = ["ffprobe", "-v", "error", "-show_entries", "stream=duration,nb_frames", "-of", "default=noprint_wrappers=1", "temp_harvest/lightning_jump_scares/r_ynyg9kurrsa61.mp4"]
print("r_ynyg9kurrsa61 streams:")
print(subprocess.check_output(cmd1, text=True))

# Check yt_5xSmGNgC5kc.mp4
cmd2 = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1", "temp_harvest/lightning_jump_scares/yt_5xSmGNgC5kc.mp4"]
print("yt_5xSmGNgC5kc duration:")
print(subprocess.check_output(cmd2, text=True))
