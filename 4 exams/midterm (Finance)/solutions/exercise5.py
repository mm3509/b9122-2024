import numpy as np

def square(x):
    return x ** 2


def check_number(n, argument_name):
    if not isinstance(n, (int, float)):
        raise ValueError("%s argument must be a number" % argument_name)


def compute_integral(fn, start, end, step):
    """
    >>> compute_integral(square, 0, 1, 0.2)
    0.33
    >>> compute_integral('abcd', 0, 1, 0.1)
    Traceback (most recent call last):
    ...
    ValueError: first argument must be a function
    >>> compute_integral(square, 'abcd', 1, 0.1)
    Traceback (most recent call last):
    ...
    ValueError: start range argument must be a number
    >>> compute_integral(square, 0, 'abcd', 0.1)
    Traceback (most recent call last):
    ...
    ValueError: end range argument must be a number
    >>> compute_integral(square, 0, 1, 'abcd')
    Traceback (most recent call last):
    ...
    ValueError: step argument must be a number
    >>> compute_integral(square, 0, 1, 1.1)
    Traceback (most recent call last):
    ...
    ValueError: step argument must be smaller than the range length
    """

    if not callable(fn):
        raise ValueError("first argument must be a function")

    check_number(start, "start range")
    check_number(end, "end range")
    check_number(step, "step")

    if step > end - start:
        raise ValueError("step argument must be smaller than the range length")

    integral = 0
    current_x = start + step / 2
    while current_x < end:
        integral += fn(current_x)
        current_x += step

    return integral * step

