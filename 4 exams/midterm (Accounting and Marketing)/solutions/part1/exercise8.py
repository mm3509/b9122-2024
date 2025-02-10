def sum_integers_up_to_number(n):
    """
    >>> sum_integers_up_to_number(3)
    6
    >>> sum_integers_up_to_number(9)
    45
    >>> sum_integers_up_to_number('abcd')
    Traceback (most recent call last):
        ...
    ValueError: argument must be a positive integer
    """

    if not (isinstance(n, int) and n >= 0):
        raise ValueError("argument must be a positive integer")

    result = 0
    for i in range(n + 1):
        result += i

    return result
