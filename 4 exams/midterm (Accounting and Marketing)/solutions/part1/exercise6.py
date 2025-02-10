def get_unique(t):
    """
    >>> get_unique(('a', 'b', 'a'))
    ('a', 'b')
    >>> get_unique(123)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a tuple
    """

    if not isinstance(t, tuple):
        raise ValueError("argument must be a tuple")

    seen = set()
    res = []

    for item in t:
        if item in seen:
            continue
        
        seen.add(item)
        res.append(item)

    return tuple(res)
