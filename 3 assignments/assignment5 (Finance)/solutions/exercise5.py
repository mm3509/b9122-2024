def find_best_sublist(returns):
    """
    >>> find_best_sublist([-1, 1.5, -2.1, -0.8, 3, 2, 5, -4])
    (4, 6, 10)
    >>> find_best_sublist([1])
    (0, 0, 1)
    >>> find_best_sublist([5, 4, -1, 7, 8])
    (0, 4, 23)
    >>> find_best_sublist([-1, -2, -3, -4])
    (-1, -1, 0)
    >>> find_best_sublist('abc')
    Traceback (most recent call last):
    ...
    ValueError: argument must be an array of numbers
    >>> find_best_sublist([1, '0'])
    Traceback (most recent call last):
    ...
    ValueError: argument must be an array of numbers
    """

    error_msg = "argument must be an array of numbers"
    if not isinstance(returns, list):
        raise ValueError(error_msg)

    if not all([isinstance(r, (float, int)) for r in returns]):
        raise ValueError(error_msg)

    # Initialize at an existing return, not at 0.
    best_return = 0
    best_start = -1
    best_end = -1

    len_returns = len(returns)
    
    for start in range(len_returns):
        for end in range(start, len_returns):
            total_return = sum(returns[start:end + 1])
            if total_return > best_return:
                best_return = total_return
                best_start = start
                best_end = end
                               
    return (best_start, best_end, best_return)


def find_best_sublist_fast(returns):

    # This function shows an example of linear complexity.
    # Doc-tests and defensive programming omitted for brevity.

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price 
        else:
            max_profit = max(max_profit, price - min_price)  

    return max_profit
