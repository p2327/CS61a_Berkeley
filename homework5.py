# Question 1

def make_withdraw(balance, pw):
    assert isinstance (pw, str), 'Password is a string' # https://stackoverflow.com/questions/2589522/proper-way-to-assert-type-of-variable-in-python
    def withdraw(amount, password):
        nonlocal pw
        nonlocal balance
        if password != pw:
            return 'Wrong password'
        if password == pw:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
    return withdraw
