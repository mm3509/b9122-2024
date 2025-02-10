import math
import time

def check_argument(n):

    if not (isinstance(n, int) and n > 0):
        raise ValueError("argument must be a positive integer")
    

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    >>> is_prime(11)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1.5)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a positive integer
    >>> is_prime(-2)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a positive integer
    """

    check_argument(n)

    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def get_primes_slow(n):
    """
    >>> get_primes_slow(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> get_primes_slow(11)
    [2, 3, 5, 7, 11]
    >>> get_primes_slow(1.5)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a positive integer
    >>> get_primes_slow(-2)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a positive integer
    """

    check_argument(n)

    res = []
    for i in range(2, n + 1):
        if is_prime(i):
            res.append(i)

    return res


def get_primes_fast(n):
    """
    >>> get_primes_fast(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> get_primes_fast(100) == get_primes_slow(100)
    True
    >>> get_primes_fast(11)
    [2, 3, 5, 7, 11]
    >>> get_primes_fast(1.5)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a positive integer
    >>> get_primes_fast(-2)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a positive integer
    """

    check_argument(n)
    
    # Initialize a list containing whether the integer could be a
    # prime. For simplicity, the index of the list correspondes to the
    # integer, e.g. could_be_prime[n] contains whether n could be a
    # prime number, so the first two elements, for 0 and 1, have to be
    # False.
    could_be_prime = [True for _ in range(n + 1)]
    could_be_prime[0] = False
    could_be_prime[1] = False

    i = 1
    while i ** 2 <= n:
        i += 1
        if not could_be_prime[i]:
            continue
        
        for multiplier in range(i, n // i + 1):
            multiple = i * multiplier
            could_be_prime[multiple] = False

    return [i for i in range(len(could_be_prime)) if could_be_prime[i]]


if __name__ == "__main__":

    N = int(2e5)
    start = time.time()
    get_primes_slow(N)
    slow = time.time() - start
    print("Slow: ", slow)
    
    start = time.time()
    get_primes_fast(N)
    fast = time.time() - start
    print("Fast: ", fast)
    print("Improvement for n = %d: %dx" % (N, slow / fast))
