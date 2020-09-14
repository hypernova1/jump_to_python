class Ant:
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
