VOWELS = "aeiouy"

def get_consonants_lowercase(s):
    """
    >>> get_consonants_lowercase('ABCD')
    'bcd'
    >>> get_consonants_lowercase('y')
    ''
    >>> get_consonants_lowercase(['a', 'B'])
    Traceback (most recent call last):
        ...
    ValueError: argument must be a string
    """

    if not isinstance(s, str):
        raise ValueError("argument must be a string")

    res = []
    for c in s.lower():
        if c in VOWELS:
            continue
        res.append(c)

    return "".join(res)
