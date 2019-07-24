class Vector(object):
    
    def __init__(self, elements=[]): # elements makes more sense than vector
        self.elements = elements
        
    def __len__(self):
        return len(self.elements)
        
    def __getitem__(self, n):
        return self.elements[n]
        
    def __neg__(self):
        """
        >>> t.__neg__()
        Vector([-1, -2, -3])
        """
        return Vector([i*-1 for i in self.elements])
    
    def __add__(self, other):
        return Vector([x+y for x, y in zip(self.elements, other.elements)])

    def __sub__(self, other):
        return self.__add__(-other)
        
    def __mul__(self, other):
        """
        >>> t.__mul__(4)
        Vector([4, 8, 12])
        """
        if type(other) == int or type(other) == float:
            return Vector([i*other for i in self.elements])
    
        elif type(other) == Vector:
            if len(self.elements) != len(other.elements):
                return 0
            return sum([x*y for x, y in zip(self.elements, other.elements)])
    
    def __reverse_mul__(self, other):
        return self.__mul__(other)

    
if __name__ == '__main__': # initialise test object
	import doctest
	doctest.testmod(extraglobs={'t': Vector([1, 2, 3])})
