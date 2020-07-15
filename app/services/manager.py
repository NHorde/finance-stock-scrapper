import os
import pandas as pd

from services.financial_scrapper.manager import manager as manager_financial_scrapper
from services.company_scrapper.manager import manager as manager_company_scrapper

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)
LOGGER.info("test")

def get_company_list(state: State):
    try:
        manager_company_scrapper()
        print("Company list scrapped with success")
    except:
        print("Company list not successfully scrapped")
    return get_ticker_information(state = state)


def get_ticker_information(state: State):
    # PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    # df = pd.read_csv(PATH + '/app/data/ticker_list.csv')
    # print(df.head())
    state = manager_financial_scrapper(state = state)
    print(state.status)
    return state


def manager():
    state = State()
    get_company_list(state = state)

