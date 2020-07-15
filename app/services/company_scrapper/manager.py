import pandas as pd
import os

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)

def manager():
    try:
        url_nasdaq = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
        url_amex = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"
        url_nyse = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
        LOGGER.info("Getting link for download")

        col = ["Symbol", "Name", "MarketCap", "IPOyear", "Sector", "industry"]
        df_nasdaq = pd.read_csv(url_nasdaq, usecols=col)
        df_amex = pd.read_csv(url_amex, usecols=col)
        df_nyse = pd.read_csv(url_nyse, usecols=col)
        LOGGER.info("Reading all .csv files")
        df = pd.concat([df_nasdaq, df_amex, df_nyse])

        PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        df.to_csv(PATH + '/app/data/ticker_list.csv')
    except:
        df = []
    return df

