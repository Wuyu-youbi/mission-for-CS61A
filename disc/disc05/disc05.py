def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branches)
    return [label] + branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if len(tree) < 1 or type(tree) != list:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 1), fib_tree(n - 2)
        return tree(label(left) + label(right),[left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    branch_count = [count_leaves(branch) for branch in branches(tree)]
    return sum(branch_count)

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(branch) for branch in branches(tree)],[])
    
def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(branch) for branch in branches(t)]
        return tree(label(t), bs)

def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent = 0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)  

def count_path(t,total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_path(b, total - label(t)) for b in branches(t)])

'''---------------------------------------------------------------------------------------------------------------------------'''

'''things above are former code, which is useful for the main code and build the data abstraction '''

def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == [label(t)]:  # when len(p) is 1
        return True
    elif label(t) != p[0]:
        return False
    else:
        "*** YOUR CODE HERE ***"
        return any(has_path(b, p[1:]) for b in branches(t))
    
def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if label(t) == x:
        return [label(t)]
    else:
        path = find_path(branches(t), x)
        if path:
            return [label(t)] + path
    return None
    '''this quastion i need to try again for a better understanding
        the URM: https://insideempire.github.io/CS61A-Website-Archive/disc/disc05/index.html Q3 Find Path'''
   

