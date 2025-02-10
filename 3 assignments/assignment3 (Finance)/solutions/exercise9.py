def check_argument(a):
    if not isinstance(a, list):
        raise ValueError("argument must be a list")


def copy_and_reverse(a):
    """
    >>> copy_and_reverse([1, 2, 3])
    [3, 2, 1]
    >>> copy_and_reverse("abcd")
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list
    """

    check_argument(a)

    return a[::-1]


def get_mirror_index(a, i):
    """
    >>> get_mirror_index([1, 2, 3], 0)
    2
    >>> get_mirror_index([1, 2, 3, 4], 1)
    2
    >>> get_mirror_index([1, 2, 3, 4, 5], 4)
    0
    """
    if len(a) % 2 == 0:
        return len(a) - i - 1

    return len(a) - i - 1


def reverse_in_place(a):
    """
    >>> a = [1, 2, 3]
    >>> reverse_in_place(a)
    >>> a
    [3, 2, 1]
    >>> reverse_in_place("abcd")
    Traceback (most recent call last):
        ...
    ValueError: argument must be a list
    """

    check_argument(a)

    for i in range(len(a) // 2):
        temp = a[i]
        a[i] = a[len(a) - i - 1]
        a[get_mirror_index(a, i)] = temp
