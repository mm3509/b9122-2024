def is_palindrome(s):
    """
    >>> is_palindrome("abba")
    True
    >>> is_palindrome("Abba")
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(121)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a string
    """

    if not isinstance(s, str):
        raise ValueError("argument must be a string")

    s = s.lower()
    return s == s[::-1]
