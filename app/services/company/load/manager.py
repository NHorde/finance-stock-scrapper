from libs.state import State
from setup import PATH

import pandas as pd

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)

def read_company_list(state: State):
    """
    Load function that is read after extract, read .csv in app/data folder

    :param state: state
    :return: call load status function
    """
    try:
        state.files.company_list = pd.read_csv(PATH + "/data/ticker_list.csv")
        state.events.load_company_list = 100
    except Exception as e:
        state.files.company_list = None
        LOGGER.warning(f"No company data loader, error: {e}")


def manager(state: State):
    read_company_list(state=state)
