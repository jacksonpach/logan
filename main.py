import services as sc
import yfinance as yf
import pandas as pd
from yahoo_fin.stock_info import get_analysts_info

config_price = 5
config_market_cap = 10
stocks_symbol = sc.get_symbols_br()

# Pegar as informações
stock = 'CAAP'

# get data on this ticker
tickerData = yf.Ticker(stock)
print(tickerData.info)

df = pd.DataFrame([tickerData.info])

# 1º Preço maior que R$ 5,0
if df.currentPrice > config_price:
    # market cap
    market_cap = df.marketCap / 10000000000
    market_cap = round(market_cap)
    # if market_cap > config_market_cap:
    #     relative_volume = df.volume / df.averageVolume10days
    #     print(relative_volume)

else:
    print('Preço abaixo de R$ 5,0')
