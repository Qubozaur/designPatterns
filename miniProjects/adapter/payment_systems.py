class oldMoneyFlow:
    def makePayment(self, value):
        if isinstance(value, int) and value >= 0:
            print(f"[OLD] Payment {value} $")


class newSuperCash:
    def makePayment(self, value: int):
        if isinstance(value, int) and value >= 0:
            print(f"[NEW] Payment {value} $")

