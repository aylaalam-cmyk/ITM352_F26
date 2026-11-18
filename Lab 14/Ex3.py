#Scrape names of ITM faulculty and grad students
import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://www.itm.ilstu.edu/people/faculty/"
print("Retrieving", itm_url)

itm_page = urllib.request.urlopen(itm_url)
itm_names = []

soup = BeautifulSoup(itm_page, 'html.parser')
#Find all the facualty, which are in h2 tags with class = "title"
faulty = soup.find_all("h2", class_="title")

for person in faulty:
    itm_names.append(p)
    









