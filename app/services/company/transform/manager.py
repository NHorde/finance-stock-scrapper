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
        state.files.combined_exchanges.columns = map(str.lower, state.files.combined_exchanges.columns)

        # Following line is dropping duplicates but there's not?
        state.output = state.files.combined_exchanges[["symbol", 'name', 'lastsale', 'marketcap', 'ipoyear', 'sector', 'industry']].drop_duplicates()
        state.output.to_csv("test.csv")
        state.events.transform_company_list = 100
        exit(1)
    except Exception as e:
        state.output = None
        LOGGER.warning(f"Could not transform company data , error: {e}")


def manager(state: State):
    filter_unique_ticker(state=state)
