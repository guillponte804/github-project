import requests
from bs4 import BeautifulSoup
import re
import os

def search_book(book_name):
    url = f"https://www.google.com/search?q={book_name}+python"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='r'))
    
    for i in range(len(results)):
        title = results[i].find('h3', class_='g')
        link = title.find('a')['href']
        
        if re.search("python", title.text):
            with open(f"python_{i+1}.txt", "w") as file:
                file.write(link)
                print(f"Found {book_name} on Google, saving to {book_name}_{i+1}.txt")

def main():
    books = os.listdir(".")
    
    for book in books:
        if os.path.isfile(book):
            search_book(os.path.basename(book))

if __name__ == "__main__":
    main()
