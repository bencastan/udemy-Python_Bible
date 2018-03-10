class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
            self.balance += amount

    def withdrawal(self, amount):
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
            else:
                print("Sorry not enough funds!")

    def statement(self):
            print("Account balance:$ {}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account : Balance ${}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings Account : Balance ${}".format(self.name, self.balance)


x = Current("Ben", 250)
print(x)
x.deposit(1001)
print(x)
x.withdrawal(8000)
print(x)
x.withdrawal(800)
print(x)

y = Savings("Benc", 1000)
print(y)
