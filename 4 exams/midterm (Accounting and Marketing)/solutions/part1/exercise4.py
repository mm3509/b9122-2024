def select_nth_elements(a, n):
    """
    >>> select_nth_elements([1, 2, 3], 1)
    [1, 2, 3]
    >>> select_nth_elements(['one', 2, 3, 'four'], 2)
    ['one', 3]
    >>> select_nth_elements(['one', 2, 3, 'four', 'five'], 4)
    ['one', 'five']
    >>> select_nth_elements('abcd', 2)
    Traceback (most recent call last):
        ...
    ValueError: first argument must be a list
    >>> select_nth_elements([1, 2, 3], 2.5)
    Traceback (most recent call last):
        ...
    ValueError: second argument must be an integer
    >>> select_nth_elements([1, 2, 3], 4)
    Traceback (most recent call last):
        ...
    ValueError: second argument must be smaller than size of list
    >>> select_nth_elements([1, 2, 3], 0)
    Traceback (most recent call last):
        ...
    ValueError: second argument must non-negative
    """

    if not isinstance(a, list):
        raise ValueError("first argument must be a list")

    if not isinstance(n, int):
        raise ValueError("second argument must be an integer")

    if n > len(a):
        raise ValueError("second argument must be smaller than size of list")

    if n <= 0:
        raise ValueError("second argument must non-negative")

    if n == 1:
        return a.copy()

    return a[0::n]
