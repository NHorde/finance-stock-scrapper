from bs4 import BeautifulSoup
import requests
import re
from json import loads

from state import State

def get_html(state: State):
    soup = BeautifulSoup(
        requests.get("https://finance.yahoo.com/quote/%s/key-statistics?p=%s" % (self.ticker, self.ticker)).content,
        'lxml')
    script = soup.find("script", text=re.compile("root.App.main")).text
    data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
    state.stores = data['context']['dispatcher']['stores']




if __name__ == '__main__':
    ticker = get_html(state = State())