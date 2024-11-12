import requests as r
from bs4 import BeautifulSoup as s

#This gets ther content of the url and sets it to object r
r = r.get('https://quotes.toscrape.com/random').text

soup = s(r, 'lxml')
#finds all info between these tags, and then gets the text between the tags
soup = soup.find("span", {"class":'text'}).get_text()

print(soup)


