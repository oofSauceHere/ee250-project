import requests

files = {'file': open("./testing-audio/night-walk-1.mp3", "rb")}
res = requests.post("http://localhost:5000/upload", files=files)
print(res.text)