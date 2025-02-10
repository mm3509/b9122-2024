import os

DELIMITER = ","

def check_argument(line):
    if not isinstance(line, str):
        raise ValueError("argument must be a string")


def parse_csv_imperative(line):
    """
    >>> parse_csv_imperative("Kings,NY,1234")
    ['Kings', 'NY', '1234']
    >>> parse_csv_imperative(1234)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a string
    """

    check_argument(line)

    if "" == line:
        return []
    
    return line.split(DELIMITER)


def parse_csv_recursive(line):
    if "" == line:
        return []

    if line.startswith(("'", '"')):
        ending = line.index(line[0], 1)
        value = line[1:ending]
        return [value] + parse_csv_recursive(line[ending + 2:])

    delim_index = line.find(DELIMITER)
    if -1 == delim_index:
        return [line]

    return [line[:delim_index]] + parse_csv_recursive(line[delim_index + 1:])


def parse_csv_recursive_wrapper(line):
    """
    >>> parse_csv_recursive_wrapper("Kings,NY,1234")
    ['Kings', 'NY', '1234']
    >>> parse_csv_recursive_wrapper('"Washington, D.C.",DC,1234')
    ['Washington, D.C.', 'DC', '1234']
    >>> parse_csv_recursive_wrapper(1234)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a string
    """

    check_argument(line)

    return parse_csv_recursive(line)


def read_csv(filepath):
    """
    >>> read_csv(123)
    Traceback (most recent call last):
        ...
    ValueError: argument must be a string
    >>> read_csv("/path/to/missing/file")
    Traceback (most recent call last):
        ...
    ValueError: filepath must exist
    """
        
    if not isinstance(filepath, str):
        raise ValueError("argument must be a string")

    if not os.path.exists(filepath):
        raise ValueError("filepath must exist")


    result = []
    with open(filepath) as f:
        for line in f.readlines():
            result.append(parse_csv_recursive(line))

    return result
