class Link:
    """A recursive list, with Python integration."""
    empty = None
 
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
 
    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({}{})'.format(self.first, rest)
 
    def __str__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ' ' + str(self.rest)[2:-2]
        return '< {}{} >'.format(self.first, rest)
        
a = Link(1)

a.rest = Link(2)

b = Link(1, Link(2, Link(3)))
