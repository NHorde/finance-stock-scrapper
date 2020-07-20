from libs.state import State
from setup import PATH

import pandas as pd

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)

def read_company_list(state: State):
    try:
        state.files.company_list = pd.read_csv(PATH + "/data/ticker_list.csv")
    except Exception as e:
        state.files.company_list = None
        LOGGER.warning(f"No company data loader, error: {e}")
    return status_read_company_list(state=state)

def status_read_company_list(state: State):
    state.events.load_company_list = 100

def manager(state: State):
    read_company_list(state=state)
