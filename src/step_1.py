from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

try:
  options = webdriver.ChromeOptions()
  options.add_argument("start-maximized")
  options.add_argument("--headless")
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
except Exception:
  pass
  
html = ""
list_page = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "others"]

for element in list_page:
    URL = "https://www.moneycontrol.com/india/stockpricequote/" + element
    driver.get(URL)
    html = html + "        " + driver.page_source
    
lst = html.split("</a>")
lst = [x.split('href="')[1]
       for x in lst if "https://www.moneycontrol.com/india/stockpricequote/" in x]
lst_url = [x.split('"')[0] for x in lst]
lst_name = [x.split(">")[-1] if len(x.split('" title="')) < 2 else x.split(
    '" title="')[1].split('"')[0] for x in lst]
print(len(lst))
print(lst)
print(lst_name)


list_page = ["","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", '<link rel="stylesheet" ',
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "OTHERS", "Others", '<link rel="stylesheet"', "", "Login", """
 < link """, """
 <link """]

df = pd.DataFrame({"NAME": lst_name, "URL": lst_url})
df = df.drop_duplicates("URL")
df = df[~df.NAME.isin(list_page)]
print(df)
df["PRICE"] = ""
df["STRENGTHS"] = ""
df["WEAKNESSES"] = ""
df["OPPORTUNITIES"] = ""
df["THREATS"] = ""
df["COMPLETED"] = "NO"
df.to_csv("stock_urls.csv", index=False)
