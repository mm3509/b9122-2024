def sum_even_numbers_from_list(a):
    """
    >>> sum_even_numbers_from_list([1, 2, 3])
    2
    >>> sum_even_numbers_from_list([2, 2, 2])
    6
    >>> sum_even_numbers_from_list('abcd')
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of integers
    >>> sum_even_numbers_from_list([1, 1.4])
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of integers
    >>> sum_even_numbers_from_list([1, '2'])
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of integers
    """

    error_msg = "argument must be a list of integers"
    if not isinstance(a, list):
        raise ValueError(error_msg)

    for i in a:
        if not isinstance(i, int):
            raise ValueError(error_msg)

    result = 0
    for i in a:
        if i % 2 == 0:
            result += i

    return result
