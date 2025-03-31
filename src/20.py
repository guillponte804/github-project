import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('div', class_='news-item')
    return [item.text for item in news_items]

url = "https://example.com"
print(fetch_news(url))
