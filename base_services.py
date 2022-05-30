import pandas as pd
from yahoo_fin import stock_info as si
from finvizfinance.quote import finvizfinance
from datetime import datetime, timedelta
import config as c


class BaseService:

    def __init__(self):

    def get_symbols_us(self):
        self.df = pd.DataFrame(si.tickers_sp500())
        return set(symbol for symbol in self.df[0].values.tolist())

    def get_stock_analytic(self, asset):

        self.stock = finvizfinance(asset)
        self.stock_finviz_fundament = self.stock.ticker_fundament()
        self.df = pd.DataFrame([self.stock_finviz_fundament])

        current_price = float(self.df['Price'][0])
        market_cap = float((self.df['Market Cap'][0][:-1]))
        relative_volume = float(self.df['Rel Volume'][0])
        volatility_week = float(self.df['Volatility W'][0][:-1])

        if 'Price' in self.df.columns:
            if current_price > c.config_price:
                if market_cap > c.config_market_cap:
                    if relative_volume > 1:
                        if volatility_week >= 3:
                            return print('Stocks available for swing trade: ')
                else:
                    return print('not sufficient market_cap')
            else:
                return print('not sufficient current price')
        else:
            return print('not sufficient columns currentPrice')
