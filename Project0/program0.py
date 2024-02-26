import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')
countries = soup.find_all('div', class_='row')
countries = countries[3:87]
data = []
for country in countries:
    name = country.find('h3', class_='country-name').text.strip()
    capital = country.find('span', class_='country-capital').text
    population = country.find('span', class_='country-population').text
    area = country.find('span', class_='country-area').text
    data.append([name, capital, population, area])

df = pd.DataFrame(data, columns = ["Country", "Capital", "Population", "Area (km^2)"])
df.to_csv('countries.csv')