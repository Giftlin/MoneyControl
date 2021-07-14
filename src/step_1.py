from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
options = webdriver.ChromeOptions()

start_time = datetime.now()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
html = ""
list_page = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "others"]

for element in list_page:
    URL = "https://www.moneycontrol.com/india/stockpricequote/" + element
    driver.get(URL)
    html = html + "        " + driver.page_source

with open("html_stock.txt", "w", encoding="utf-8") as f:
    f.write(html)
