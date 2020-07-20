from libs.state import State
from setup import PATH

import pandas as pd

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)

def read_company_list(state: State):
    try:
        df = pd.read_csv
    except Exception as e:
        df = []
        LOGGER.warning(f"URL {url} not working, error: {e}")
    return df
