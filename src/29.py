import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

url = "https://example.com"
soup = fetch_html(url)
if soup:
    for link in soup.find_all('a'):
        print(link.get("href"))
