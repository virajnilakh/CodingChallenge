import urllib
import wave
import struct

duration=3000
sample_rate=44100.0
samples=duration*(sample_rate/1000.0)
from random import randint
audio=[]
random=0

for i in range(0,int(samples)):
    if int(random) == 0:
        random = urllib.request.urlopen(
            "https://www.random.org/integers/?num=1&min=-3267&max=3267&col=1&base=10&format=plain&rnd=new").read()

    audio.append(random)
    random/10

sound_file=wave.open('my_sound.wav',"w")
channels = 1
width = 2
frames = len(audio)
comp_type = "NONE"
comp_name = "not compressed"
sound_file.setparams((channels,width,sample_rate,frames,comp_type,comp_name))

for j in audio:
    sound_file.writeframes(struct.pack('h',int(j)))

sound_file.close()
