import subprocess, json

for i in [5, 4, 3, 2, 1]:
    path = f'public/clips/unintentional_hero_catches/clip_{i}.mp4'
    cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_packets',
           '-show_entries', 'stream=nb_read_packets,width,height,r_frame_rate,pix_fmt',
           '-of', 'json', path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    vdata = json.loads(res.stdout)['streams'][0]

    cmd_a = ['ffprobe', '-v', 'error', '-select_streams', 'a:0',
             '-show_entries', 'stream=codec_name,sample_rate,channels',
             '-of', 'json', path]
    res_a = subprocess.run(cmd_a, capture_output=True, text=True)
    adata = json.loads(res_a.stdout)['streams'][0]

    cmd_d = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', path]
    res_d = subprocess.run(cmd_d, capture_output=True, text=True)
    duration = float(json.loads(res_d.stdout)['format']['duration'])

    print(f"clip_{i}: frames={vdata.get('nb_read_packets')}, dur={duration:.2f}s, res={vdata['width']}x{vdata['height']}, fps={vdata['r_frame_rate']}, pix_fmt={vdata['pix_fmt']}, aac={adata['codec_name']}, sr={adata['sample_rate']}")
