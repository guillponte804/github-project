import requests
from bs4 import BeautifulSoup

def fetch_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return None

# Example usage
text = fetch_text("https://example.com")
if text is not None:
    with open("/tmp/fetch_data.txt", "w") as file:
        file.write(text)
