import doctest

from ex2 import check_value_with_rounding


def calculate_interest(balance, rate, transactions):
    """
    Incorrect solution from a student, not obvious why.
    
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

    start_balance = balance
    for day in range(0, days_in_month):
        for i in range(len(transactions)):
            if transactions[i][0] == day:
                balance += daily_rate * (balance + transactions[i][1])

    interest = balance - start_balance
    return interest

interest = calculate_interest(1000, 0.05, [])
print(interest)


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
