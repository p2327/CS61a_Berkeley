# Question 1

def make_withdraw(balance, password):
    assert isinstance (password, str), 'Password is a string'
    wrongpw = []
    def withdraw(amount, p):
        nonlocal wrongpw
        nonlocal password
        nonlocal balance
        if p != password:
            wrongpw += [p]
            if len(wrongpw) >= 3: # using f string
                return f'Your account is locked. Attempts: {" ".join(str(x) for x in wrongpw)}'
            return 'Wrong password'
        if p == pw:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
    return withdraw
        
wd = make_withdraw(100, 'mag01f')

wd(10, 'abdci')
wd(10, 'aishie')
wd(10, 'ldfw39u2')

# with unpack helper function
def unpack(s):
    return " ".join(map(str, s))  # using map here to apply join to all args in sequence
    
""" becomes

if password != pw:
            wrongpw += [password]
            if len(wrongpw) >= 3:
                return f'Your account is locked. Attempts: {unpack(wrongpw)}'
            return 'Wrong password'
            """
