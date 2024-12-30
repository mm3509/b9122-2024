def merge_intervals(list_of_tuples):
    """
    >>> merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)])
    [(1, 6), (8, 10), (15, 18)]
    >>> merge_intervals([(1, 4), (4, 5)])
    [(1, 5)]
    >>> merge_intervals([(1, 4), (2, 3)])
    [(1, 4)]
    >>> merge_intervals(123)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a list of valid tuple intervals
    >>> merge_intervals([1, 2, 3])
    Traceback (most recent call last):
    ...
    ValueError: argument must be a list of valid tuple intervals
    >>> merge_intervals([(1, 2), (3, 1)])
    Traceback (most recent call last):
    ...
    ValueError: argument must be a list of valid tuple intervals
    >>> merge_intervals([(1, 2), (3, 3)])
    Traceback (most recent call last):
    ...
    ValueError: argument must be a list of valid tuple intervals
    """

    msg = "argument must be a list of valid tuple intervals"
    if not isinstance(list_of_tuples, list):
        raise ValueError(msg)

    for element in list_of_tuples:
        if not isinstance(element, tuple):
            raise ValueError(msg)
        if 2 != len(element):
            raise ValueError(msg)
        if element[0] >= element[1]:
            raise ValueError(msg)

    if 0 == len(list_of_tuples):
        return []

    # Students: this sorts the list by the first element, then the
    # second.
    sorted_list = sorted(list_of_tuples)

    merged_list = []
    current_tuple = sorted_list[0]

    for i in range(len(sorted_list) - 1):
        next_tuple = sorted_list[i + 1]

        if current_tuple[1] < next_tuple[0]:
            merged_list.append(current_tuple)
            current_tuple = next_tuple
        else:
            end = max(current_tuple[1], next_tuple[1])
            current_tuple = (current_tuple[0], end)

    merged_list.append(current_tuple)

    return merged_list
