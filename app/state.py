from bs4 import BeautifulSoup
import requests
import re
from json import loads


class State:
    _defaults = {
        'ticker': None
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)


