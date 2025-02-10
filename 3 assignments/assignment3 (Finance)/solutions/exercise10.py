def remove_all(a, item):
    """
    >>> a = [1, 2, 3]
    >>> remove_all(a, 1)
    >>> a
    [2, 3]
    >>> a = [1, 2, 3]
    >>> remove_all(a, 3)
    >>> a
    [1, 2]
    >>> a = [1, 2, 3]
    >>> remove_all(a, 4)
    >>> a
    [1, 2, 3]
    >>> a = [2, 2, 3, 4]
    >>> remove_all(a, 2)
    >>> a
    [3, 4]
    >>> remove_all("abcd", "a")
    Traceback (most recent call last):
        ...
    ValueError: first argument must be a list
    """

    if not isinstance(a, list):
        raise ValueError("first argument must be a list")
    
    i = len(a) - 1
    while i >= 0:
        if a[i] == item:
            a.pop(i)
        i -= 1
