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
        print("현재 계좌 잔고: ", self.account)

    def sell_stock(self, price):
        if 0 > self.stock_count:
            print("보유한 주식의 개수가 0개입니다.")
            return
        self.account += price
        print("주식을 ", price + "에 팔았습니다.")
        print("현재 계좌 잔고: ", self.account)

class StockMarket(object):
    def __init__(self):
        self.day = 0
        self.fee = 0.015
        self.stock = Stock()

    def get_stock_price(self, count):
        return self.stock.price * count * self.fee

    def set_stock_price(self):
        self.stock.price += random.randint(-200, 200)

class Stock(object):
    def __init__(self):
        self.price = random.randint(500, 1000)

stock_market = StockMarket()

ant = Ant("권샘찬")
