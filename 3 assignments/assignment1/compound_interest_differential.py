import doctest


def calculate_interest_differential(balance,
                                    baseline_rate,
                                    bonus_rate,
                                    transactions):
    """
    Calculate the compound interest paid monthly on the balance of a
    bank account.

    Args:
      balance: Current balance of the account at the start of the calculation.
      rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
      transactions: A list of tuples representing transactions (day, amount).
          Positive amounts are deposits, negative are withdrawals.

    Returns:
      The interest rate to be paid at the end of the month.

    Note: Each doc-test has a comment at the start describing the case.
    
    >>> # Simple example.
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, [])
    >>> print("%.2f" % i)
    3.23
    >>> # Simple example, constructed another way.
    >>> i = calculate_interest_differential(0, 0.02, 0.04, [(0, 1000)])
    >>> print("%.2f" % i)
    3.23
    >>> # Example with a withdrawal.
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, [(29, -1)])
    >>> print("%.2f" % i)
    1.63
    >>> # Example with credits and withdrawals.
    >>> transactions = [(5, 500), (10, -200), (20, 100)]
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, transactions)
    >>> print("%.2f" % i)
    2.14
    >>> # The interest rate has to compound daily.
    >>> i = calculate_interest_differential(10000, 0.02, 0.05, [])
    >>> print("%.2f" % i)
    40.18
    >>> # Transactions may happen twice in a day.
    >>> interest = calculate_interest(1000, 0.05, [(20, 1000), (20, 1000)])
    >>> print("%.2f" % interest)
    """

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
baseline_rate = 0.02
bonus_rate = 0.04

# Transactions: day 5 deposit 500, day 10 withdraw 200, day 20 deposit 100.
transactions = [(5, 500), (10, -200), (20, 100)]

interest = calculate_interest_differential(initial_balance,
                                           baseline_rate,
                                           bonus_rate,
                                           transactions)

print(f"Interest to be paid at the end of the month: ${interest:.2f}")
