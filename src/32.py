import requests
import json

url = "https://api.example.com/data"
headers = {
    "Authorization": "Bearer your_api_token",
    # add any other required headers here
}

response = requests.get(url, headers=headers)
data = response.json()

print(data)
