# Guidance / grading on DRY / Don't Repeat Yourself

This document explains our human judgment on what constitutes "DRY" code.

As a rule-of-thumb, if you ever find yourself copy-pasting code, consider "refactoring" that piece of code you were about to copy into:

- a variable that you use multiple times

- a function that you can call

- a module that you can import

## example from math

The concept of "refactoring" in programming is similar to "factoring" in math.

This expression is called "distributed":

```python
a + a + a + a + a
```

and has the same value as this expression, which is "factored":

```python
5 * a
```

but the latter is shorter, simpler, easier to read, and less likely to have bugs.

## simple rules-of-thumb

### Use augmented assignment operators

When peforming arithmetic operations to update a variable, use the operators `+=`, `-=` and `*=`. These are called **augmented assignment operators** because they combine an operation with an assignment.

That is, the following four arithmetic operations:

```python
a = a + 1
b = b - 2
c = c * 3
d = d / 4
```

are the same as, and should be replaced by:

```python
a += 1
b -= 2
c *= 3
d /= 4
```

This saves about one third of characters and reading time.

### Use default arguments

To get a range, for example from `0` to `30`, use the default argument for the start, which is zero.

That is, instead of writing:

```python
range(0, 30)
```

you should write:

```
range(30)
```

### do not use re-assignment when an in-place function would do

To sort a list, you could use this code:

```python
transactions = sorted(transactions)
```

but the following in-place function is shorter and does not repeat the variable name:

```python
transactions.sort()
```

### Write functions under 20 lines

Your functions should be small, under 20 lines of code.

## examples from assignment 1

### exercise 1.1

Here is an example of WET code:

```python
interest = 0
days_passed = 0
if len(transactions) > 0:
    for i in transactions:
        interest = interest + ((1 + rate) ** (1 / 365)) ** (i[0] - days_passed) * balance - balance
        balance = balance + i[1]
        days_passed = i[0]
    interest += ((1 + rate) ** (1 / 365)) ** (days_in_month - days_passed) * balance - balance
elif len(transactions) == 0:
    interest = interest + ((1 + rate) ** (1 / 365)) ** days_in_month * balance - balance
```

In the case of no transactions, `days_passed = 0`, so the last line and the third-to-last line are the same and should be "refactored", which eliminates three lines of code (or 30% of the original lines):

```python
interest = 0
days_passed = 0
for i in transactions:
    interest = interest + ((1 + rate) ** (1 / 365)) ** (i[0] - days_passed) * balance - balance
    balance = balance + i[1]
    days_passed = i[0]
interest = interest + ((1 + rate) ** (1 / 365)) ** (days_in_month - days_passed) * balance - balance
```

Furthermore, the two lines starting with `interest = interest + ...` can be refactored with an augmented assignment operator: `interest += ...`, and the long formula to compute the interest is also repeated and should be refactored into a function, for example:

```python
DAYS_IN_YEAR = 365

def compute_interest_over_period(balance, rate, num_days):
    return (((1 + rate) ** (1 / DAYS_IN_YEAR)) ** num_days - 1) * balance


interest = 0
days_passed = 0
for i in transactions:
    interest += compute_interest_over_period(balance, rate, i[0] - days_passed)
    balance = balance + i[1]
    days_passed = i[0]
interest += compute_interest_over_period(balance, rate, days_in_month - days_passed)
```

### exercise 1.2

Here is an example of WET code: 

```python
def calculate_interest_differential(balance,
                                    baseline_rate,
                                    bonus_rate,
                                    transactions):
    """ Doc-string ommitted for clarity. """
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
    
    for interest_day in range(30):
        balance += merged_dict.get(interest_day, 0) 
        interest_compounded += balance * true_rate
        balance += balance * true_rate
    round(interest_compounded, 2)
```

Notice that, if the baseline rate applies, the formula for it is inside two indentations. If we have to change the number of days in a year, for example because of a leap year (366), or to calendar days (360, twelve times 30), it will be easy to introduce a bug by changing it only at the top.

Instead, DRY code uses the function defined in the above exercise. A Python file is a module and you can import it!


```python
from compound_interest_solution_DRY import calculate_interest

def calculate_interest_differential(balance,
                                    baseline_rate,
                                    bonus_rate,
                                    transactions):
    """ Doc-string ommitted for clarity. """
    rate = bonus_rate
    for _, amount in transactions:
        if amount < 0:
            rate = baseline_rate
            break

    return calculate_interest(balance, rate, transactions)
```
## example from assignment 4 (morning)

In assigment 4, you had to program a function to determine whether a string was valid. This code is not DRY because if we want to add `()` as a valid string, we have to add them in three places:

```
def is_valid(s):
    """
    >>> is_valid("{}[]{}")
    True
    """

    stack = []
    matching_bracket = {']': '[', '}': '{'}

    for char in s:
        if char in '[{':  # <- not DRY
            stack.append(char)
        elif char in ']}':  # <- not DRY
            if not stack or stack.pop() != matching_bracket[char]:
                return False
        else:
            return False

    return not stack
```

instead, this code is DRY:

```
def is_valid(s):
    """
    >>> is_valid("{}[]{}")
    True
    """

    stack = []
    matching_bracket = {']': '[', '}': '{'}

    for char in s:
        if char in matching_brackets.values():  # <- changed here
            stack.append(char)
        elif char in matching_brackets.kesy():  # <- changed here
            if not stack or stack.pop() != matching_bracket[char]:
                return False
        else:
            return False

    return not stack
```

