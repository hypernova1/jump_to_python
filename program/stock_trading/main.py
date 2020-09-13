import random

class Ant(object):
    def __init__(self, name):
        self.name = name
        self.account = 5000
        self.stock_count = 0

    def buy_stock(self, price):
        if price > self.account:
            print("금액이 모자라 주식을 구매할 수 없습니다.")
            return
        self.account -= price
        print("주식을 ", price + "원 만큼 구매했습니다.")
        print("현재 계좌 잔고: ", self.account)

    def sell_stock(self, price):
        if 0 > self.stock_count:
            print("보유한 주식의 개수가 0개입니다.")
            return
        self.account += price
        print("주식을 ", price + "원에 팔았습니다.")
        print("현재 계좌 잔고: ", self.account)

class StockMarket(object):
    def __init__(self):
        self.day = 0
        self.fee = 0.015
        self.stock = Stock()
        self.stock_price_history = []

    def get_stock_price(self, count):
        return self.stock.price * count * self.fee

    def set_stock_price(self):
        self.day += 1
        self.stock.price += random.randint(-200, 200)
        self.set_stock_price()

    def set_stock_price_history(self):
        stock_price = StockPrice(self.day, self.price)
        self.stock_price_history.append(stock_price)

class StockPrice(object):
    def __init__(self, day, price):
        self.day = day
        self.price = price

class Stock(object):
    def __init__(self):
        self.price = random.randint(500, 1000)

stock_market = StockMarket()

ant = Ant("권샘찬")
