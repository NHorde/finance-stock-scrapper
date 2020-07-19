import pandas as pd
import os
import timeout_decorator
from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


@timeout_decorator.timeout(10)
def scrap_company_list(url: str, col: list):
    try:
        df = pd.read_csv(url, usecols=col)
    except Exception as e:
        df = []
        LOGGER.info(f"Ticker {url} not working, error: {e}")
    return df

def manager(state: State):

    url_nasdaq = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
    url_amex = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"
    url_nyse = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
    col = ["Symbol", "Name", "MarketCap", "IPOyear", "Sector", "industry"]


    state.files.nasdaq = scrap_company_list(url= url_nasdaq, col = col)
    state.files.amex = scrap_company_list(url=url_amex, col=col)
    state.files.nyse = scrap_company_list(url=url_nyse, col=col)
    LOGGER.info("Reading all .csv files")
    # exit()
    # df_amex = pd.read_csv(url_amex, usecols=col)
    # df_nyse = pd.read_csv(url_nyse, usecols=col)
    # PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    # df.to_csv(PATH + '/app/data/ticker_list.csv')
    # df = pd.concat([df_nasdaq, df_amex, df_nyse])

    # function_appl
    return state