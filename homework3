"""A mathematical function G on positive integers is defined by two cases:

G(n) = n,  if n <= 3
G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3

e.g. g(4) = g(3) + 2g(2) + 3g(1)

3 + 2*2 + 3*1 = 10 

g(5) = g(4) + 2g(3) + 3g(2)

g(6) = g(5) + 2g(4) + 3g(3)


Write a recursive function g that computes G(n). 
Then, write an iterative function g_iter that also computes G(n):"""


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)
        
test = g(5)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3

    p1, p2, p3 = 3, 2, 1
    i, current = 4, 0
    while i <= n:
        current = p1 + 2 * p2 + 3 * p3
        p1, p2, p3 = current, p1, p2
        i += 1

    return current
        


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)



ppseq = "1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
        # Following is a tree-recursion (2-way) version,
    # which takes too much time when n is large.
    #
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # elif (n - 1) % 7 == 0 or has_seven(n - 1):
    #     return pingpong(n - 2)
    # else:
    #     return 2 * pingpong(n - 1) - pingpong(n - 2)

    # So re-implement a from-bottom-to-top recursion, using a helper fuction.
    def helper(k, direction, ret):
        if k == n:
            return ret + direction
        elif k % 7 == 0 or has_seven(k):
            return helper(k + 1, -direction, ret + direction)
        else:
            return helper(k + 1, direction, ret + direction)

    return helper(1, 1, 0)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"



def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count_digit(digit, number):
        if number < 10 and number == digit:
            return 1
        elif number < 10 and number != digit:
            return 0
        elif number % 10 == digit:
            return 1 + count_digit(digit, number // 10)
        else:
            return count_digit(digit, number // 10)

    def helper(n):
        if n < 10:
            return 0
        else:
            return count_digit(10 - n % 10, n // 10) + helper(n // 10)

    return helper(n)



def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'
