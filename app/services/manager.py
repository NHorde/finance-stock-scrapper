import os
import pandas as pd

from services.financial_scrapper.manager import manager as manager_financial_scrapper
from services.company_scrapper.manager import manager as manager_company_scrapper

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def get_company_list(state: State):
    LOGGER.info("Beginning of company list scrap")
    try:
        LOGGER.info("Downloading company list")
        # manager_company_scrapper()
        LOGGER.info("Company list scrapped with success")
    except:
        LOGGER.info("Company list not successfully scrapped")

    return get_ticker_information(state = state)


def get_ticker_information(state: State):

    state = manager_financial_scrapper(state = state)
    LOGGER.info(f"Status of ticker: {state.status}")
    return state


def manager():
    LOGGER.info("Start of the script")
    state = State()
    get_company_list(state = state)

