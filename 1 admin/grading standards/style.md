# Grading / guidance on style

We will build gradually over the term to a good coding style. I will add style rules gradually on GradeScope and you will get immediate feedback.

## Google Python Style Guide

For general guidance and examples of good style, please check the [Google Python Style
Guide here](https://google.github.io/styleguide/pyguide.html).

## Specific errors from GradeScope

For specific guidance on each error, for example `E225: missing whitespace around operator`, check a link such as this (replacing the end code, before `.html`, with your error code):

https://www.flake8rules.com/rules/W293.html

## Running style checks locally

You can run style checks locally (on your computer, without waiting
for a GradeScope report) by installing `flake8` from a shell:

```bash
pip install flake8
```

and then checking the style on this file (ignoring the same errors as GradeScope for assignment 2) with:

flake8 'FILEPATH' --ignore=E501,W504,E128,E127,E303,E251,W291,F401,W391,E302,E305,E241,E261,E231,E261,F841,E124,W292,W293,W503,W504

When you run this, or when it runs on Gradescope, you will get an error such as:

```
compound_interest.py:171:12: F821 undefined name 'days_in_monthh'
```

This indicates that the source of the error:

- is in the file `compound_interest.py`

- on line 171

- on the 12th character of the line

- the machine-readable error has code F821 (and you can read about it at    https://www.flake8rules.com/rules/F821.html )

- the human-readable error means that one variable name is not defined (in this case, it's a typo and has an extra `h` at the end)

## function length

For assignment 2 and the midterm, we expect functions to be under 40 lines (this feature is not yet on Autograder).

A statement that runs over multiple lines counts as one line, for example this long function call:

```python
return some_recursive_function(balance,
                               base_rate,
                               bonus_rate,
                               transactions,
                               recursive_counter + 1)
```

The treatment of edge cases that raise errors do not count as line length.

The treatment of edge cases that do raise errors are part of the function's logic and count towards function length.

## ternary operators

We encourage you to use ternary operators to make functions shorter. These operators condense the code and are still readable. The following three examples are equivalent, but they get shorter.

Here is a typical conditional:

```python
if a <= 0:
    b = "positive_or_zero"
else:
    b = "negative"
```

Here is the same result, but we initialize a variable at a default value:

```python
b = "positive_or_zero"
if a < 0:
    b = "negative"
```

And her is the same result with a "ternary" operator ("ternary" because it uses three arguments: `"positive_or_zero"`, the boolean `a >= 0`, and `"negative"`):

```python
b = "positive_or_zero" if a >= 0 else "negative"
```

## 80-character limit (assignment 3 onwards)

You now have to keep your lines of code under 80 characters.

Here is an example of a long line, over 80 characters:

``` python
if np.any(a <= 0):
    raise ValueError("All elements in the input array must be strictly positive.")
```

which you can refactor into two shorter lines under 80 characters:

``` python
if np.any(a <= 0):
    message = "All elements in the input array must be strictly positive."
    raise ValueError(message)
```

Here is another example of a long line in doc-tests, over 80 characters:

``` python
    >>> compute_variance_of_log_growth(np.array([[33], [21], [4], [81]]).astype(float))
```

which you can refactor into two shorter lines under 80 characters:

``` python
    >>> a = np.array([[33], [21], [4], [81]]).astype(float)
    >>> compute_variance_of_log_growth(a)
```

If one of your comments is a hyperlink and longer than 80 characters, please
add ` # noqa: E501` (which stands for "NO Quality Assurance" on this
style guideline, which has code 501) and it will be graded manually, for example:

```python
# Inspired by:
# https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/  # noqa: E501
```
