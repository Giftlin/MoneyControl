import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
df = pd.read_csv("files/stock_urls.csv")
new_df = df[df.COMPLETED == "NO"]
new_urls = new_df.URL
for URL in new_urls:
    driver.get(URL)
    html = driver.page_source
    try:
        try:
            val = html.split('data-numberanimate-value="')[1].split('"')[0]
        except Exception:
            try:
                val = html.split('<input id="bsespotval" type="hidden" value="')[
                    1].split('"')[0]
            except Exception:
                val = ""
        try:
            s = html.split("<strong>Strengths (")[1].split(")")[0]
            w = html.split("<strong>Weaknesses (")[1].split(")")[0]
            o = html.split("<strong>Opportunities (")[1].split(")")[0]
            t = html.split("<strong>Threats (")[1].split(")")[0]
        except Exception:
            s, w, o, t = "", "", "", ""
        df.loc[df.URL == URL, 'PRICE'] = val
        df.loc[df.URL == URL, 'STRENGTHS'] = s
        df.loc[df.URL == URL, 'WEAKNESSES'] = w
        df.loc[df.URL == URL, 'OPPORTUNITIES'] = o
        df.loc[df.URL == URL, 'THREATS'] = t
    except Exception:
        pass
    df.loc[df.URL == URL, 'COMPLETED'] = "YES"
    df.to_csv("stock_swot.csv", index=False)
