class paymentInterface:
    def pay(self, amount):
        raise NotImplementedError

class oldPayAdapter(paymentInterface):
    def __init__(self, old_api):
        self.old_api = old_api

    def pay(self, amount):
        self.old_api.makePayment(amount)


class newPayAdapter(paymentInterface):
    def __init__(self, new_api):
        self.new_api = new_api

    def pay(self, amount):
        self.new_api.makePayment(amount)