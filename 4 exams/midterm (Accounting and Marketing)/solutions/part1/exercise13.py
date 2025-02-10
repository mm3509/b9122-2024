import exercise2

def filter_out_leap_years(a):
    """
    >>> filter_out_leap_years([1900, 1984, 1985, 2000])
    [1900, 1985]
    >>> filter_out_leap_years('abcd')
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of non-negative integers
    >>> filter_out_leap_years([1980, '2000'])
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of non-negative integers
    >>> filter_out_leap_years([-1, 2000])
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of non-negative integers
    """

    error_msg = "argument must be a list of non-negative integers"
    if not isinstance(a, list):
        raise ValueError(error_msg)

    for i in a:
        if not (isinstance(i, int) and i > 0):
            raise ValueError(error_msg)

    res = []
    for i in a:
        if exercise2.is_leap_year(i):
            continue
        res.append(i)

    return res
