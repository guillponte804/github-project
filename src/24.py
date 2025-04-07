import requests
from bs4 import BeautifulSoup
import re

url = "https://www.example.com"
html_content = requests.get(url).content

soup = BeautifulSoup(html_content, 'lxml')

title = soup.find('h1', class_='example-class').text.strip()
print("Title:", title)

# Example: 
pattern = re.compile(r'<span>(.*?)</span>', re.DOTALL)
result = pattern.search(title)
if result:
    print("Pattern found:")
    print(result.group(1))
else:
    print("No pattern found.")
