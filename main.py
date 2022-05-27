import services as sc
import yfinance as yf
import pandas as pd
from yahoo_fin.stock_info import get_analysts_info

config_price = 5
config_market_cap = 10
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)

print(tickerData.info)
