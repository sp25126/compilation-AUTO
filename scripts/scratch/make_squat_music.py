import numpy as np
from scipy.io import wavfile
import subprocess, os

sr = 44100
dur = 65  # seconds
t = np.linspace(0, dur, int(sr*dur), endpoint=False)

mix = np.zeros(len(t))

# Heavy gym phonk/trap bass & kick rhythm (130 BPM -> 0.4615s per beat)
bpm = 128
spb = 60.0 / bpm
t_beat = np.linspace(0, spb, int(sr*spb), endpoint=False)

# Punchy Kick drum (drops from 150Hz to 45Hz)
kick_env = np.exp(-t_beat * 24)
kick_freq = 45 + 105 * np.exp(-t_beat * 35)
kick_wave = np.sin(2 * np.pi * kick_freq * t_beat) * kick_env * 0.45

# Snare / Clap on beats 2 & 4
snare_noise = (np.random.rand(len(t_beat)) * 2 - 1) * np.exp(-t_beat * 18) * 0.22
snare_tone = np.sin(2 * np.pi * 190 * t_beat) * np.exp(-t_beat * 25) * 0.18
snare_hit = snare_noise + snare_tone

# Phonk cowbell / synth riff pattern
# Frequencies: A4=440, C5=523, D5=587, E5=659, G5=784
cowbell_riff = [
    (440, 0.25), (440, 0.25), (523, 0.25), (587, 0.25),
    (659, 0.5),  (587, 0.25), (523, 0.25), (440, 0.5),
    (392, 0.25), (440, 0.25), (523, 0.5),  (440, 0.5)
]

num_beats = int(dur / spb)
for b in range(num_beats):
    idx = int(b * spb * sr)
    # Kick on 1 and 3 (and syncopated on 2.5)
    beat_in_bar = b % 4
    if beat_in_bar == 0 or beat_in_bar == 2:
        end_idx = min(idx + len(kick_wave), len(mix))
        mix[idx:end_idx] += kick_wave[:end_idx-idx]
    if beat_in_bar == 1 or beat_in_bar == 3:
        end_idx = min(idx + len(snare_hit), len(mix))
        mix[idx:end_idx] += snare_hit[:end_idx-idx]

# Sub-bass 808 glide (45Hz - 55Hz)
bass_t = np.linspace(0, dur, len(mix))
bass_sub = np.sin(2 * np.pi * 50 * bass_t) * 0.28
# duck sub slightly on kick
mix += bass_sub

# Cowbell melody overlay
curr_time = 0.0
riff_idx = 0
while curr_time < dur:
    freq, beats = cowbell_riff[riff_idx % len(cowbell_riff)]
    dur_note = beats * spb
    note_samples = int(dur_note * sr)
    tn = np.linspace(0, dur_note, note_samples, endpoint=False)
    # Metallic cowbell tone (harmonic rich)
    env = np.exp(-tn * 9)
    cowbell = (np.sin(2 * np.pi * freq * tn) + 0.5 * np.sin(2 * np.pi * freq * 1.5 * tn) + 0.3 * np.sin(2 * np.pi * freq * 2.5 * tn)) * env * 0.16
    start_s = int(curr_time * sr)
    end_s = min(start_s + len(cowbell), len(mix))
    mix[start_s:end_s] += cowbell[:end_s-start_s]
    curr_time += dur_note
    riff_idx += 1

# Normalize
mix = mix / (np.max(np.abs(mix)) + 1e-6) * 0.85
mix_int16 = (mix * 32767).astype(np.int16)

wav_path = "temp_harvest/squat_rack_blunders/music_bed.wav"
wavfile.write(wav_path, sr, mix_int16)

out_mp3 = "public/audio/stems/squat_rack_blunders_music_bed.mp3"
os.makedirs("public/audio/stems", exist_ok=True)
cmd = ["ffmpeg", "-y", "-i", wav_path, "-c:a", "libmp3lame", "-b:a", "192k", out_mp3]
subprocess.run(cmd, check=True)
print(f"Generated {out_mp3} successfully!")
