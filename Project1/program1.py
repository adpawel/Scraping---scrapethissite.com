import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.scrapethissite.com/pages/forms/"
response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')
table = soup.find('table', class_ = 'table')
rows = table.find_all("tr", class_ = "team")
rows = rows[0:2]
data = []

for row in rows:
    name = row.find("td", class_ = "name").text.strip()
    year = row.find("td", class_ = "year").text.strip()
    wins = row.find("td", class_ = "wins").text.strip()
    losses = row.find("td", class_ = "losses").text.strip()
    ot_losses = row.find("td", class_ = "ot-losses").text.strip()
    win_pct = row.find("td", class_ = "pct text-success").text.strip()
    gf = row.find("td", class_ = "gf").text.strip()
    ga = row.find("td", class_ = "ga").text.strip()
    diff = row.find("td", class_ = "diff text-success").text.strip()

    data.append([name, year, wins, losses, ot_losses, win_pct, gf, ga, diff])

print(data)

