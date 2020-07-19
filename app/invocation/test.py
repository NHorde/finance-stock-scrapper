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
v = "https://dumbstockapi.com/stock?format=csv&countries=US"
import urllib.request
urllib.request.urlretrieve (v, "Ktest.csv")