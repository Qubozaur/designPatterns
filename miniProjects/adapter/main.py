from payment_systems import oldMoneyFlow, newSuperCash
from adapters import oldPayAdapter, newPayAdapter

def perform_payment(payment_method, amount):
    payment_method.pay(amount)

def main():
    oldpay = oldPayAdapter(oldMoneyFlow())
    superpay = newPayAdapter(newSuperCash())




    perform_payment(oldpay, 50)
    perform_payment(superpay, 75)


if __name__ == "__main__":
    main()