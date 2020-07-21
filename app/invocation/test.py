# import time
# import timeout_decorator
# import pandas as pd

# @timeout_decorator.timeout(5)
# def mytest():
#     print ("Start")
#     for i in range(1,10):
#         time.sleep(1)
#         print ("%d seconds have passed" % i)
#
# if __name__ == '__main__':
#     mytest()

# col = ["Symbol", "Name", "MarketCap", "IPOyear", "Sector", "industry"]
# df = pd.read_csv("https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download", usecols = col)
# print(df.head())

# u = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
# v = "https://dumbstockapi.com/stock?format=csv&countries=US"
# import urllib.request
# urllib.request.urlretrieve (v, "Ktest.csv")


# import requests
#
# url = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
# url2 = "https://www.nasdaq.com/market-activity/stocks/screener?exchange=nasdaq&letter=0&render=download"
# r = requests.get(url2)
# with open('a.csv', 'wb') as f:
#     f.write(r.content)

# NYSE
url_nyse = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
# Nasdaq
url_nasdaq = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
# AMEX
url_amex = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"

import pandas as pd

df = pd.read_csv(url_nyse)
stocks = df.index.tolist()