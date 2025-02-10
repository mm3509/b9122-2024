def merge_intervals(list_of_tuples):
    """
    >>> merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)])
    [(1, 6), (8, 10), (15, 18)]
    >>> merge_intervals([(1, 4), (4, 5)])
    [(1, 5)]
    >>> merge_intervals([(1, 4), (2, 3)])
    [(1, 4)]
    """

    # TODO: add defensive programming.

    # Students: this sorts the list by the first element, then the
    # second.
    sorted_list = sorted(list_of_tuples)  # noqa: F841

    # TODO: complete the function.

    return
