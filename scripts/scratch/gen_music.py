import numpy as np
from scipy.io import wavfile
import os

sr = 44100
dur = 65  # seconds
t = np.linspace(0, dur, int(sr*dur), endpoint=False)

mix = np.zeros(len(t))

# Energetic sports comedy arcade beat
# Bass pattern - E2(82Hz) upbeat groove
bass_pattern = [(82,0.25),(82,0.125),(98,0.125),(110,0.25),(82,0.125),(98,0.25)]
pos=0
while pos < dur:
    for freq,length in bass_pattern:
        if pos < dur:
            s=int(pos*sr); e=min(int((pos+length)*sr),len(mix))
            tt=t[s:e]
            if len(tt)==0: pos+=length; continue
            sig=0.35*(2*(tt*freq%1)-1)
            env=np.ones(len(tt)); att=int(0.005*sr); rel=int(0.02*sr)
            env[:min(att,len(tt))]=np.linspace(0,1,min(att,len(tt)))
            env[-min(rel,len(tt)):]=np.linspace(1,0,min(rel,len(tt)))
            mix[s:e] += sig*env
        pos+=length

# Bright melody - bouncy sports fanfare
melody_notes = [(523,0.25),(659,0.25),(784,0.25),(880,0.5),(784,0.25),(659,0.5),(523,0.25),(0,0.25),
                (659,0.25),(784,0.25),(880,0.25),(1047,0.5),(880,0.25),(784,0.5),(659,0.25),(0,0.5)]
pos=0
while pos < dur:
    for freq,length in melody_notes:
        if pos < dur and freq > 0:
            s=int(pos*sr); e=min(int((pos+length)*sr),len(mix))
            tt=t[s:e]
            if len(tt)==0: pos+=length; continue
            sig=0.18*np.sin(2*np.pi*freq*tt)
            env=np.ones(len(tt)); att=int(0.01*sr); rel=int(0.03*sr)
            env[:min(att,len(tt))]=np.linspace(0,1,min(att,len(tt)))
            env[-min(rel,len(tt)):]=np.linspace(1,0,min(rel,len(tt)))
            mix[s:e] += sig*env
        pos+=length

# Hi-hat 8th notes
rng = np.random.default_rng(42)
for i in range(int(dur*4)):
    s=int(i*0.25*sr); e=min(s+int(0.08*sr),len(mix))
    if s < len(mix):
        noise = 0.08*rng.standard_normal(e-s)
        env=np.linspace(1,0,e-s)
        mix[s:e] += noise*env

# Kick drum on beats 1 and 3
for i in range(int(dur*2)):
    s=int(i*0.5*sr); e=min(s+int(0.1*sr),len(mix))
    if s < len(mix):
        tt2=np.linspace(0,0.1,e-s)
        kick=0.5*np.sin(2*np.pi*(80+300*np.exp(-40*tt2))*tt2)
        env=np.exp(-30*tt2)
        mix[s:e] += kick*env

# Snare on beats 2 and 4
for i in range(int(dur*2)):
    s=int((i*0.5+0.25)*sr); e=min(s+int(0.08*sr),len(mix))
    if s < len(mix):
        noise = 0.3*rng.standard_normal(e-s)
        env=np.exp(-50*np.linspace(0,0.08,e-s))
        mix[s:e] += noise*env

# Normalize
mx = np.max(np.abs(mix))
if mx > 0: mix = mix / mx * 0.75

mix16 = (mix * 32767).astype(np.int16)
wavfile.write('public/audio/stems/trickshot_disasters_music_bed.wav', sr, mix16)
print('WAV written successfully')
