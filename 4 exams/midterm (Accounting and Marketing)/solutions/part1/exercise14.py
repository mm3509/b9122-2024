import exercise2


def filter_out_leap_years(a):
    """
    >>> a = [1900, 1984, 1985, 2000]
    >>> filter_out_leap_years(a)
    >>> a
    [1900, 1985]
    >>> filter_out_leap_years("abcd")
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of non-negative integers
    >>> filter_out_leap_years([1980, "2000"])
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

    for i in range(len(a) - 1, -1, -1):
        element = a[i]
        if not exercise2.is_leap_year(a[i]):
            continue
        a.pop(i)
