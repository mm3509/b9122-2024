import doctest

from ex2 import check_value_with_rounding


import compound_interest as exercise11


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
    >>> check_value_with_rounding(3.23, i)
    True
    >>> # Simple example, constructed another way.
    >>> i = calculate_interest_differential(0, 0.02, 0.04, [(0, 1000)])
    >>> check_value_with_rounding(3.23, i)
    True
    >>> # Example with a withdrawal.
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, [(29, -1)])
    >>> check_value_with_rounding(1.63, i)
    True
    >>> # Example with credits and withdrawals.
    >>> transactions = [(5, 500), (10, -200), (20, 100)]
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, transactions)
    >>> check_value_with_rounding(2.14, i)
    True
    >>> # The interest rate has to compound daily.
    >>> i = calculate_interest_differential(10000, 0.02, 0.05, [])
    >>> check_value_with_rounding(40.18, i)
    True
    """

    # Miguel: note the syntax for operating through a list of
    # tuples. Commas in assignment "unpack" a tuple. My syntax is
    # equivalent to this, but is shorter:
    #
    # for t in transactions:
    #     _, amount = t

    rate = bonus_rate
    for _, amount in transactions:
        if amount < 0:
            rate = baseline_rate

            # As soon as we have one withdrawal, the baseline rate
            # applies and we can exit the loop.
            break

    return exercise11.calculate_interest(balance, rate, transactions)


if __name__ == "__main__":
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 == tests_run:
        print("Unable to run doc-tests")
    elif 0 != tests_failed:
        print("Some doc-tests failed")
    else:
        print("Your doc-tests pass, congratulations!")
