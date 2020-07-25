from libs.state import State
from setup import PATH
import pandas as pd

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)


def filter_unique_ticker(state: State):
    """
    Because a ticker can be used in many exchanges, only return list of unique tickers

    :param state:
    :return: Call transform status function
    """
    if state.events.extract_company_list + state.events.load_company_list == 200:
        try:
            state.files.combined_exchanges.columns = map(str.lower, state.files.combined_exchanges.columns)

            # Following line is dropping duplicates but there's not?
            state.output = state.files.combined_exchanges[["symbol", 'name', 'lastsale', 'marketcap', 'ipoyear', 'sector', 'industry']].drop_duplicates()
            state.output.to_csv(f"{PATH}/data/combined_exchanges.csv")
            state.events.transform_company_list = 100
        except Exception as e:
            state.output = None
            LOGGER.warning(f"Could not transform company data , error: {e}")

    else:
        state.output = pd.read_csv(f"{PATH}/data/combined_exchanges.csv")
        LOGGER.warning(f"Using old company ticker file")


def manager(state: State):
    filter_unique_ticker(state=state)