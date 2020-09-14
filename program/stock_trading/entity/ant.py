class Ant:
    def __init__(self, name):
        self.name = name
        self.account = 5000
        self.stock_count = 0

    def buy_stock(self, count, price):
        if count * price > self.account:
            raise RuntimeError
        self.account -= price * count
        self.stock_count += count
        print("--------------------------------")
        print("주식을 ", price * count, "원(수수료 포함) 만큼 구매했습니다.")
        print("현재 계좌 잔고: ", self.account)
        print("--------------------------------")

    def sell_stock(self, count, price):
        if self.stock_count - count < 0:
            raise RuntimeError
        self.account += price * count
        self.stock_count -= count
        print("--------------------------------")
        print("주식을 ", price * count, "원에 팔았습니다.")
        print("현재 계좌 잔고: ", self.account)
        print("--------------------------------")

    def get_stock_price(self, price):
        return self.stock_count * price

    def print_info(self, stock_price):
        print("================================")
        print("자산:", self.account)
        print("보유한 주식 개수: ", self.stock_count)
        print("현재 주식 시가:", stock_price * self.stock_count)
        print("================================")
