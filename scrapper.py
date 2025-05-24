import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_Africa_by_revenue"
r = requests.get(url)
print(r.status_code)  
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_Africa_by_revenue"
r = requests.get(url)
print(r.text)  # Add this line to display the HTML content
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())  # Print the prettified HTML content
table = soup.find_all("table")[1]
soup.find('table', class_= "wikitable sortable")
table.find_all("th")
africa_titles = table.find_all("th")
print(africa_titles)
africa_titles = [title.text.strip() for title in africa_titles]
print(africa_titles)
import pandas as pd
df = pd.DataFrame(columns = africa_titles)
print(df)
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    if len(columns) == len(africa_titles):
        data = [col.text.strip() for col in columns]
        df.loc[len(df)] = data
print(df)
df.to_csv("africa_companies.csv", index=False)