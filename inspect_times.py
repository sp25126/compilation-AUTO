import subprocess

def inspect_range(video_path, start_s, dur_s, out_prefix):
    cmd = [
        "ffmpeg", "-y", "-ss", str(start_s), "-t", str(dur_s), "-i", video_path,
        "-vf", "fps=1,scale=320:-1", "-q:v", "2", f"temp_harvest/left_hanging_public/{out_prefix}_%02d.jpg"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

inspect_range("temp_harvest/left_hanging_public/longest_highfive_rejection_Ft41g48Kp-0.mp4", 28, 12, "test_rank5")
inspect_range("temp_harvest/left_hanging_public/mclaurin_handshake_9WalqnrDu08.mp4", 1.5, 7.5, "test_rank4")
inspect_range("temp_harvest/left_hanging_public/kobe_phil_hanging_2CBVPTgyZjA.mp4", 15, 12, "test_rank3")
inspect_range("temp_harvest/left_hanging_public/trump_polish_handshake_PD03pcjKnMw.mp4", 5, 10, "test_rank2")
inspect_range("temp_harvest/left_hanging_public/seacrest_blind_highfive_TSdw4MKaxxo.mp4", 16, 9, "test_rank1")
print("Inspection frames generated.")
