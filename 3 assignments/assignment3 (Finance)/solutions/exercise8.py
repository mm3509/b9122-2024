def is_leap_year(n):
    """
    >>> is_leap_year(1984)
    True
    >>> is_leap_year(1985)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year('1984')
    Traceback (most recent call last):
        ...
    ValueError: argument must be a positive integer
    >>> is_leap_year(-4)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a positive integer
    """

    if not (isinstance(n, int) and n > 0):
        raise ValueError("argument must be a positive integer")

    if n % 400 == 0:
        return True

    if n % 100 == 0:
        return False

    if n % 4 == 0:
        return True

    return False


def filter_out_leap_years(a):
    """
    >>> a = [1900, 1984, 1985, 2000]
    >>> filter_out_leap_years(a)
    >>> a
    [1984, 2000]
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
        if is_leap_year(a[i]):
            continue
        a.pop(i)
