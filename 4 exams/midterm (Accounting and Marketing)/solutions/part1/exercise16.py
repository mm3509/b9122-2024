def check_argument(a):
    error_msg = "arguments must be lists of integers"
    if not isinstance(a, list):
        raise ValueError(error_msg)

    for i in a:
        if not isinstance(i, int):
            raise ValueError(error_msg)


def combine_and_sort_lists(a, b):
    """
    >>> combine_and_sort_lists([1, 3, 4], [0, 2, 5])
    [0, 1, 2, 3, 4, 5]
    >>> combine_and_sort_lists("abcd", [])
    Traceback (most recent call last):
        ...
    ValueError: arguments must be lists of integers
    >>> combine_and_sort_lists([], "abcd")
    Traceback (most recent call last):
        ...
    ValueError: arguments must be lists of integers
    >>> combine_and_sort_lists([1, 2], ["3", "4"])
    Traceback (most recent call last):
        ...
    ValueError: arguments must be lists of integers
    >>> combine_and_sort_lists(["1", "2"], [3, 4])
    Traceback (most recent call last):
        ...
    ValueError: arguments must be lists of integers
    """

    for tmp in [a, b]:
        check_argument(tmp)

    return sorted(a + b)
