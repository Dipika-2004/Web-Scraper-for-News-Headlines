import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/news" 
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all('h2')  
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        title = headline.get_text(strip=True)
        if title:  # Avoid empty strings
            file.write(title + "\n")
print("Headlines saved to headlines.txt")