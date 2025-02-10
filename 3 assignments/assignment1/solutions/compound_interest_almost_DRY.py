import doctest

from ex2 import check_value_with_rounding


def calculate_interest(balance, rate, transactions):
    """
    Almost DRY solution from a student.
    
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
    >>> interest = calculate_interest(1000, 0.05, [(20, 1000), (20, 1000)])
    >>> check_value_with_rounding(6.69, interest)
    True
     """

    days_in_month = 30
    days_in_year = 365

    daily_rate = (1 + rate) ** (1 / days_in_year) - 1

    interest = 0.0

    # Miguel: range(0, days_in_month) is the same as range(days_in_month).
    for day in range(0, days_in_month):
        for i in range(len(transactions)):
            if transactions[i][0] == day:
                balance += transactions[i][1]

        # Miguel: starting in assignment 2, operators like * will need spaces around them.
        interest += (balance + interest)*daily_rate

    return interest


if __name__ == "__main__":
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 == tests_run:
        print("Unable to run doc-tests")
    elif 0 != tests_failed:
        print("Some doc-tests failed")
    else:
        print("Your doc-tests pass, congratulations!")
