def is_valid(s):
    """
    >>> is_valid("{}[]{}")
    True
    >>> is_valid("{}[}")
    False
    >>> is_valid("{{{[]}}}")
    True
    >>> is_valid("}")
    False
    >>> is_valid("{{}")
    False
    >>> is_valid("{a}")
    False
    >>> is_valid(123)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a string
    """

    # TODO: complete this function.

    return


if "__main__" == __name__:
    print(is_valid("{}[]{}"))
