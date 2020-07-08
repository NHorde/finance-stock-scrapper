import os
import sys

from bs4 import BeautifulSoup
import requests
import re
from json import loads

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from libs.state import State

def get_html(state: State):
    soup = BeautifulSoup(
        # requests.get("https://finance.yahoo.com/quote/%s/key-statistics?p=%s" % (self.ticker, self.ticker)).content, 'lxml')
        requests.get("https://finance.yahoo.com/quote/%s/key-statistics?p=%s" % ("AMZN", "AMZN")).content, "lxml")
    script = soup.find("script", text=re.compile("root.App.main")).text
    data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
    state.url = data['context']['dispatcher']['stores']
    return crawler_summary(state=state)

def crawler_summary(state: State):
    try:
        state.quote_summary_store = state.url['QuoteSummaryStore']
    except ValueError("No data"):
        state.quote_summary_store = None
    print(state.quote_summary_store)

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

manager(state = state)