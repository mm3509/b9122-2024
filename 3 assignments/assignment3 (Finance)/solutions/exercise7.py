def remove_at_even_indices(a):
    """
    >>> a = [0, 1, 2]
    >>> remove_at_even_indices(a)
    >>> a
    [1]
    >>> a = ["one", 2, 3, {'a': '1'}]
    >>> remove_at_even_indices(a)
    >>> a
    [2, {'a': '1'}]
    >>> remove_at_even_indices('abcd')
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list
    """

    if not isinstance(a, list):
        raise ValueError("argument must be a list")

    end_index = len(a) - 1
    if end_index % 2 != 0:
        end_index -= 1
        
    for i in range(end_index, -1, -2):
        a.pop(i)
