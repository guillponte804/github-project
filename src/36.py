import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve the web page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None

def scrape_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Assuming data is in a specific tag that starts with 'data-source'
    data = soup.find('div', {'class': 'data-source'}).text
    return data

# Example usage
url = "https://example.com"  # Replace with the URL of your webpage
html = get_html(url)
if html:
    print("Scraped Data: ", scrape_data(html))
else:
    print("Failed to retrieve the web page. Please check your URL and try again.")
