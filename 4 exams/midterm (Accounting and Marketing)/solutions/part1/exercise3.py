def rotate_list(a, steps):
    """
    >>> rotate_list([1, 2, 3], 1)
    [3, 1, 2]
    >>> rotate_list([], 2)
    []
    >>> rotate_list(['one', 2, 3, 'four'], 2)
    [3, 'four', 'one', 2]
    >>> rotate_list(['one', 2, 3, 'four'], 4)
    ['one', 2, 3, 'four']
    >>> rotate_list([37, 42, 31, 11, 28, 5, 9, 39, 21, 14, 25], 4)
    [39, 21, 14, 25, 37, 42, 31, 11, 28, 5, 9]
    >>> rotate_list('abcd', 2)
    Traceback (most recent call last):
    ...
    ValueError: first argument must be a list
    >>> rotate_list([1, 2, 3], 2.5)
    Traceback (most recent call last):
    ...
    ValueError: second argument must be an integer
    """

    if not isinstance(a, list):
        raise ValueError("first argument must be a list")

    if not isinstance(steps, int):
        raise ValueError("second argument must be an integer")

    if [] == a:
        return a.copy()

    steps = steps % len(a)
    
    if steps in [0, len(a)]:
        return a.copy()

    return a[-steps:] + a[:-steps]
