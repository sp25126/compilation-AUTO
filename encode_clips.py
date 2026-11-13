import subprocess
import json
import os

clips = [
    {
        'rank': 5,
        'src': 'temp_harvest/couple_pranks_gone_wholesome/yt_dv8u_g64g2A.mp4',
        'ss': '00:00:27.5',
        't': '8.0',
        'vf': 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2'
    },
    {
        'rank': 4,
        'src': 'temp_harvest/couple_pranks_gone_wholesome/yt_OcONhIIHw3k.webm',
        'ss': '00:00:33.5',
        't': '8.0',
        'vf': 'crop=608:1080:600:0,scale=1080:1920,setpts=PTS-STARTPTS,fps=30'
    },
    {
        'rank': 3,
        'src': 'temp_harvest/couple_pranks_gone_wholesome/yt_9nDcSeT37Bg.mp4',
        'ss': '00:00:04.0',
        't': '8.0',
        'vf': 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2'
    },
    {
        'rank': 2,
        'src': 'temp_harvest/couple_pranks_gone_wholesome/r_i4xkszyeg3d31.mp4',
        'ss': '00:00:47.5',
        't': '8.0',
        'vf': 'setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2'
    },
    {
        'rank': 1,
        'src': 'temp_harvest/couple_pranks_gone_wholesome/yt_ErXHxxiF7EQ.mp4',
        'ss': '00:00:26.0',
        't': '8.0',
        'vf': 'crop=608:1080:656:0,scale=1080:1920,setpts=PTS-STARTPTS,fps=30'
    }
]

os.makedirs('public/clips/couple_pranks_gone_wholesome', exist_ok=True)

for c in clips:
    rank_num = c['rank']
    out = f'public/clips/couple_pranks_gone_wholesome/rank_{rank_num}.mp4'
    cmd = [
        'ffmpeg', '-y',
        '-ss', c['ss'],
        '-t', c['t'],
        '-i', c['src'],
        '-vf', c['vf'],
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-r', '30',
        '-g', '15',
        '-keyint_min', '15',
        '-sc_threshold', '0',
        '-c:a', 'aac',
        '-ar', '48000',
        '-b:a', '192k',
        out
    ]
    print(f"Encoding rank {rank_num}...")
    subprocess.check_call(cmd)
    print(f"Done rank {rank_num}")

print("All 5 clips encoded successfully!")
