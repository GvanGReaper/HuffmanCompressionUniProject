import requests
res = requests.post('http://127.0.0.1:5000/sending', json={
    "mytext":"lalala",
    "myage": 18
})



