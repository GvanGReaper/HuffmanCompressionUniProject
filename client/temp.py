import requests


res = requests.post('http://127.0.0.1:5000/result', json={
    "mytext":"lalala",
    "myage": 18
})

res = requests.get("http://127.0.0.1:5000/result")
t = res.text
print(t)