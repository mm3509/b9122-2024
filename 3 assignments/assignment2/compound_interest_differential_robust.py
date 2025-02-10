import doctest

###########################################################################
#
# TODO: Complete this section to import modules, until the next
# heading similar to this one
#
###########################################################################
pass

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

    ###########################################################################
    #
    # Your doc-string and doc-tests should end here.
    #
    ###########################################################################
    """

    ###########################################################################
    #
    # TODO: Complete the rest of this function, until the next heading
    # similar to this one
    #
    ###########################################################################
    return -1

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
baseline_rate = 0.02
bonus_rate = 0.04

# Transactions: day 5 deposit 500, day 10 withdraw 200, day 20 deposit 100.
transactions = [(5, 500), (10, -200), (20, 100)]

interest = calculate_interest_differential(initial_balance,
                                           baseline_rate,
                                           bonus_rate,
                                           transactions)

print(f"Interest to be paid at the end of the month: ${interest:.2f}")
