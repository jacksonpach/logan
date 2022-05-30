import pandas as pd
from yahoo_fin import stock_info as si
import yfinance as yf
import config as c


def get_symbols_br():
    df = pd.DataFrame(si.tickers_ibovespa())
    return set(symbol for symbol in df[0].values.tolist())


def get_symbols_sp500():
    df = pd.DataFrame(si.tickers_sp500())
    return set(symbol for symbol in df[0].values.tolist())


def get_test():
    return 'Test'


    # current_price = float(df['Price'][0])
    # market_cap = float((df['Market Cap'][0][:-1]))
    # relative_volume = float(df['Rel Volume'][0])
    # volatility_week = float(df['Volatility W'][0][:-1])
    #
    # if 'Price' in df.columns:
    #     if current_price > c.config_price:
    #         if market_cap > c.config_market_cap:
    #             if relative_volume > 1:
    #                 if volatility_week >= 3:
    #                     return print('Stocks available swing trade: ')
    #         else:
    #             return print('not sufficient market_cap')
    #     else:
    #         return print('not sufficient current price')
    # else:
    #     return print('not sufficient columns currentPrice')


