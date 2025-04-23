import requests

def send_request():
    response = requests.post('http://your-api-endpoint', json={'data': 'Hello World'})
    print(response.json())

if __name__ == "__main__":
    send_request()
