
import timeout_decorator
from libs.state import State
from libs.logger import BASE_LOGGER
from setup import PATH

import urllib.request

LOGGER = BASE_LOGGER.getChild(__name__)


timeout_decorator.timeout(10)
def scrap_company_list(url: str, path: str):
    """
    Download the list of all company tickers and store it in the app/data folder

    :param url: string
    :param path: string
    :return:
    """
    try:
        urllib.request.urlretrieve(url, path + "/data/ticker_list.csv")
    except Exception as e:
        LOGGER.warning(f"URL {url} not working, error: {e}")


def extract(state: State):
    """
    Call extract function

    :param state: state
    :return: Status of the extract
    """
    url = "https://dumbstockapi.com/stock?format=csv&countries=US"
    scrap_company_list(url=url, path=PATH)
    return status_extract(state=state)

def status_extract(state: State):
    """
    Return 100 if extract was successful, remain as 400 by default otherwise

    :param state: string
    :return: dataframe
    """
    state.events.extract_company_list = 100


def manager(state: State):
    extract(state=state)