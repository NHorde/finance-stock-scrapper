from libs.state import State

from libs.logger import BASE_LOGGER
LOGGER = BASE_LOGGER.getChild(__name__)


def filter_unique_ticker(state: State):
    state.output = state.files.company_list[["ticker", 'name']].drop_duplicates()
    return status_transform(state=state)


def status_transform(state: State):
    state.events.transform_company_list = 100


def manager(state: State):
    filter_unique_ticker(state=state)
