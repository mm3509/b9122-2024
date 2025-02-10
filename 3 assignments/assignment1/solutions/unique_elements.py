import doctest


def get_unique(ascending_list):
    """
    Gets the unique elements of a sorted list of integers.

    Args:
      l: A list of integers, sorted ascendingly.

    Returns:
      A list of unique elements in the original list.

    Raises:
      ValueError: If the list is not sorted, or does not contain integers.

    >>> get_unique([2, 2, 4, 4, 6, 8, 9, 10, 10])
    [2, 4, 6, 8, 9, 10]
    >>> get_unique([2, 4, 6, 8, -9, 10])
    Traceback (most recent call last):
        ...
    ValueError: Argument must be a sorted list
    >>> get_unique([2.5, 6])
    Traceback (most recent call last):
        ...
    ValueError: Argument must be a list of integers
    >>> get_unique(["1", "2"])
    Traceback (most recent call last):
        ...
    ValueError: Argument must be a list of integers
    >>> get_unique(123)
    Traceback (most recent call last):
        ...
    ValueError: Argument must be a list
    >>> get_unique("abcd")
    Traceback (most recent call last):
        ...
    ValueError: Argument must be a list
    """

    if not isinstance(ascending_list, list):
        raise ValueError("Argument must be a list")

    if not all([isinstance(element, int) for element in ascending_list]):
        raise ValueError("Argument must be a list of integers")

    for i in range(len(ascending_list) - 1):
        if ascending_list[i] > ascending_list[i + 1]:
            raise ValueError("Argument must be a sorted list")

    unique_list = []
    for element in ascending_list:
        if element not in unique_list:
            unique_list.append(element)

    return unique_list


if __name__ == "__main__":
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 == tests_run:
        print("Unable to run doc-tests")
    elif 0 != tests_failed:
        print("Some doc-tests failed")
    else:
        print("Your doc-tests pass, congratulations!")
