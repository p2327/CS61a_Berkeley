class FibIter:
    def __init__(self):
        self._next = 0
        self._addend = 1
        
    def __next__(self):
        result = self._next
        self._addend, self._next = self._next, self._addend + self._next
        return result
        

fibs = FibIter()

fibos = [next(fibs) for _ in range(10)]
