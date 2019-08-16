import numpy 

def sieve(n, k):
    """Returns the k-th prime number starting from n.
    
    >>> sieve(5, 10001)
    104743
    
    """
    flags = numpy.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        if flags[i]:
            flags[i*i::i] = False
    try:
        # to make sure index 0 gives the first element in the array
        if pos == 0:
            ans = numpy.flatnonzero(flags)[pos]
            return ans
        # pos-1 as python index start at 0
        ans = numpy.flatnonzero(flags)[k-1]
    except:
        return sieve(n*n, k)
    return ans
