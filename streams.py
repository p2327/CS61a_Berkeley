class Stream:
        """A lazily computed linked list."""
        class empty:
            def __repr__(self):
                return 'Stream.empty'
        empty = empty()
        def __init__(self, first, compute_rest=lambda: empty):
            assert callable(compute_rest), 'compute_rest must be callable.'
            self.first = first
            self._compute_rest = compute_rest
        @property
        def rest(self):
            """Return the rest of the stream, computing it if necessary."""
            if self._compute_rest is not None:
                self._rest = self._compute_rest()
                self._compute_rest = None
            return self._rest
        def __repr__(self):
            return 'Stream({0}, <...>)'.format(repr(self.first))
            
            

"""When a Stream instance is constructed, the field self._rest is None, 
signifying that the rest of the Stream has not yet been computed. 
When the rest attribute is requested via a dot expression, 
the rest property method is invoked, which triggers computation 
with self._rest = self._compute_rest(). 

Because of the caching mechanism within a Stream, 
the compute_rest function is only ever called once, then discarded.

Lazy evaluation gives us the ability to represent infinite sequential datasets
using streams. For example, we can represent increasing integers, 
starting at any first value."""

def integer_stream(first):
        def compute_rest():
            return integer_stream(first+1)
        return Stream(first, compute_rest)
        
ans = integer_stream(5)

ans2 = ans.rest

# compute the next integer infinitely
ans3 = ans.rest.rest.rest
