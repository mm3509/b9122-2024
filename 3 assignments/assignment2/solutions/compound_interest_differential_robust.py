import doctest

###########################################################################
#
# TODO: Complete this section to import modules, until the next
# heading similar to this one
#
###########################################################################

import compound_interest_differential as exercise12


DAYS_IN_MONTH = 30


def check_number(value, argument_name):
    if not isinstance(value, (int, float)):
        raise ValueError("%s must be a number" % argument_name)
    if value < 0:
        raise ValueError("%s must be positive" % argument_name)


def check_dollar_amount(value, argument_name):
    amount_in_cents = value * 100
    discrepancy = amount_in_cents - round(amount_in_cents)
    if discrepancy > 1e-5:
        raise ValueError("%s must be a round number of cents" %
                         argument_name)


def check_transactions(transactions):
    if not isinstance(transactions, list):
        raise ValueError("transactions must be a list")

    for t in transactions:
        if not isinstance(t, tuple):
            raise ValueError("transactions must be a list of tuples")

        if len(t) != 2:
            raise ValueError("a transaction must be a tuple of size 2")
        day, amount = t
        if not isinstance(day, int):
            raise ValueError("transaction day must be an integer")

        if day < 0 or day >= DAYS_IN_MONTH:
            raise ValueError("transactions must happen in range(30)")

        check_dollar_amount(amount, "transaction amount")


###########################################################################
#
# Your imports should end here.
#
###########################################################################

def calculate_interest_differential(balance,
                                    baseline_rate,
                                    bonus_rate,
                                    transactions):
    """
    Calculate the compound interest paid monthly on the balance of a
    bank account, recursively.

    Args:
      balance: Current balance of the account at the start of the calculation.
      rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
      transactions: A list of tuples representing transactions (day, amount).
          Positive amounts are deposits, negative are withdrawals.

    Returns:
      The interest rate to be paid at the end of the month.

    ###########################################################################
    #
    # TODO: Complete the rest of the doc-string, until the next heading
    # similar to this one
    #
    ###########################################################################
    >>> bal = 1000
    >>> base = 0.02
    >>> bonus = 0.04
    >>> trans = []
    >>> calculate_interest_differential("abcd", base, bonus, trans)
    Traceback (most recent call last):
        ...
    ValueError: balance must be a number
    >>> calculate_interest_differential(-1000, base, bonus, trans)
    Traceback (most recent call last):
        ...
    ValueError: balance must be positive
    >>> calculate_interest_differential(10.0333, base, bonus, trans)
    Traceback (most recent call last):
        ...
    ValueError: balance must be a round number of cents
    >>> calculate_interest_differential(bal, "abcd", bonus, trans)
    Traceback (most recent call last):
        ...
    ValueError: rate must be a number
    >>> calculate_interest_differential(bal, base, "abcd", trans)
    Traceback (most recent call last):
        ...
    ValueError: rate must be a number
    >>> calculate_interest_differential(bal, -0.01, bonus, trans)
    Traceback (most recent call last):
        ...
    ValueError: rate must be positive
    >>> calculate_interest_differential(bal, base, -0.01, trans)
    Traceback (most recent call last):
        ...
    ValueError: rate must be positive
    >>> calculate_interest_differential(bal, base, bonus, "abcd")
    Traceback (most recent call last):
        ...
    ValueError: transactions must be a list
    >>> calculate_interest_differential(bal, base, bonus, [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: transactions must be a list of tuples
    >>> calculate_interest_differential(bal, base, bonus, [(0, 100), 2])
    Traceback (most recent call last):
        ...
    ValueError: transactions must be a list of tuples
    >>> calculate_interest_differential(bal, base, bonus, [(0, 100, "abcd")])
    Traceback (most recent call last):
        ...
    ValueError: a transaction must be a tuple of size 2
    >>> calculate_interest_differential(bal, base, bonus, [(10.5, 100)])
    Traceback (most recent call last):
        ...
    ValueError: transaction day must be an integer
    >>> calculate_interest_differential(bal, base, bonus, [(-1, 100)])
    Traceback (most recent call last):
        ...
    ValueError: transactions must happen in range(30)
    >>> calculate_interest_differential(bal, base, bonus, [(30, 100)])
    Traceback (most recent call last):
        ...
    ValueError: transactions must happen in range(30)
    >>> calculate_interest_differential(bal, base, bonus, [(10, 10.333)])
    Traceback (most recent call last):
        ...
    ValueError: transaction amount must be a round number of cents
    >>> calculate_interest_differential(bal, base, bonus, [(10, -1001)])
    Traceback (most recent call last):
        ...
    ValueError: balance cannot go negative
    >>> # Days are zero-indexed.
    >>> i = calculate_interest_differential(500, 0.02, 0.04, [(0, 500)])
    >>> exercise12.check_value_with_rounding(3.23, i)
    True

    ###########################################################################
    #
    # Your doc-string and doc-tests should end here.
    #
    ###########################################################################
    """

    check_number(balance, "balance")
    check_dollar_amount(balance, "balance")

    for rate in [baseline_rate, bonus_rate]:
        check_number(rate, "rate")

    check_transactions(transactions)

    current_balance = balance
    for _, amount in transactions:
        current_balance += amount
        if current_balance < 0:
            raise ValueError("balance cannot go negative")

    return exercise12.calculate_interest_differential(balance,
                                                      baseline_rate,
                                                      bonus_rate,
                                                      transactions)

    ###########################################################################
    #
    # TODO: Complete the rest of this function, until the next heading
    # similar to this one
    #
    ###########################################################################

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
initial_balance = 3000
baseline_rate = 0.02
bonus_rate = 0.04

# Transactions: day 5 deposit 500, day 10 withdraw 200, day 20 deposit 100.
transactions = [(5, 500), (10, -200), (20, 100)]


interest = calculate_interest_differential(initial_balance,
                                           baseline_rate,
                                           bonus_rate,
                                           transactions)

print(f"Interest to be paid at the end of the month: ${interest:.2f}")
