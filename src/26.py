import requests
import os

url = "http://example.com/upload"
file_path = "/path/to/your/file.pdf"

response = requests.post(url, files={"file": open(file_path, "rb")})

if response.status_code == 201:
    print("Upload successful!")
else:
    print(f"Failed to upload. Status code: {response.status_code}")
