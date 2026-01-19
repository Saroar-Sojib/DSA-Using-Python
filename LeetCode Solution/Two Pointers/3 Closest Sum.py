import json
import requests


url = "http://192.168.146.235:80/jwt-api-token-auth/"
headers = {
    "Content-Type": "application/json",
}
data = {
    "username": "99011",
    "password": "123456"
}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)