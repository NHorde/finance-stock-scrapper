import pandas as pd
import os
import timeout_decorator
from libs.state import State
from libs.logger import BASE_LOGGER

import urllib.request

LOGGER = BASE_LOGGER.getChild(__name__)



@timeout_decorator.timeout(10)
def scrap_company_list(url: str, path: str):
    try:
        df = urllib.request.urlretrieve(url, path + "/data/ticker_list.csv")
    except Exception as e:
        df = []
        LOGGER.warning(f"URL {url} not working, error: {e}")
    return df





def extract(state: State):
    url = "https://dumbstockapi.com/stock?format=csv&countries=US"
    PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    scrap_company_list(url=url, path=PATH)
    LOGGER.info("List of all tickers downloaded with success")
    # exit()

    print(PATH)
    df = pd.concat([df_nasdaq, df_amex, df_nyse])
    df.to_csv(PATH + '/app/data/ticker_list.csv')
    # function_appl
    return state


def manager(state: State):
    extract(state=state)