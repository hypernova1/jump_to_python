from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtCore import *
from config.errorCode import *


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        print("Kiwoom() class start.")

        self.login_event_loop = QEventLoop()
        self.detail_account_info_event_loop = None

        # 계좌 관련 변수
        self.account_num = None  # 계좌번호
        self.deposit = 0  # 예수금
        self.use_money = 0  # 실제 투자에 사용할 금액
        self.use_money_percent = 0.5  # 예수금에서 실제 사용할 비율
        self.output_deposit = 0  # 출력가능금액
        self.total_buy_money = 0  # 실제 구매 금액
        self.total_profit_loss_money = 0  # 총 평가 손익 금액
        self.total_profit_loss_rate = 0.0  # 총 수익률
        self.screen_my_info = "2000"

        self.get_ocx_instance()
        self.event_slots()
        self.signal_login_commConnect()
        self.get_account_info()
        self.detail_account_info()
        self.detail_account_my_stock()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")  # 설치된 API 모듈을 사용할 수 있게하는 함수

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
        self.OnReceiveTrData.connect(self.trdata_slot)

    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()  # 로그인을 요청하는 송/수신이 안전하게 완료될 때 까지 대기

    def login_slot(self, err_code):
        print(errors(err_code)[1])
        self.login_event_loop.exit()  # 로그인이 완료되면 QEventLoop가 종료되고 다음 코드 실행

    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(QString)", "ACCNO")
        account_num = account_list.split(';')[0]

        self.account_num = account_num

        print("계좌번호: %s" % account_num)

    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):
        print(sRQName)
        if sRQName == "예수금상세현황요청":
            deposit = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "예수금")
            self.deposit = int(deposit)

            use_money = float(self.deposit) * self.use_money_percent
            self.use_money = int(use_money)
            self.use_money = self.use_money / 4

            output_deposit = self.dynamicCall("GetCommData(QString, QString, int, QString",
                                              sTrCode, sRQName, 0, "출금가능금액")
            self.output_deposit = int(output_deposit)
            print("예수금: %s" % self.output_deposit)
            self.stop_screen_cancel(self.screen_my_info)

        elif sRQName == "계좌평가잔고내역요청":
            total_buy_money = self.dynamicCall("GetCommData(QString, QString, int, QString)",
                                               sTrCode, sRQName, 0, "총매입금액")
            self.total_buy_money = int(total_buy_money)
            total_profit_loss_money = self.dynamicCall("GetCommData(QString, QString, int, QString)",
                                                       sTrCode, sRQName, 0, "총평가손익금액")
            self.total_profit_loss_money = int(total_profit_loss_money)
            total_profit_loss_rate = self.dynamicCall("GetCommData(QString, QString, int, QString)",
                                                      sTrCode, sRQName, 0, "총수익률")
            self.total_profit_loss_rate = int(total_profit_loss_rate)

            print("계좌평가잔고내역요청 싱글데이터: %s - %s -%s" % (total_buy_money, total_profit_loss_money, total_profit_loss_rate))

            self.stop_screen_cancel(self.screen_my_info)
            self.detail_account_info_event_loop.exit()

    def stop_screen_cancel(self, sScrNo=None):
        self.dynamicCall("DisconnectRealData(QString)", sScrNo)

    def detail_account_info(self, sPrevNext="0"):
        self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_num)
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호", "0000")
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(QString, QString)", "조회구분", "1")
        self.dynamicCall("CommRqData(QString, QString, int, QString)",
                         "예수금상세현황요청", "opw00001", sPrevNext, self.screen_my_info)

    def detail_account_my_stock(self, sPrevNext="0"):
        self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_num)
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호", "0000")
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(QString, QString)", "조회구분", "1")
        self.dynamicCall("CommRqData(QString, QString, int, QString)", "계좌평가잔고내역요청", "opw00018", sPrevNext,
                         self.screen_my_info)

        self.detail_account_info_event_loop = QEventLoop()
        self.detail_account_info_event_loop.exec_()
