from services.financial_scrapper.manager import manager as manager_financial_scrapper
from services.company_scrapper.manager import manager as manager_company_scrapper

from libs.state import State

def get_company_list(state: State):
    try:
        manager_company_scrapper()
        print("Company list scrapped with success")
    except:
        print("Company list not successfully scrapped")
    return get_ticker_test(state = state)


def get_ticker_test(state: State):
    state = manager_financial_scrapper(state =state)
    print(state.status)
    return state

def manager():
    state = State()
    get_company_list(state = state)

