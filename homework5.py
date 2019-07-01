# Question 1

def make_withdraw(balance, password):
    assert isinstance (password, str), 'Password must be a string'
    wrongpw = []
    def withdraw(amount, p):
        nonlocal wrongpw, password, balance
        if p != password:
            wrongpw += [p]
            if len(wrongpw) >= 3: # using f string
                return f'Your account is locked. Attempts: {" ".join(str(x) for x in wrongpw)}'
            return 'Wrong password'
        elif p == pw:
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


# Question 2

def make_withdraw(balance, password):
    assert isinstance (password, str), 'Password is a string'
    wrongpw = []
    # with unpack helper function
    def unpack(s):
        return " ".join(map(str, s))
    def withdraw(amount, p):
        nonlocal wrongpw, password, balance
        if p != password:
            wrongpw += [p]
            if len(wrongpw) >= 3:
                return f'Your account is locked. Attempts: {unpack(wrongpw)}'
            return 'Wrong password'
        elif p == password:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
    return withdraw
        
wd = make_withdraw(10, 'mck32nz1')

""" wd(10, 'abdci')
wd(10, 'aishie')
wd(10, 'ldfw39u2')"""

def make_joint(withdraw, oldpw, newpw):
    account_test = withdraw(0, oldpw) # func stores newpw, oldpw values
    if type(account_test) == str:
        return account_test
    def joint(amount, pw_attempt): # check if pw to withdrwa matches newpw
        if pw_attempt == newpw:
            return withdraw(amount, oldpw) # if true it calls withdrwa on the oldpw, enabling withdrawing
        else:
            return withdraw(amount, pw_attempt) # if not it calls withdraw on a the wrong password
    return joint # returns a function joint


j = make_joint(wd, 'mck32nz1', 'h0lla')

j(10, 'b6g8')
    
