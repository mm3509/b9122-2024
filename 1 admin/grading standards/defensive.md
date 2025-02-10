# Defensive programming

## Check arguments

When you write a function, you should anticipate that it will be called with the wrong arguments and raise a ValueError.

For example, this function computes the area of a rectangle:

```
def compute_area(height, width):
    return height * width
```

but when called with "2" and 3, it returns "222".

You should raise a `ValueError` when the arguments are not of the type you expect, for example:


```
def check_argument(a):
    if not isinstance(a, (float, int)):
        raise ValueError("Input must be a number")

def compute_area(height, width):
    check_argument(height)
    check_argument(width)
    return height * width
```

## `ValueError` or `TypeError`?

The best practice when checking arguments is to raise a `ValueError`. Here is a quote from the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#244-decision):

> raise a `ValueError` to indicate a programming mistake like a violated precondition, such as may happen when validating function arguments.

[This thread on StackOverflow](https://stackoverflow.com/questions/256222/which-exception-should-i-raise-on-bad-illegal-argument-combinations-in-python) has a divided opinion on using `ValueError` or `TypeError`. Therefore, as of October 19th, 2024, Autograder will accept both `ValueError` and `TypeError` around corner cases.
