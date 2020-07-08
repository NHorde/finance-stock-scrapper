import setup

from services.ticker.financial_scrapper.manager import manager
from libs.state import State


state = State()
print(state)
state = manager(state = state)
print(state.current_price)
