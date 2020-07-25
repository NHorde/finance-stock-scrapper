from services.company.manager import manager as manager_etl
from services.financial.manager import manager as manager_financial_scrapper
from setup import PATH

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def execute_etl(state: State):
    """
    Call ETL manager script (extract, transform load), logger is included within the company library. This library is downloading the list of all tickers
    that exists in the 3 main exchanges (NASDAQ, NYSE & AMEX) and store them in the /app/data folder. A physical copy is not necessarily required but
    it's always nice to keep a copy in case something happens in the source

    :param state: state
    :return: call ticker financial scrapper
    """
    manager_etl(state=state)
    LOGGER.info(f"ETL completed | Status: {state.events.etl_company_list}")
    return get_ticker_information(state=state)


def get_ticker_information(state: State):
    """
    Call financial scrapper

    :param state: state
    :return: end of the script
    """
    # state.output["current_price"] = None
    # state.output[state.output['symbol'] == "BCOW"]["current_price"] = 3
    # print(state.output[state.output['symbol'] == "BCOW"])
    #
    # exit(1)
    for index, row in state.output.iterrows():
        symbol = row["symbol"]
        manager_financial_scrapper(state=state, symbol=symbol)
        try:
            state.output.at[index, 'current_price'] = state.ticker.current_price
            delattr(state.ticker, "current_price")
        except:
            pass
        try:
            state.output.at[index, 'current_price_to_book'] = state.ticker.current_price_to_book
            delattr(state.ticker, "current_price_to_book")
        except:
            pass
        try:
            state.output.at[index, 'current_price_to_book_date'] = state.ticker.current_price_to_book_date
            delattr(state.ticker, "current_price_to_book_date")
        except:
            pass
        try:
            state.output.at[index, 'price_to_book_q1'] = state.ticker.price_to_book_q1
            delattr(state.ticker, "price_to_book_q1")
        except:
            pass
        try:
            state.output.at[index, 'price_to_book_q2'] = state.ticker.price_to_book_q2
            delattr(state.ticker, "price_to_book_q2")
        except:
            pass
        try:
            state.output.at[index, 'price_to_book_q3'] = state.ticker.price_to_book_q3
            delattr(state.ticker, "price_to_book_q3")
        except:
            pass
        try:
            state.output.at[index, 'price_to_book_q4'] = state.ticker.price_to_book_q4
            delattr(state.ticker, "price_to_book_q4")
        except:
            pass
    # for attribut in vars(state.ticker):
    #         delattr(state.ticker, attribut)

    state.output.to_csv(f"{PATH}/data/output.csv")

    return state


def manager():
    LOGGER.info("Start of the script")
    execute_etl(state = State())

