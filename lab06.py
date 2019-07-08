class Person(object):
    species = 'Human'
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.repeat() # starts at whatever value you'd like
    'I squirreled it away before it could catch on fire.'
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __repr__(self):
        return f'{self.name} is a person'
    
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.previous = []

    def say(self, stuff):
        self.previous += [stuff]
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        if self.previous:
            return str(self.previous[-1])
        return 'I said nothing'
        
    def start_again(self):
        full = ' '.join([self.previous[i] for i in range(len(self.previous))])
        return full

    
    
class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.txs = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.balance = self.balance + amount
        self.txs += ('deposit', amount)
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.txs += ('withdraw', amount)
        return self.balance
    
    @property # let a zero call method behave like an attribute
    def transactions(self):
        return self.txs
