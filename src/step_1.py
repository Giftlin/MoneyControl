from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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

with open("./files/html_stock.txt", "w", encoding="utf-8") as f:
    f.write(html)
