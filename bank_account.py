class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

        if (self.balance < 0):
            self.overdraft_fees +=36
        return amount  

rome_checking = BankAccount("checking")
print("My new account is a {} account. ".format(rome_checking.kind)) 

rome_checking.deposit(3000)
print("My current balance is ${}.".format(rome_checking.balance))

rome_checking.withdraw(1500)
print("My current balance is ${}.".format(rome_checking.balance))

rome_checking.withdraw(2000)
print("Overdraft {}.".format(rome_checking.overdraft_fees))
print("My current balance is {}.".format(rome_checking.balance))         