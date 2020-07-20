from services.company.extract.manager import manager as manager_company_extract
from services.company.load.manager import manager as manager_company_load
from services.company.transform.manager import manager as manager_company_transform

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def extract_company_list(state: State):
    manager_company_extract(state=state)
    LOGGER.info("Company extract completed")
    return load_company_list(state=state)


def load_company_list(state: State):
    manager_company_load(state=state)
    LOGGER.info("Company load completed")
    return transform_company_list(state=state)


def transform_company_list(state: State):
    manager_company_transform(state=state)
    LOGGER.info("Company transform completed")


def manager(state: State):
    extract_company_list(state=state)
