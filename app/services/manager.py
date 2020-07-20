import os
import pandas as pd

from services.financial_scrapper.manager import manager as manager_financial_scrapper
from services.company.extract.manager import manager as manager_company_scrapper
from services.company.load.manager import manager as manager_load

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def download_company_list(state: State):
    try:
        manager_company_scrapper(state=state)
        LOGGER.info("Company list scrapped with success")
    except Except as e:
        LOGGER.warning(f"Company list not successfully scrapped: {e}")
    return load_company_list(state=state)


def load_company_list(state: State):
    try:
        manager_load(state=state)
    except Except as e:
        LOGGER.warning(f"Could not load company list, error: {e}")
    return get_ticker_information(state=state)


def get_ticker_information(state: State):

    state = manager_financial_scrapper(state = state)
    LOGGER.info(f"Status of ticker: {state.status}")
    state.files.test = "test"
    LOGGER.info(f"Checking {state.files.test}")
    return state


def manager():
    LOGGER.info("Start of the script")
    state = State()
    download_company_list(state = state)

