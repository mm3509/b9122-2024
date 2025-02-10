import doctest

# Miguel: these are global variables, they come at the top of the
# file, after imports. It is bad practice to change a global
# variable during execution (which is what the style guide means by
# "avoid mutable global state") and you should not change them.
DAYS_IN_MONTH = 30
DAYS_IN_YEAR = 365


def check_value_with_rounding(value1, value2):
    return abs(value1 - value2) <= 0.02


def calculate_interest(balance, rate, transactions):
    """
    Calculate the compound interest paid monthly on the balance of
    a bank account, recursively.

    Args:
      balance: Current balance of the account at the start of the calculation.
      rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
      transactions: A list of tuples representing transactions (day, amount).
          Positive amounts are deposits, negative are withdrawals.

    Returns:
      The interest rate to be paid at the end of the month.

    Note: Each doc-test has a comment at the start describing the case.

    >>> # Simple example.
    >>> interest = calculate_interest(1000, 0.05, [])
    >>> check_value_with_rounding(4.02, interest)
    True
    >>> # Same example, in a different way.
    >>> interest = calculate_interest(0, 0.05, [(0, 1000)])
    >>> check_value_with_rounding(4.02, interest)
    True
    >>> # The interest rate has to compound daily.
    >>> interest = calculate_interest(10000, 0.05, [])
    >>> check_value_with_rounding(40.18, interest)
    True
    >>> # Example with a list of transactions.
    >>> transactions = [(5, 500), (10, -200), (20, 100)]
    >>> interest = calculate_interest(1000, 0.05, transactions)
    >>> check_value_with_rounding(5.29, interest)
    True
    >>> # Transactions may not be ordered.
    >>> interest = calculate_interest(1000, 0.05, [(20, 1000), (10, 1000)])
    >>> check_value_with_rounding(8.03, interest)
    True
    >>> # Transactions may happen twice in a day.
    >>> transactions = [(20, 500), (20, 500), (10, 1000)]
    >>> interest = calculate_interest(1000, 0.05, transactions)
    >>> check_value_with_rounding(8.03, interest)
    True
    """

    ###########################################################################
    #
    # TODO: Complete the rest of this function, until the next heading
    # similar to this one
    #
    # Note: the only thing this function should do is call the
    # recursive function with the right parameters. That's why it's
    # called a "wrapper" or "helper" function: it wraps around the
    # recursive function, and helps you call it with the right
    # parameters.
    #
    ###########################################################################

    new_balance = calculate_balance_recursive(balance, rate, transactions)

    transaction_sum = sum(t[1] for t in transactions if t[0] < DAYS_IN_MONTH)

    return new_balance - balance - transaction_sum

    ###########################################################################
    #
    # Your function should end here. You can write or edit code below
    # this point to help you solve the assignment, but it will not be
    # tested nor graded.
    #
    ###########################################################################


def calculate_balance_recursive(balance, rate, transactions, day=0):
    """
    Recursive inner function.
    """

    # Daily interest rate, that compounds to the annual rate.
    daily_rate = (1 + rate) ** (1 / DAYS_IN_YEAR) - 1

    ###########################################################################
    #
    # TODO: Complete the rest of this function, until the next heading
    # similar to this one. Your recursive function should have the
    # terminal condition (n = 0 in the factorial case) and the
    # recursive call ((n-1)! in the factorial case).
    #
    ###########################################################################

    # Terminal case: if the current day exceeds the days in the month,
    # return the final balance.
    if day >= DAYS_IN_MONTH:
        return balance

    # Apply transactions for the current day.
    for transaction_day, amount in transactions:
        if transaction_day == day:
            balance += amount

    balance *= (1 + daily_rate)

    # Recur to the next day, updating the balance with compound interest.
    return calculate_balance_recursive(balance, rate, transactions, day + 1)

    ###########################################################################
    #
    # Your function should end here. You can write or edit code below
    # this point to help you solve the assignment, but it will not be
    # tested nor graded.
    #
    ###########################################################################


tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
if 0 < tests_run:
    assert 0 == tests_failed, 'Some doc-tests failed, exiting...'
    msg = ["*" * 20,
           "",
           "Success! your doc-tests pass!",
           "",
           "*" * 20]
    print("\n".join(msg))
else:
    print('Unable to run doc-tests, please see Miguel!')

# Example usage:
initial_balance = 1000
annual_rate = 0.05

# Transactions: day 5 deposit 500, day 10 withdraw 200, day 20 deposit 100.
transactions = [(5, 500), (10, -200), (20, 100)]

interest = calculate_interest(initial_balance, annual_rate, transactions)

print(f"Interest to be paid at the end of the month: ${interest:.2f}")
