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
