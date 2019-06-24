""" A linked list is a pair containing the first element of the sequence (in this case 1) and the rest of the sequence 
(in this case a representation of 2, 3, 4). The second element is also a linked list. 
The rest of the inner-most linked list containing only 4 is 'empty', a value that represents an empty linked list."""



def link(first, rest): # don't confuse these names with function first and rest below
        """Construct a linked list from its first element and the rest."""
        assert is_link(rest), "rest must be a linked list."
        return [first, rest]
    
def is_link(s):
        """s is a linked list if it is empty or a (first, rest) pair."""
        return s == empty or (len(s) == 2 and is_link(s[1]))

def first(s):
    return s[0]
def rest(s):
    return s[1]

def getitem_link(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

four = [1, [2, [3, [4, 'empty']]]] # four has index [0] = 1 and index [1] the rest [2...] 
getitem_link(four, 1)


# recursive implementation of getitem_link
def getitem_link_recursive(s, i):
        """Return the element at index i of linked list s."""
        if i == 0:
            return first(s)
        return getitem_link_recursive(rest(s), i - 1)

    
# recursive implementation of link    
def extend_link(s, t):
        """Return a list with the elements of s followed by those of t."""
        assert is_link(s) and is_link(t)
        if s == empty:
            return t
        else:
            return link(first(s), extend_link(rest(s), t))
