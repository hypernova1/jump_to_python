import random


class StockMarket:
    def __init__(self):
        self.price = 400
        self.day = 0
        self.fee = 0.015
        self.stock = Stock()
        self.stock_price_history = []

    def get_stock_price(self, count):
        return self.stock.price + (self.stock.price * count * self.fee)

    def set_stock_price(self):
        self.day += 1
        self.stock.price += random.randint(-200, 200)
        stock_price = StockPrice(self.day, self.price)
        self.stock_price_history.append(stock_price)

    def print_stock_history(self):
        for i in range(len(self.stock_price_history)):
            print(i)


class StockPrice:
    def __init__(self, day, price):
        self.day = day
        self.price = price


class Stock:
    def __init__(self):
        self.price = random.randint(500, 1000)