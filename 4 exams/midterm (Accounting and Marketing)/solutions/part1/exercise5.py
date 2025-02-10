def count_frequency(s):
    """
    >>> count_frequency('aba')
    {'a': 2, 'b': 1}
    >>> count_frequency('abc')
    {'a': 1, 'b': 1, 'c': 1}
    >>> count_frequency(123)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a string
    """

    if not isinstance(s, str):
        raise ValueError("argument must be a string")

    res = {}
    for c in s:
        res[c] = res.get(c, 0) + 1

    return res
