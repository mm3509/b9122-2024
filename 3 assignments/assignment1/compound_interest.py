import doctest


def calculate_interest(balance, rate, transactions):
    """
    Calculate the compound interest paid monthly on the balance of
    a bank account.

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
    >>> print("%.2f" % interest)
    4.02
    >>> # Same example, in a different way.
    >>> interest = calculate_interest(0, 0.05, [(0, 1000)])
    >>> print("%.2f" % interest)
    4.02
    >>> # The interest rate has to compound daily.
    >>> interest = calculate_interest(10000, 0.05, [])
    >>> print("%.2f" % interest)
    40.18
    >>> # Example with a list of transactions.
    >>> transactions = [(5, 500), (10, -200), (20, 100)]
    >>> interest = calculate_interest(1000, 0.05, transactions)
    >>> print("%.2f" % interest)
    5.29
    >>> # Transactions may not be ordered.
    >>> interest = calculate_interest(1000, 0.05, [(20, 1000), (10, 1000)])
    >>> print("%.2f" % interest)
    8.03
    >>> # Transactions may happen twice in a day.
    >>> interest = calculate_interest(1000, 0.05, [(20, 1000), (20, 1000)])
    >>> print("%.2f" % interest)
    6.69
    >>> # The interest from a transaction has to compound too.
    >>> interest = calculate_interest(10000, 0.05, [(10, 10000)])
    >>> print("%.2f" % interest)
    66.95
    """

    days_in_month = 30  # Assume a 30-day month.
    days_in_year = 365  # Assume a normal year.

    # Daily interest rate, that compounds to the annual rate.
    daily_rate = (1 + rate) ** (1 / days_in_year) - 1

    ############################################################################
    #
    # TODO: Complete the rest of this function, until the next heading
    # similar to this one
    #
    ############################################################################
    return -1








    ############################################################################
    #
    # Your function should end here. You can write or edit code below
    # this point to help you solve the assignment, but it will not be
    # tested nor graded.
    #
    ############################################################################



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
