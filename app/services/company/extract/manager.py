import pandas as pd
import os
import timeout_decorator
from libs.state import State
from libs.logger import BASE_LOGGER

import urllib.request

LOGGER = BASE_LOGGER.getChild(__name__)

urllib.request.urlretrieve (v, "Ktest.csv")

@timeout_decorator.timeout(5)
def scrap_company_list(url: str, col: list):
    try:
        df = pd.read_csv(url, usecols=col)
    except Exception as e:
        df = []
        LOGGER.warning(f"URL {url} not working, error: {e}")
    return df





def extract(state: State):

    url_nasdaq = "https://dumbstockapi.com/stock?format=csv&countries=US"
    col = ["Symbol", "Name", "MarketCap", "IPOyear", "Sector", "industry"]

    state.files.nasdaq = scrap_company_list(url= url_nasdaq, col = col)
    state.files.amex = scrap_company_list(url=url_amex, col=col)
    state.files.nyse = scrap_company_list(url=url_nyse, col=col)
    LOGGER.info("Reading all .csv files")
    # exit()
    df_amex = pd.read_csv(url_amex, usecols=col)
    df_nyse = pd.read_csv(url_nyse, usecols=col)
    PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    df = pd.concat([df_nasdaq, df_amex, df_nyse])
    df.to_csv(PATH + '/app/data/ticker_list.csv')
    # function_appl
    return state


def manager(state: State):
    extract(state=state)