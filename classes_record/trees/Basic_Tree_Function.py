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