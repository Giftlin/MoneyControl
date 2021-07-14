from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import os

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Giftlin Nowfal\\OneDrive\\Documents\\chromedriver.exe")
df = pd.read_csv("stock_urls.csv")
new_df = df[df.COMPLETED=="NO"]
new_urls = new_df.URL
for URL in new_urls:
    driver.get(URL)
    html = driver.page_source
    try:
        val = html.split('data-numberanimate-value="')[1].split('"')[0]
        df.loc[df.URL == URL, 'PRICE'] = val
        s = html.split("<strong>Strengths (")[1].split(")")[0]
        df.loc[df.URL == URL, 'STRENGTHS'] = s
        w = html.split("<strong>Weaknesses (")[1].split(")")[0]
        df.loc[df.URL == URL, 'WEAKNESSES'] = w
        o = html.split("<strong>Opportunities (")[1].split(")")[0]
        df.loc[df.URL == URL, 'OPPORTUNITIES'] = o
        t = html.split("<strong>Threats (")[1].split(")")[0]
        df.loc[df.URL == URL, 'THREATS'] = t
    except Exception:
        pass
    df.loc[df.URL == URL, 'COMPLETED'] = "YES"
    df.to_csv("stock_swot.csv", index=False)
