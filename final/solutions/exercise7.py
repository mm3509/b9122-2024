def longest_substring(s):
    """
    >>> longest_substring("abcabcbb")  # = 3 ("abc")
    3
    >>> longest_substring("bbbbb")     # = 1 ("b")
    1
    >>> longest_substring("weekend")    # = 4 ("kend")
    4
    >>> longest_substring("")           # = 0
    0
    >>> longest_substring(123)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a string
    """

    if not isinstance(s, str):
        raise ValueError("argument must be a string")

    s = s.lower()
    max_length = 0
    for start in range(len(s)):
        seen = set(s[start])
        for end in range(start + 1, len(s) + 1):

            if end == len(s):
                max_length = max(max_length, len(s) - start)
                break

            char = s[end]
            max_length = max(max_length, end - start)
            if char in seen:
                break
            seen.add(char)

    return max_length
