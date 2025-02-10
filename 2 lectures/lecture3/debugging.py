import datetime

def pay_interest(balance, rate, day, month):

    if 2 == day & 1 == month:
        interest = balance * rate
        print("On day %s and month %s, the customer should be paid this interest: %3.1f" % (day, month, interest))
    else:
        print("The customer should not be paid interest on day %s and month %s" % (day, month))


today = datetime.datetime.today()
pay_interest(1000, 0.04, today.day, today.month)

pay_interest(1000, 0.04, 2, 1)
