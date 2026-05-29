def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        return True
    else:
        all_but_last, last, second_last = x // 10, x % 10, ((x // 10) % 10)
        while all_but_last != 0:
            if last < second_last:
                return False
            all_but_last, last, second_last = all_but_last // 10, all_but_last % 10, ((all_but_last // 10) % 10)
        return True