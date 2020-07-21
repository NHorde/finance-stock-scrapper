
import timeout_decorator
from libs.state import State
from libs.logger import BASE_LOGGER
from setup import PATH

import urllib.request

LOGGER = BASE_LOGGER.getChild(__name__)


timeout_decorator.timeout(10)
def scrap_company_list(state: State,
                       url: str,
                       path: str):
    """
    Download the list of all company tickers and store it in the app/data folder

    :param state: state
    :param url: string
    :param path: string
    :return:
    """
    try:
        urllib.request.urlretrieve(url, path + "/data/ticker_list.csv")
        state.events.extract_company_list = 100
    except Exception as e:
        LOGGER.warning(f"URL {url} not working, error: {e}")


def extract(state: State):
    """
    Call extract function

    :param state: state
    :return: Status of the extract
    """
    url = "https://dumbstockapi.com/stock?format=csv&countries=US"
    scrap_company_list(state = state, url=url, path=PATH)


def manager(state: State):
    extract(state=state)