from services.company.extract.manager import manager as manager_company_extract
from services.company.load.manager import manager as manager_company_load
from services.company.transform.manager import manager as manager_company_transform

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def extract_company_list(state: State):
    """
    Call extract manager script

    :param state:
    :return: call load manager script
    """
    manager_company_extract(state=state)
    LOGGER.info(f"Company extract completed | Status: {state.events.extract_company_list}")
    return load_company_list(state=state)


def load_company_list(state: State):
    """
    Call load manager script

    :param state:
    :return: call transform manager script
    """
    manager_company_load(state=state)
    LOGGER.info(f"Company load completed | Status: {state.events.load_company_list}")
    return transform_company_list(state=state)


def transform_company_list(state: State):
    """
    Call transform manager script

    :param state:
    :return: call ETL status function
    """
    manager_company_transform(state=state)
    LOGGER.info(f"Company transform completed | Status: {state.events.transform_company_list}")
    return etl_status(state=state)


def etl_status(state: State):
    if state.events.extract_company_list + state.events.load_company_list + state.events.transform_company_list == 300:
        state.events.etl_company_list = 100


def manager(state: State):
    extract_company_list(state=state)
