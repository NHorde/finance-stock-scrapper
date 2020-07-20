from services.company.manager import manager as manager_etl
from services.financial.manager import manager as manager_financial_scrapper

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def execute_etl(state: State):
    manager_etl(state=state)
    LOGGER.info(f"ETL completed | Status: {state.events.etl_company_list}")
    return get_ticker_information(state=state)


def get_ticker_information(state: State):
    state = manager_financial_scrapper(state = state)
    LOGGER.info(f"Status of ticker: {state.status}")
    state.files.test = "test"
    LOGGER.info(f"Checking {state.files.test}")
    return state


def manager():
    LOGGER.info("Start of the script")
    execute_etl(state = State())

