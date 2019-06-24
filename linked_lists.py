""" A linked list is a pair containing the first element of the sequence (in this case 1) and the rest of the sequence 
(in this case a representation of 2, 3, 4). The second element is also a linked list. 
The rest of the inner-most linked list containing only 4 is 'empty', a value that represents an empty linked list."""


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
