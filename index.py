from bs4 import BeautifulSoup
import requests

url = 'https://zbinworld.com/usa-college-admissions-presentation-for-zimbos/'

page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
print(soup)