SEPARATOR = " "

def refill_recursive(s, max_chars):

    if not s:
        return []

    if s.startswith(" ") or s.endswith(" "):
        return refill_recursive(s.strip(), max_chars)

    if len(s) <= max_chars:
        return [s]

    if s[max_chars] == SEPARATOR:
        return [s[:max_chars]] + refill_recursive(s[max_chars:], max_chars)

    i = s[:max_chars].rfind(SEPARATOR)

    if i == -1:
        i = max_chars

    return [s[:i]] + refill_recursive(s[i:], max_chars)


def refill_wrapper(s, max_chars=80):
    """
    >>> refill_wrapper('')
    []
    >>> refill_wrapper('abcd', max_chars=2)
    ['ab', 'cd']
    >>> refill_wrapper('abc', max_chars=2)
    ['ab', 'c']
    >>> refill_wrapper('1234567', max_chars=3)
    ['123', '456', '7']
    >>> refill_wrapper('123456789', max_chars=2)
    ['12', '34', '56', '78', '9']
    >>> refill_wrapper('abcd', max_chars=3)
    ['abc', 'd']
    >>> refill_wrapper('ab cd ef gh', max_chars=5)
    ['ab cd', 'ef gh']
    >>> refill_wrapper('I will send an announcement', max_chars=15)
    ['I will send an', 'announcement']
    >>> refill_wrapper(123)
    Traceback (most recent call last):
        ...
    ValueError: first argument must be a string
    >>> refill_wrapper('abcd', '80')
    Traceback (most recent call last):
        ...
    ValueError: second argument must be a positive integer
    """
    if not isinstance(s, str):
        raise ValueError("first argument must be a string")

    if not (isinstance(max_chars, int) and max_chars > 0):
        raise ValueError("second argument must be a positive integer")

    return refill_recursive(s, max_chars)
