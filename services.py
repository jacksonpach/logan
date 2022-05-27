import pandas as pd
from yahoo_fin import stock_info as si
import yfinance as yf

def get_symbols_br():
    df = pd.DataFrame(si.tickers_ibovespa())
    return set(symbol for symbol in df[0].values.tolist())


def get_symbols_sp500():
    df = pd.DataFrame(si.tickers_sp500())
    return set(symbol for symbol in df[0].values.tolist())


async def get_data_info():
    stock = 'ALB'
    # tickerData = yf.Ticker(stock)
    # df = pd.DataFrame([tickerData.info])
    return stock


def get_fundamental_values(stocks_symbol):
    for symbol in stocks_symbol:
        return print(symbol)
