from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import EdgeOptions, Edge

try:
  options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
except Exception:
  options = webdriver.FirefoxOptions()
  driver = webdriver.Chrome(GeckoDriverManager().install(), options=options)
  
html = ""
list_page = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "others"]

for element in list_page:
    URL = "https://www.moneycontrol.com/india/stockpricequote/" + element
    driver.get(URL)
    html = html + "        " + driver.page_source

with open("html_stock.txt", "w", encoding="utf-8") as f:
    f.write(html)
