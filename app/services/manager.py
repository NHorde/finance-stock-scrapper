import setup

from services.financial_scrapper.manager import manager as manager_financial_scrapper
from services.company_scrapper.manager import manager as manager_company_scrapper

from libs.state import State


manager_company_scrapper()
state = manager_financial_scrapper(state = State())
print(state.status)