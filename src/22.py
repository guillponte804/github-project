import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"  # Replace with the desired website URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
