import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('p', {'class': 'example-class'})
    else:
        return None

url = "https://example.com"
content = fetch_content(url)

if content:
    for element in content:
        print(element)
else:
    print("Failed to load content")
