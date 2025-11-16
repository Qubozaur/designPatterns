class account:
    def __init__(self,name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number
        self.cash = 0

    def deposit(self, amount):
        self.cash += amount

    def withdraw(self, amount):
        if amount > self.cash:
            print("You can't witdraw more than you have on account")

