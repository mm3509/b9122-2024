import doctest

def factorial(n):
    """
    >>> factorial(0)
    1
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(3.5)
    Traceback (most recent call last):
    ...
    ValueError: argument must be integer
    >>> factorial("3")
    Traceback (most recent call last):
    ...
    ValueError: argument must be integer
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: argument must be positive
    """

    # TODO: complete this function.
    return -1


tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
if 0 < tests_run:
    assert 0 == tests_failed, 'Some doc-tests failed, exiting...'
    print("Your doc-tests pass, congratulations!")
else:
    print("Unable to run doc-tests, please see Miguel!")
