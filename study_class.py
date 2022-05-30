from base_services import BaseService

bs = BaseService('tsla')

symbolList = bs.get_symbols_us()
for symbol in symbolList:
    print(symbol)
# analytic = bs.getStockAnalytic()
# print(bs)
# analytic = bs.get_stock_analytic()
# print(analytic)




