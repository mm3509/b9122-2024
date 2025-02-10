STOPWORDS = ["of", "a", "and", "the"]

def convert_to_title_case(s):
    """
    >>> convert_to_title_case("a tale of two cities")
    'A Tale of Two Cities'
    >>> convert_to_title_case("of mice and men")
    'Of Mice and Men'
    >>> convert_to_title_case(123)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a string
    """

    if not isinstance(s, str):
        raise ValueError("argument must be a string")

    if 1 >= len(s):
        return s.upper()

    result = []
    words = s.split(" ")
    for word in words:
        if result and word.lower() in STOPWORDS:
            result.append(word.lower())
            continue
        if 1 >= len(word):
            result.append(word.upper())
            continue
        
        result.append(word[0].upper() + word[1:].lower())
    
    return " ".join(result)
