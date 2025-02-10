def copy_even_numbers(a):
    """
    >>> copy_even_numbers([1, 2, 3])
    [2]
    >>> copy_even_numbers([2, 2, 2])
    [2, 2, 2]
    >>> copy_even_numbers("abcd")
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of integers
    >>> copy_even_numbers([1, "a", "b"])
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of integers
    >>> copy_even_numbers([1, 1.5])
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

    result = []
    for i in a:
        if i % 2 == 0:
            result.append(i)

    return result
