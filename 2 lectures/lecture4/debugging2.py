import doctest
import datetime

def compute_interest(balance, rate, day, month):
    """
    Compute whether a customer should be paid interest, only on
    January 2nd of a year.

    Args:
      balance:
        A number for the balance on the account.

      rate:
        A number for the current interest rate.

      day:
        An integer for the day of the month under consideration (not 0-indexed)

      month:
        An integer for the month (not 0-indexed)

    Returns:
      A number with the interest to be paid.
    
    >>> today = datetime.datetime.today()
    >>> i = compute_interest(1000, 0.05, 27, 9)
    The customer should not be paid interest on day 27 and month 9.
    >>> i
    0
    >>> i = compute_interest(1000, 0.05, 2, 1)
    The customer should be paid this interest on day 2 and month 1: 50.0.
    >>> i
    50.0

    """

    # Note: in this exercise, days and months are NOT zero-indexed.

    # TODO: add a variable for the value of each part of this
    # comparison, then inspect the value, e.g.:
    # a = 2 == day
    # print(a)
    # b = 1 == month
    # print(b)
    # print(a & b)
    
    if 2 == day & 1 == month:
        interest = balance * rate
        msg = ("The customer should be paid this interest on day"
               " %s and month %s: %3.1f.") % (interest, day, month)
        
    else:
        interest = 0
        msg = ("The customer should not be paid interest on day %s and" +
               " month %s.") % (day, month)
        
    print(msg)
    return interest


compute_interest(1000, 0.04, 2, 1)

doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'

print("Your doc-tests pass, congratulations!")

