import numpy as np


def compute_variance_of_log_growth(a):
    """
    >>> a = np.array([[1, np.exp(1), np.exp(3)]])
    >>> compute_variance_of_log_growth(a.T)
    0.25
    >>> compute_variance_of_log_growth(123)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a NumPy 2D-array with a column vector
    >>> compute_variance_of_log_growth(np.array([1, 2, 3]))
    Traceback (most recent call last):
        ...
    ValueError: argument must be a NumPy 2D-array with a column vector
    >>> compute_variance_of_log_growth(np.array([[1, 2, 3], [4, 5, 6]]))
    Traceback (most recent call last):
        ...
    ValueError: argument must be a NumPy 2D-array with a column vector
    """

    error_msg = "argument must be a NumPy 2D-array with a column vector"
    
    if not isinstance(a, np.ndarray):
        raise ValueError(error_msg)

    if 2 != len(a.shape):
        raise ValueError(error_msg)

    if 1 != a.shape[1]:
        raise ValueError(error_msg)

    return float(np.var(np.log(a[1:]) - np.log(a[:-1])))

