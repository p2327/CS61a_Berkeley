from operator import add

class Naturals(object):
    def __init__(self):
        self.current = 0
        
    def __next__(self):
        result = self.current
        self.current += 1
        return result
        
    def __iter__(self):
        return self
        

class IterCombiner(object):
    def __init__(self, iter1, iter2, combiner):
        self.current1 = iter1.current
        self.current2 = iter2.current
        self.combiner = combiner
    
    def __next__(self):
        result = self.combiner(self.current1, self.current2)
        self.current1 += 1
        self.current2 += 1
        return result
    
    def __iter__(self):
        return self
        
        
evens = IterCombiner(Naturals(), Naturals(), add)

ans = next(evens)

ans2 = next(evens)


class FibIter(object):
    def __init__(self):
        self.pred = 0
        self.curr = 1
        
    def __next__(self):
        resp = self.pred
        self.pred, self.curr = self.curr, self.pred + self.curr
        return resp
        
    def __iter__(self):
        return self


flag = False
count = 0
while not flag:
    fib = next(fibiter)
    print(fib)
    count += 1
    if count == 5:
        flag = True

        
def perfect_squares():
    start = 0
    first = 1
    while True:
        yield start
        start = first**2
        first += 1
        
"""
def perfect_squares():
    start = 0
    first = 1
    while True:
        if start == 0 or start == 1:
            print(f'{start} is the square of {start}')
        else:
            print(f'{start} is the square of {first-1}')
        yield start
        start = first**2
        first += 1
""" 
