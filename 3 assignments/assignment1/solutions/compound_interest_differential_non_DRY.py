import doctest

from ex2 import check_value_with_rounding


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

    # Miguel: This whole code is repeated from 1.1. Import that file
    # and use that function instead!
    
    true_rate = (1 + bonus_rate) ** (1 / 365) - 1
    merged_dict = {}
    
    for day, amount in transactions:
        if day in merged_dict:
            merged_dict[day] += amount
        else:
            merged_dict[day] = amount
        if amount < 0:
            true_rate = (1 + baseline_rate) ** (1 / 365) - 1

    interest_compounded = 0

    # Miguel: numbers like 30 should be in variables at the top of the
    # function; and range(0, 30) is the same as range(30)
    for interest_day in range(0, 30):
        balance += merged_dict.get(interest_day, 0) 
        interest_compounded += balance * true_rate
        balance += balance * true_rate
    return round(interest_compounded, 2)


if __name__ == "__main__":
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 == tests_run:
        print("Unable to run doc-tests")
    elif 0 != tests_failed:
        print("Some doc-tests failed")
    else:
        print("Your doc-tests pass, congratulations!")
