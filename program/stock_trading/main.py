from entity.stock_market import StockMarket
from entity.ant import Ant

stock_market = StockMarket()

ant = Ant("권샘찬")

i = 1
while 1:
    stock_market.open()
    stock_price = stock_market.stock.price
    print(i, "일째 주식 시장이 열렸습니다. 주식 가격: ", stock_price)
    ant.print_info(stock_price)

    answer = str(input("주식 구매/판매/패스 선택(b/s/p)")).upper()
    if answer == "B":
        buy_count = int(input("구입할 개수 입력: "))
        try:
            ant.buy_stock(buy_count, stock_market.get_stock_price_with_fee())
        except RuntimeError:
            print("금액이 모자라 주식을 구매할 수 없습니다.")
            print("현재 보유한 금액:", ant.account, "원")
            continue
        else:
            print("주식 ", buy_count, "개를 샀습니다.")

    elif answer == "S":
        sell_count = int(input("판매할 개수 입력: "))
        try:
            ant.sell_stock(sell_count, stock_market.get_stock_price_with_fee())
        except RuntimeError:
            print("보유한 주식이 판매할 주식보다 적습니다.")
            print("현재 보유한 주식 개수:", ant.stock_count, "개")
            continue
        else:
            print("주식 ", sell_count, "개를 팔았습니다.")

    elif answer == "P":
        print("패스하셨습니다.")
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")
        continue

    total_assets = stock_price * ant.stock_count + ant.account
    if total_assets > 15000:
        print("부자가 되었습니다. 인생을 즐기세요!")
        break
    if total_assets < 2000:
        print("거지가 되었습니다.. 게임 끝..")
        break
    i += 1
    print("\n")

