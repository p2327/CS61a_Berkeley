""" The dispatch function is a general method for implementing a message passing interface for abstract data. 
To implement message dispatch, we have thus far used conditional statements to compare the message string to a fixed 
set of known messages.

The built-in dictionary data type provides a general method for looking up a value for a key. Instead of using 
conditionals to implement dispatching, we can use dictionaries with string keys.

The mutable account data type below is implemented as a dictionary. It has a constructor account and selector
check_balance, as well as functions to deposit or withdraw funds. Moreover, the local state of the account is 
stored in the dictionary alongside the functions that implement its behavior."""

# By storing the balance in the dispatch dictionary rather than in the account frame directly, 
# we avoid the need for nonlocal statements in deposit and withdraw.

def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit':   deposit,
                'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']

John = account(20)
Jade = account(450)
deposit(John, 5)
withdraw(Jade, 17)
withdraw(John, 15)

check_balance(John)
check_balance(Jade)
