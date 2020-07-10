import pandas as pd
import os

def manager
    url_nasdaq = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
    url_amex = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"
    url_nyse = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"

    col = ["Symbol", "Name", "MarketCap", "IPOyear", "Sector", "industry"]
    df_nasdaq = pd.read_csv(url_nasdaq, usecols=col)
    df_amex = pd.read_csv(url_amex, usecols=col)
    df_nyse = pd.read_csv(url_nyse, usecols=col)

    df = pd.concat([df_nasdaq, df_amex, df_nyse])

    PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    df.to_csv(PATH + '/data/ticker_list.csv')

