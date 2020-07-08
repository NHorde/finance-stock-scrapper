import os
import sys

from bs4 import BeautifulSoup
import requests
import re
import json
from json import loads

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

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
        state.current_price = state.financial_data['currentPrice']['raw']
    except ValueError:
        state.current_price = None
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
    print(result)
    return result


state = State()
state = manager(state = state)
print(state.current_price)
# for name in state.financial_data:
#     print(name)
# print(json.dumps(state.financial_data, indent=3, default=str))