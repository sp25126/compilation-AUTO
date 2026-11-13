import subprocess
import glob
import json

for p in sorted(glob.glob('public/clips/left_hanging_public/rank_*.mp4')):
    cmd = ['ffprobe', '-v', 'quiet', '-show_streams', '-of', 'json', p]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(res.stdout)
    v = [s for s in data['streams'] if s['codec_type'] == 'video'][0]
    a = [s for s in data['streams'] if s['codec_type'] == 'audio'][0]
    print(f"{p} | {v['width']}x{v['height']} | fps:{v['r_frame_rate']} | frames:{v.get('nb_frames')} | dur:{v.get('duration')}s | a_rate:{a['sample_rate']}")
