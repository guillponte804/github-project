import os
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

def main():
    # Your code here, replace the URLs with your own
    data1 = fetch_data("http://example.com/data1")
    data2 = fetch_data("http://example.com/data2")

if __name__ == "__main__":
    main()
