from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_India")
soup = BeautifulSoup(page.text, "html")

# print(soup)
table = soup.find_all("table")[0]
# print(table)
india_title = table.find_all("th")
#print(india_title)
india_titles_table = [title.text.strip() for title in india_title]
print(india_titles_table)

df = pd.DataFrame(columns=india_titles_table)

# print(df)

table_data = table.find_all("tr")

for row in table_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    # print(individual_row_data)

    length=len(df)
    df.loc[length]= individual_row_data
print(df)
df.to_excel("output.xlsx", index=False)