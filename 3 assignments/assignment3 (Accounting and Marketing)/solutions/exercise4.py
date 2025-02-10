import numpy as np

def check_number(n, argument_name):
    if not isinstance(n, (int, float)):
        raise ValueError("%s argument must be a number" % argument_name)


def compute_integral(fn, start, end, num_segments):
    """
    >>> compute_integral(np.square, 0, 1, 5)
    0.33
    >>> compute_integral("abcd", 0, 1, 10)
    Traceback (most recent call last):
        ...
    ValueError: first argument must be a function
    >>> compute_integral(np.square, "abcd", 1, 10)
    Traceback (most recent call last):
        ...
    ValueError: start range argument must be a number
    >>> compute_integral(np.square, 0, "abcd", 10)
    Traceback (most recent call last):
        ...
    ValueError: end range argument must be a number
    >>> compute_integral(np.square, 0, 1, -5)
    Traceback (most recent call last):
        ...
    ValueError: number of segments must be a positive integer
    >>> compute_integral(np.square, 0, 1, 1.1)
    Traceback (most recent call last):
        ...
    ValueError: number of segments must be a positive integer
    """

    if not callable(fn):
        raise ValueError("first argument must be a function")

    check_number(start, "start range")
    check_number(end, "end range")

    if not (isinstance(num_segments, int) and num_segments > 0):
        raise ValueError("number of segments must be a positive integer")

    integral = 0
    step = (end - start) / num_segments
    current_x = start + step / 2
    for i in range(num_segments):
        integral += fn(current_x)
        current_x += step

    return float(integral * step)
