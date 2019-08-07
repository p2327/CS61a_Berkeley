class Letters:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return LetterIter(self.start, self.end)
        

class LetterIter:
    
    def __init__(self, start, end):
        self.next_letter = start
        self.end = end
        
    def __next__(self):
        if self.next_letter >= self.end:
            raise StopIteration    
        result = self.next_letter
        self.next_letter = chr(ord(result)+1)
        return result
        
        
b_to_e = Letters('b', 'e') # initialise a Letters object

li = iter(b_to_e) # initialise iterator on Letters object

next(li)
next(li)
