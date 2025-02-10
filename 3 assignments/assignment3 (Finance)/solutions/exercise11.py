import sys


def clean_string(s):

    s = s.lower()
    for punctuation in [" ", ".", "'", ",", '"', ":"]:
        s = s.replace(punctuation, "")

    return sorted(s)


def are_anagrams(s1, s2):
    """
    >>> are_anagrams("The Morse Code", "Here come dots")
    True
    >>> are_anagrams("Madame Curie", "me: radium ace")
    True
    >>> are_anagrams("", "")
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

    s1_clean = clean_string(s1)
    s2_clean = clean_string(s2)

    return s1_clean == s2_clean


if "__main__" == __name__:

    if 3 != len(sys.argv):
        raise ValueError("You must pass exactly two arguments")

    s1 = sys.argv[1]
    s2 = sys.argv[2]

    print(are_anagrams(s1, s2))
