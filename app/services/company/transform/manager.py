from libs.state import State

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)


def filter_unique_ticker(state: State):
    """
    Because a ticker can be used in many exchanges, only return list of unique tickers

    :param state:
    :return: Call transform status function
    """
    try:
        state.output = state.files.company_list[["ticker", 'name']].drop_duplicates()
        state.events.transform_company_list = 100
    except Except as e:
        state.output = None
        LOGGER.warning(f"Could not transform company data , error: {e}")


def manager(state: State):
    filter_unique_ticker(state=state)
