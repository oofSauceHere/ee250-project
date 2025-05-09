import requests

# create a dictionary with the audio file to be sent for processing
files = {'audio': open("./testing-audio/night-walk-1.mp3", "rb")}
res = requests.post("http://127.0.0.1:5000/upload", files=files)
print(res.text)