import setup

from services.ticker.financial_scrapper.manager import manager
from libs.state import State



state = manager(state = State())
print(state.status)