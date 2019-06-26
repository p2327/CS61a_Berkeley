class Account:
    interest = 0.04
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
            
kirk_acc = Account('Kirk')


spock_acc = Account('Spock')
spock_acc.balance = 200

accounts = (kirk_acc, spock_acc)
[acc.balance for acc in accounts]

kirk_acc.interest = 0.5

Account.interest = 0.3

print(spock_acc.interest)

Account.deposit(spock_acc, 150)

print(kirk_acc.interest)
