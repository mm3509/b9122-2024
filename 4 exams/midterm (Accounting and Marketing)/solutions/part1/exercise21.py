import sys


import exercise5


def clean_string(s):

    return s.lower().replace(" ", "")


def are_anagrams(s1, s2):
    """
    >>> are_anagrams("The Morse Code", "Here come dots")
    True
    >>> are_anagrams("", "")
    True
    >>> are_anagrams(1, "1")
    Traceback (most recent call last):
        ...
    ValueError: arguments must be strings
    >>> are_anagrams("1", 1)
    Traceback (most recent call last):
        ...
    ValueError: arguments must be strings
    """

    if not (isinstance(s1, str) and isinstance(s2, str)):
        raise ValueError("arguments must be strings")

    d1 = exercise5.count_frequency(clean_string(s1))
    d2 = exercise5.count_frequency(clean_string(s2))

    return d1 == d2


if "__main__" == __name__:

    if 3 != len(sys.argv):
        raise ValueError("You must pass exactly two arguments")

    s1 = sys.argv[1]
    s2 = sys.argv[2]

    print(are_anagrams(s1, s2))
