# Assignment 3 (afternoon section, MS Accounting + MS Marketing)

Unliked previous assessments, this assignment has 140 points. Bonus questions are optional, but will increase your grade in this assignment up to a maximum of 140 points.

For all these questions:

1. complete the relevant Python function(s) and submit it on Gradescope without changing the name of the file, of the function(s), nor the number and order of arguments;

2. all your functions should have doc-tests and apply defensive programming (see the FAQ section for what is a doc-tests and examples);

3. you can define a separate function that you call in the original function that I wrote.

## Exercise 1: string manipulation (30 points)

This function takes a string and converts it to title case. Title case means that the first letter is uppercase and every letter at the start of a word is upper case (unless they are a "stopword", which in this case will only be four of them: "a", "the", "of", "and").

You can use these Python string methods:

- `.upper()` converts to uppercase,
- `.lower()` converts to lower case
- `.split(separator)` splits a string on a separator and returns a list
- `separator.join(some_list)`, which does the opposite of `.split()`: it take a list as argument and returns the elements of the list with `separator` (or any other string) in between them.

You are NOT allowed to use the built-in Python function `.title()`.

I added one doc-test for you. You will have to add two more.

## Exercise 2: debugging and dictionary manipulation (30 points)

This function is for you to debug; do NOT write doc-tests for it, and do not expect things to go wrong.

CBS has two email adddresses for the same person. These different usernames are called "aliases" (similar to a nickname). For example, for me they could be:

- UNI: mm3509@columbia.edu
- GSB, with graduation year: MMorin26@gsb.columbia.edu

Some students have this GSB email, other students are not from CBS and do not.

This function takes a dictionary with details on students' grades. The keys of the dictionary are the UNIs in lowercase. The value of the dictionary is **another** dictionary with the following keys:

- `"gsb"`: the CBS username with graduation year, if the student is a student at CBS
- `"grade"`: the grade

This function does this search, but it has a bug. Find the bug, fix it, and add a comment explaining the bug.

## Exercise 3: NumPy manipulation (30 points)

This file computes the variance of the log-growth rate of a time series. The log growth rate between times `s` and `t` is:

```
log_growth_rate = log (X_t / X_s) = log(X_t) - log(X_s)
```

This function takes as argument a NumPy 2D array of size `(N, 1)` (comparable to a column vector). Assume that the input is a time series at the yearly frequency, i.e. each observation in the input data corresponds to a year in a continuous sequence. You should compute the log growth rate from one year to the next. You should then return the variance of this log growth rate.
You can assume that, if the argument is an `(N, 1)` array, it only has positive numbers (no zeroes). If it did have a zero, then NumPy would return `NaN`, or not-a-number.

You should use NumPy functions like `numpy.log()` and `numpy.var()`.

## Exercise 4: Integral calculation (50 points)

A Riemann integral is the successive approximation of the integral of a function, as in this image:

<img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Riemann_integral_regular.gif" />

For clarity, I will refer to the function in your exercise as "your Python function", and to the function whose integral you'll compute as the "my analytic function". My analytic function will be an argument to your Python function (indeed, Python can store functions into variables and you can pass them around; it's a programming paradigm called "functions as first-class citizens"). For example, if `fn` is the argument to your Python function, you can get its value at 0 with `fn(0)`.

Your Python function computes one step iteration in this approximation of the integral of a function. Your function takes as arguments:

- my analytic function

- a start for the range (interval) where to compute the integral

- an end for the range (interval) where to compute the integral

- an integer for the number of segments

Your Python function should use the value of my analytic function at the midpoint; for example, if the start is 0, then end is 1, and the number of segments is 5, you should use the values of my analytic function at 0.1, 0.3, 0.5, 0.7, and 0.9.

Your function should have doc-tests using the NumPy square function, `numpy.square()`. You can check if a variable is a function with the function `callable()`, e.g. `callable(square)` returns `True`.

Your Python function should return the approximate value of the integral of my analytic function over the given range and with the given number of segments.

## Exercise 5: reading and parsing a CSV file (bonus question, 15 points)

A CSV file (Comma-Separated Values) is a common format for data storage. It is similar to Excel's XLS, but it only stores data or values (no formulas). It has a delimiter, most commonly a comma, to separate columns; and the delimiter to separate rows is usually a newline (the value in Python is `"\n"`).

For example, a CSV file with income by county in the US would look like this:

```
county,state,income
Kings,NY,1234
Queens,NY,6789
```

Reading and understanding a file in this way is called "parsing."

You cannot use module functions like `pandas.readcsv()` nor `csv.reader()`.

### Imperative function

Complete the function `parse_csv_imperative()` in imperative style. It takes as input a string with a line in the CSV file, and returns a list with the value of each cell, for example on the first line it would return:

```
["county", "state", "income"]
```

This function should check for the edge case where the argument is not a string.

### Recursive function

Sometimes, the value of a cell has the delimiter itself, for example "Washington, D.C." In this case, the CSV format stores it with quotes around the name, for example:

```
county,state,income
"Washington, D.C.",DC,1234
```

Complete the function `parse_csv_recursive()` to handle this case and remove the quotes (the imperative function above is not expected to handle this case, which is much easier to handle recursively). For the second line in the above example, it should return:

```
['Washington, D.C.', 'DC', '1234']
```

Also complete the function `parse_csv_recursive_wrapper()`. It should only check for edge cases, then it should call the recursive function (the "wrapper" function is called so because it wraps around the recursive function).

The wrapper function should check for the edge case where the argument is not a string.

### Reading from a file

Complete the function `read_csv()` that takes as argument a filepath and returns a list of lists with the contents of the file.

You should check that the filepath exists with `import os` and `os.path.exists()`. If you don't know how to read files, check the Jupyter notebook called `Review` in lecture 6. The function should have no other doc-tests because we can't assume that a file exists on the computer running the system.

The function should call the recursive function. You should ignore empty lines. This function should also check for the edge case where the filepath in the argument is missing.

