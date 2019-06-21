"""
Alyssa P. Hacker is designing a system 
to help people solve engineering problems. 
One feature she wants to provide in her system is the ability
to manipulate inexact quantities (such as measured parameters 
of physical devices) with known precision, 
so that when computations are done with such approximate
quantities the results will be numbers of known precision.

Alyssa's idea is to implement interval arithmetic as 
a set of arithmetic operations for combining "intervals" 
(objects that represent the range of possible values 
of an inexact quantity). The result of adding, 
subracting, multiplying, or dividing two intervals 
is itself an interval, representing the range of the result.

Alyssa postulates the existence of an abstract object called 
an "interval" that has two endpoints: 
a lower bound and an upper bound. She also presumes that, 
given the endpoints of an interval, she can construct 
the interval using the data constructor interval. 
Using the constructor and selectors, she defines the 
following operations:
"""


def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


##########################
########ASSIGNMENT########
##########################
"""
Alyssa's program is incomplete 
because she has not specified the 
implementation of the interval abstraction. 
Define the constructor and selectors in terms of two-element 
lists:"""


"""
def interval_b(a, b):
    assert type(b) == list, 'b must be a list'
    for num in b:
        return [a] + [i for i in range(a+1, b[-1]+1)]
"""        
        
def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return [a] + [i for i in range(a+1, b+1)]
        

test_i = interval(1, 3)

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

lo_bound = lower_bound(test_i)

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[-1]

up_bound = upper_bound(test_i)





