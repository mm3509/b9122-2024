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

    ############################################################################
    #
    # TODO: Complete the rest of this function, until the next heading
    # similar to this one
    #
    ############################################################################
    return []








    ############################################################################
    #
    # Your function should end here. You can write or edit code below
    # this point to help you solve the assignment, but it will not be
    # tested nor graded.
    #
    ############################################################################


tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
if 0 < tests_run:
    assert 0 == tests_failed, 'Some doc-tests failed, exiting...'
    print('Your doc-tests pass, congratulations!')
else:
    print('Unable to run doc-tests, please see Miguel!')


# Example usage.
print(get_unique([2, 2, 4, 4, 6, 8, 9, 10, 10]))
