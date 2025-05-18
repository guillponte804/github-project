import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Add your code here to parse the HTML and extract specific information

url = "https://example.com"
html = fetch_html(url)
if html:
    parsed_html = parse_html(html)
    print(parsed_html)

