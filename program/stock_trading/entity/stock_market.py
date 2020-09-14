import random
import math


class StockMarket:
    def __init__(self):
        self.day = 0
        self.fee = 0.015
        self.stock = Stock()
        self.stock_price_history = []

    def get_stock_price_with_fee(self):
        return math.trunc(self.stock.price + (self.stock.price * self.fee))

    def open(self):
        self.day += 1
        self.stock.price += random.randint(-200, 200)
        stock_price = StockPrice(self.day, self.stock.price)
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
