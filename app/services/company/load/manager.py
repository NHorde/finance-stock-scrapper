from libs.logger import BASE_LOGGER
from libs.state import State

LOGGER = BASE_LOGGER.getChild(__name__)

def read_company_list(state: State):
    try:
        df = urllib.request.urlretrieve(url, path + "/data/ticker_list.csv")
    except Exception as e:
        df = []
        LOGGER.warning(f"URL {url} not working, error: {e}")
    return df
