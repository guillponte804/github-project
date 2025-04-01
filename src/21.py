import requests
import json

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}, status code: {response.status_code}")

data = fetch_data('https://api.example.com/data')
json_data = json.dumps(data)
print(json_data)
