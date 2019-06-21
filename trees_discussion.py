def tree(val, branches=[]):
    assert is_tree(branches), 'branches must be trees'
    for branch in branches:
        return [val] + list(branches)
     
def branches(tree_obj):
    return tree_obj[1:]

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch): 
            return False
    return True



# t1 = tree(4, [3, [4, [3]]])

def square_tree(t):
    root3 = []
    for i in tree:
        root1 = []
        root2 = []
        if not is_tree(i):
            root1 = [i * i]
        else:
            root2 = [square_tree(i)]
        root3 += root1 + root2
    return root3
    
t2 = tree(4, [1, [1]])

# t_squared = square_tree(t2)


def tree_size(tree_obj):
    """return the size of a tree (the number of the nodes)"""
    num = 0
    for i in tree_obj:
        if not is_tree(i):
            num += 1
        else:
            num += tree_size(i)
    return num
    
size = tree_size(t2)


def tree_max(tree):
    """return the max of a tree"""
    num = 0
    for i in tree:
        if not is_tree(i):
            if i > num:
                num = i
        else:
            temp = tree_max(i)
            if num < temp:
                num = temp
    return num

print(tree_max(t))
