#!/usr/local/bin/python3

import doctest

    

def compute_area(height, width):
    """
    >>> compute_area(2, 3)
    6
    >>> compute_area(2, -1)
    Traceback (most recent call last):
        ...
    ValueError: arguments must be positive
    >>> compute_area("B9122", 2)
    Traceback (most recent call last):
        ...
    ValueError: arguments must be numbers
    """

    return None


doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
print("All tests succeed, good job!")
