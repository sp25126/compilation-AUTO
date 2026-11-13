import subprocess
import json

for rank in [5, 4, 3, 2, 1]:
    f = f"public/clips/accidental_trickshots/rank_{rank}.mp4"
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-count_packets",
        "-show_entries", "stream=nb_read_packets,duration,width,height,r_frame_rate",
        "-of", "json",
        f
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    d = json.loads(res.stdout)
    st = d["streams"][0]
    print(f"Rank {rank}: {st.get('nb_read_packets')} frames, {st.get('duration')}s, {st.get('width')}x{st.get('height')}, fps={st.get('r_frame_rate')}")
