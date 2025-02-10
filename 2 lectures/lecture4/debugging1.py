import doctest
import numpy

def sum_numpy(a, b):
    """
    Sum two numbers.

    >>> import numpy
    >>> a = numpy.uint8(1)
    >>> b = numpy.uint8(2)
    >>> bool(sum_numpy(a, b) == 3)
    True
    >>> a = numpy.uint8(250)
    >>> b = numpy.uint8(250)
    >>> bool(sum_numpy(a, b) == 500)
    True
    """

    return a + b



a = numpy.uint8(250)
b = numpy.uint8(250)

# TODO: add a breakpoint here, then step into the function.
# Iterate through the function and look at the result in the Console.
# Find why 250 + 250 is not 500.
c = sum_numpy(a, b)


doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'

print("Your doc-tests pass, congratulations!")

