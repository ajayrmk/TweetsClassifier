# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Create an URL object
url = 'http://www.rsdb.org/full'

# Create object page
page = requests.get(url)

# Obtain page's information
soup = BeautifulSoup(page.text, 'html.parser')

# Obtain information from tag <table>
table1 = soup.find("table")

# Obtain every title of columns with tag <th>
headers = []
for i in table1.find_all("th"):
 title = i.text
 headers.append(title)

# Create a dataframe with headers
data = pd.DataFrame(columns = headers)

# Create a for loop to fill data
for j in table1.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(data)
 data.loc[length] = row
    
# Export .csv file containing the slur words only
data["Slur"].to_csv("slurs.csv", index=False, header=None)



