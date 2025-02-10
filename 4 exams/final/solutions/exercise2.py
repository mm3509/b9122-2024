def all_characters_unique(s):
    """
    >>> all_characters_unique("hello")
    False
    >>> all_characters_unique("Pip")
    False
    >>> all_characters_unique("Python")
    True
    >>> all_characters_unique(123)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a string
    """

    if not isinstance(s, str):
        raise ValueError("argument must be a string")

    seen = set()
    for char in s.lower():
        if char in seen:
            return False
        seen.add(char)

    return True
