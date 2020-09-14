from entity.stock_market import StockMarket
from entity.ant import Ant

stock_market = StockMarket()

ant = Ant("권샘찬")

stock_market.set_stock_price()
stock_market.get_stock_price(1)

stock_market.print_stock_history()
