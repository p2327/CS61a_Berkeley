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
    if type(account_test) == str: # checks that oldpw is valid (it returned a balance) otherwise we have a string, i.e. error from make_withdraw like 'Insufficient funds'
    def joint(amount, pw_attempt): 
        if pw_attempt == newpw: # check if pw used to withdrwa matches newpw
            return withdraw(amount, oldpw) # if true it calls withdrwa on the oldpw, enabling withdrawing
        else:
            return withdraw(amount, pw_attempt) # if not it calls withdraw on a the wrong password
    return joint # returns a function joint


j = make_joint(wd, 'mck32nz1', 'h0lla')

j(10, 'b6g8')
    
##############
###CLASSES####
##############

# Q1

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, vend_stock, candy_type, candy_price):
        self.balance = 0
        self.stock = vend_stock
        self.candy = candy_type
        self.price = candy_price
    
    def vend(self):
        change = self.balance - self.price
        def check(res):
            if self.balance == 0:
                return f'You must deposit ${self.price}'
            elif res == 'yes':
                return f"Here's your candy. Balance: ${self.balance}"
            else:
                self.balance = 0
                return f"Here's your candy and ${change} change"
        if self.stock == 0:
            return 'Machine out of stock'
        else:
            if self.balance < 10:
                return f'You must deposit ${10-self.balance} more'
            elif change >= 0:
                self.stock -= 1
                self.balance -= self.price
                if self.balance < 0:
                    self.balance = 0
                ans = input('Buy more?: yes/no')
                return check(ans)
    
    def deposit(self, amount):
        if self.stock == 0:
            return f"Out of stock. Here's your ${amount}"
        self.balance += amount
        return f'Current balance: ${self.balance}'
    
    def restock(self, quantity):
        self.stock += quantity
        return f'Current {self.candy} stock: {self.stock}'
    

mm = VendingMachine(3, 'Mars bars', 10)
