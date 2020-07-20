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
    return status_extract(state=state)

def status_extract(state: State):
    state.events.download_company_list = 100

def manager(state: State):
    extract(state=state)