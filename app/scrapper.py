from bs4 import BeautifulSoup
import requests
import re
from json import loads


class Ticker:
    _defaults = {
        'ticker': None
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
        self.stores = None

    def get_html(self):
        soup = BeautifulSoup(
            requests.get("https://finance.yahoo.com/quote/%s/key-statistics?p=%s" % (self.ticker, self.ticker)).content,
            'lxml')
        script = soup.find("script", text=re.compile("root.App.main")).text
        data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
        self.stores = data['context']['dispatcher']['stores']


src = Ticker(ticker='HD')
src.get_html()
src.stores


parse = src.stores

print(parse)