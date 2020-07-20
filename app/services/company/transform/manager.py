from libs.state import State
from setup import PATH

import pandas as pd

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)

def filter_unique_ticker(state: State):
    state.output = state.files.company_list[["ticker", 'name']].drop_duplicates()



def manager(state : State):
    filter_unique_ticker(state=state)
