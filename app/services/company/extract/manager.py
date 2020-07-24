
import timeout_decorator
from libs.state import State
from libs.logger import BASE_LOGGER
from setup import PATH

import urllib.request

LOGGER = BASE_LOGGER.getChild(__name__)


@timeout_decorator.timeout(3)
def scrap_company_list(state: State,
                       url: str,
                       path: str,
                       exchange: str):
    """
    Download the list of all company tickers and store it in the app/data folder

    :param state: state
    :param url: string
    :param path: string
    :return:
    """
    try:
        urllib.request.urlretrieve(url, f"{path}/data/{exchange}.csv")
        state.events.extract_company_list = 100
        LOGGER.info(f"{exchange} exchange downloaded with success")
    except Exception as e:
        LOGGER.warning(f"URL {url} not working, error: {e}")


def extract(state: State):
    """
    Call extract function

    :param state: state
    :return: Status of the extract
    """

    exchange_list = ["nasdaq", "nyse", "amex"]

    for exchange in exchange_list:
        scrap_company_list(state = state,
                           url = f"https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange={exchange}&render=download",
                           path = PATH,
                           exchange = exchange)

def manager(state: State):
    extract(state=state)