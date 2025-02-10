def get_squares(a):
    """
    >>> get_squares([1, 3, 4])
    [16]
    >>> get_squares([])
    []
    >>> get_squares("abcd")
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list of integers
    >>> get_squares(["3", "4"])
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
    
    
    return [i ** 2 for i in a if i % 2 == 0]
