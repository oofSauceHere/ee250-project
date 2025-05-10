import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import requests

# settings
rate = 48000
duration = 10

# record from mic
rec = sd.rec(frames=duration*rate, samplerate=rate, channels=1)
print("recording...")

# wait to finish
sd.wait()
print("done!")

write('recording.wav', rate, rec)
print("saved!")

# create a dictionary with the audio file to be sent for processing
files = {'audio': open("recording.wav", "rb")}
res = requests.post("http://192.168.99.25:5000/upload", files=files)
print(res.text)