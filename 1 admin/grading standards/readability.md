# Guidance / grading on readability

This course emphasizes writing code that is easy to read and to maintain.

DRY and refactoring is a big part of readability. This guide covers the part of readability after DRY, which is more at "high-level" and thinking how to structure code (as opposed to "low-level", writing code).

## Code is more often read than written

Code has two very different audiences:

- computers, which execute code
- humans, who read and modify code

Here are a few quotes that explain the difference between the two.

> Programs must be written for people to read, and only incidentally for machines to execute. (Harold Abelson and Gerald Jay Sussman, teachers at MIT)

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand. (Martin Fowler)

> The function of good software is to make the complex appear to be simple. (Grady Booch)

> Code is more often read than written.

> Programming is the art of telling a computer what to do. (Donald Knuth)

Most of burden in code happens maintaining it and editing it, after it's written. Your job will often be to read someone else's code and try to understand it.

For example, imagine I were hired into a bank, and my first task is to address on customer's complaint that the interest paid at the end of the month seems wrong. The more readable the code, the faster I will understand it, and the easier it will be to debug.

## Quality assurance

Computers happily execute any piece of code; the real art is to write code that assures the humans reading and maintaining it that the computer is doing what we expect. This is known as "quality assurance".

Some means of quality assurance are black-and-white and can be automatically checked:

- the doc-tests pass

- a style check (also called a "linter") throws no errors

These are already coded into GradeScope.

Other means of quality assurance are more subtle and require developing judgment.

## Standards or assignment 2 onwards

Standards for assignment 2 and the midterm are still loose. I will tighten them over the term.

### Choose good variable names

Here is an example submission from assignment 1:

```python
def calculate_interest(balance, rate, transactions):

    days_in_month = 30
    days_in_year = 365
    interest = 0
    days_passed = 0
    
    for i in transactions:

        interest += ((1 + rate) ** (1 / days_in_year)) ** (i[0] - days_passed) * balance - balance
        balance = balance + i[1]
        days_passed = i[0]
```

The element `i` in the transaction list is used three times. I find it hard to read `i[0]` and remember that it's a day, or `i[1]` and remember that it's a dollar amount. It is also easy to introduce a bug when editing this code, e.g. if I want to compute the total sum of transactions, I could easily write `total_transactions += i[0]`.

A better choice of variable names makes the code easier to read and less prone to bugs.

```python
def calculate_interest(balance, rate, transactions):

    days_in_month = 30
    days_in_year = 365
    interest = 0
    days_passed = 0
    
    for i in transactions:
        day = i[0]
        dollar_amount = i[1]
        interest += ((1 + rate) ** (1 / days_in_year)) ** (day - days_passed) * balance - balance
        balance = balance + dollar_amount
        days_passed = day
```

An even better solution is to make use of "tuple unpacking", so we iterate through the transactions list and assign these variable names in one line instead of three:

```python
def calculate_interest(balance, rate, transactions):

    days_in_month = 30
    days_in_year = 365
    interest = 0
    days_passed = 0
    
    for day, dollar_amount in transactions:

        interest += ((1 + rate) ** (1 / days_in_year)) ** (day - days_passed) * balance - balance
        balance = balance + dollar_amount
        days_passed = day
```

## Standards for assignment 3 onwards

### Refactor functions from wide / horizontal to long / vertical

Consider this function that returns whether a year is a leap year:

``` python
def is_leap_year(year):
    return (year % 4) and not ((year % 100) and not (year % 400))
```

The body of the function is wide with 65 characters and hard to read: should it be `and` or `or`? Are parentheses in the right place? Is it correctly using the conversion of integers to booleans?
Because it's hard to read, it's also hard to find the bug.

Instead, from assignment 3 onwards, I want you to write functions that are long / vertical and use early returns:

``` python
def is_leap_year(year):

    if year % 400 == 0:
        return True
        
    if year % 100 == 0:
        return False
        
    return year % 4 == 0
```

### Align the "happy path" to the left edge / line of sight

Here is an example submission from Assignment 3. The happy path is nested in one other level of indentation and is hard to read:

``` python
def convert_to_title_case(string):

    if isinstance(string, str):
        list_of_words = string.split(" ")
        title_words = []
        
        # other code
    else:
        raise TypeError("The Input argument should be a String.")
```

A more readable code flips the logic and deals with the edge case first. Then, the "happy path", i.e. the path taken by the most common case, is at one level of indentation (the left edge) instead of two levels, which makes it more readable:

``` python
def convert_to_title_case(string):

    if not isinstance(string, str):
        raise TypeError("The Input argument should be a String.")
        
    list_of_words = string.split(" ")
    title_words = []
```

## Goal

Here is quote from Hoare:

> There are two ways to write code: write code so simple there are obviously no bugs in it, or write code so complex that there are no obvious bugs in it.

Our goal for this course is for you to write the former.

Here is the standard we will apply for assignment 5 and the final, quoted from the syllabus:

> The code is easy to read and understand; variable, function and object names are appropriate and convey meaning; functions are clear in what they do; they follow the "happy path". The code is so clear in what it does that there are obviously no bugs. 
