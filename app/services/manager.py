from services.company.manager import manager as manager_etl
from services.financial.manager import manager as manager_financial_scrapper

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def execute_etl(state: State):
    """
    Call ETL manager script (extract, transform load), logger is included within the company library. This library is downloading the list of all tickers
    that exists in the 3 main exchanges (NASDAQ, NYSE & AMEX) and store them in the /app/data folder. A physical copy is not necessarily required but
    it's always nice to keep a copy in case something happens in the source

    :param state: state
    :return: call ticker financial scrapper
    """
    manager_etl(state=state)
    LOGGER.info(f"ETL completed | Status: {state.events.etl_company_list}")
    return get_ticker_information(state=state)


def get_ticker_information(state: State):
    """
    Call financial scrapper

    :param state: state
    :return: end of the script
    """
    state = manager_financial_scrapper(state = state)

    state.files.test = "test"
    return state


def manager():
    LOGGER.info("Start of the script")
    execute_etl(state = State())

