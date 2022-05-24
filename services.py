import pandas as pd
from yahoo_fin import stock_info as si


def get_symbols_br():
    df = pd.DataFrame(si.tickers_ibovespa())
    return set(symbol for symbol in df[0].values.tolist())

def get_fundamental_values(stocks_symbol):
    for symbol in stocks_symbol:
        return print(symbol)