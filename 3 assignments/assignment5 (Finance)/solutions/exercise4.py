def maximize_profit(prices):
    """
    >>> maximize_profit([5, 6, 9, 2, 4, 5])
    4
    >>> maximize_profit([10, 5, 4, 3, 2, 0])
    0
    >>> maximize_profit('abc')
    Traceback (most recent call last):
    ...
    ValueError: argument must be an array of non-negative numbers
    >>> maximize_profit([1, '0'])
    Traceback (most recent call last):
    ...
    ValueError: argument must be an array of non-negative numbers
    >>> maximize_profit([1, -1])
    Traceback (most recent call last):
    ...
    ValueError: argument must be an array of non-negative numbers
    """

    error_msg = "argument must be an array of non-negative numbers"
    if not isinstance(prices, list):
        raise ValueError(error_msg)

    if not all([isinstance(p, (float, int)) for p in prices]):
        raise ValueError(error_msg)

    if not all([p >= 0 for p in prices]):
        raise ValueError(error_msg)

    max_profit = 0
    len_prices = len(prices)
    for buying_day in range(len_prices):
        for selling_day in range(buying_day + 1, len_prices):
            profit = prices[selling_day] - prices[buying_day]
            if profit > max_profit:
                max_profit = profit

    return max_profit
