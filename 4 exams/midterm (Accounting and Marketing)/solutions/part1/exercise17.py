def calculate_sum_recursive(a):

    if not a:
        return 0

    return a[0] + calculate_sum_recursive(a[1:])


def calculate_sum(a):
    """
    >>> calculate_sum([1, 3, 4])
    8
    >>> calculate_sum([])
    0
    >>> calculate_sum("abcd")
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of integers
    >>> calculate_sum(["3", "4"])
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

    return calculate_sum_recursive(a)
