from bs4 import BeautifulSoup
import requests
import re
import json
from json import loads

from libs.state import State


def get_html(state: State):
    soup = BeautifulSoup(requests.get("https://finance.yahoo.com/quote/%s/key-statistics?p=%s" % ("AMZN", "AMZN")).content, "lxml")
    script = soup.find("script", text=re.compile("root.App.main")).text
    data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
    state.url = data['context']['dispatcher']['stores']
    return crawler_quote_summary(state=state)


def crawler_quote_summary(state: State):
    try:
        state.quote_summary_store = state.url['QuoteSummaryStore']
    except ValueError:
        state.quote_summary_store = None
    return crawler_financial_data(state=state)


def crawler_financial_data(state: State):
    try:
        state.financial_data = state.quote_summary_store['financialData']
    except ValueError:
        state.financial_data = None
    return get_current_price(state=state)


def get_current_price(state: State):
    try:
        state.current_price = state.financial_data['currentPrice']['fmt']
    except ValueError:
        state.current_price = None
    return crawler_default_key_statistics(state=state)

def crawler_default_key_statistics(state: State):
    try:
        state.default_key_statistics = state.quote_summary_store['defaultKeyStatistics']
    except ValueError:
        state.default_key_statistics = None
    return get_price_to_book(state=state)

def get_price_to_book(state: State):
    try:
        state.price_to_book = state.default_key_statistics['priceToBook']['fmt']
    except ValueError:
        state.price_to_book = None
    return state


def manager(state: State):
    """
    :param state:
    :type state: State
    :rtype: dict
    :return: object
    """
    try:
        result = get_html(state)
        print("good")
    except:
        result = "nice try"
        print("not good")
    # for item in state.default_key_statistics:
    #     print(item)
    print(state.price_to_book)
    return result
