def tree(root, branches=[]):
    return lambda dispatch: root if dispatch == 'root' else list(branches)
    
def root(tree):
    return tree('root')
    
def branches(tree):
    return tree('branches')
    
t = tree(1,
         [tree(2),
          tree(3,
               [tree(4),
                tree(5)]),
          tree(6,
               [tree(7)])])
               

def print_tree(t, indent=0):
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)

""" Q1
Define the function countdown_tree so that it returns 
the specific tree below.Make sure to use the tree constructor 
from the Data Abstraction!"""

def countdown_tree():
    """Return a tree that has the following structure.

    >>> print_tree(countdown_tree())
    10
      9
        8
      7
        6
          5
    """
    "*** YOUR CODE HERE ***"
    return tree(10,[tree(9,[tree(8)]),tree(7,[tree(6,[tree(5)])])])
    
print_tree(countdown_tree())


""" Q2
Define the function size_of_tree, which takes in a tree 
as an argument and returns the number of entries in the tree."""

def size_of_tree(t):
    """Return the number of entries in the tree.

    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> size_of_tree(numbers)
    7
    """
    "*** YOUR CODE HERE ***"
    return 1 + sum([size_of_tree(t) for t in branches(t)])
    # alt solution
    """ 
    return len(t)
    if len(branches(t))==0:
        return 1
    else:
        size=1
        for branch in branches(t):
            size += size_of_tree(branch)
        return size """
