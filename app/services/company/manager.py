from services.company.extract.manager import manager as manager_company_scrapper
from services.company.load.manager import manager as manager_load
from services.company.transform.manager import manager as manager_transform

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def extract_company_list(state: State):
    try:
        manager_company_scrapper(state=state)
        LOGGER.info("Company list scrapped with success")
    except Except as e:
        LOGGER.warning(f"Company list not successfully scrapped: {e}")
    return load_company_list(state=state)


def load_company_list(state: State):
    try:
        manager_load(state=state)
    except Except as e:
        LOGGER.warning(f"Could not load company list, error: {e}")
    return transform_company_list(state=state)


def transform_company_list(state: State):
    manager_transform(state=state)
    return get_ticker_information(state=state)

def manager(state: State):
