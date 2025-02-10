# Midterm exam (in-person, for morning section)

## Miguel Morin, (c) 2024

For all these questions:

1. complete the relevant Python function and submit it on Gradescope without changing the name of the file or of the functions;

2. you can import other modules, including those you wrote yourself (to be DRY);

3. all your functions should have doc-tests and apply defensive programming (see the FAQ section for what is a doc-tests and examples).

**Doc-tests**: For many of these questions, you'll have to write doc-tests for normal and edge cases, at least 3 doc-tests per file. The text of the question will tell you whether you have to write doc-tests; the Python file will also have a note whether to write them or not. In any case, Gradescope will tell you when it expects doc-tests. You can read the FAQ at the end of this document to know how to write doc-tests. When using strings in doc-tests, you should use single quotes.

You can write helper functions to keep your code DRY. Do not change the name of the function in the Python file or Gradescope will not find it.

Bonus questions are optional, but will increase your grade up to a maximum of 100 points. They serve as insurance **within** the exam and compensate when you get less than full marks on another question. They DO NOT serve as insurance **across** exams and DO NOT compensate when you get less than full marks on another exam.

At the end, you have to submit your files on Canvas. This is how we ensure that you are using Proctorio until the end. We will compare the two submissions and use the one on Canvas if they are different.

# Penalties

This exam has strict rules and the following penalties:

- 1 point for talking during or disrupting the exam (except to instructors)

- 5 points for not taking your assigned seat

- 5 points for using an electronic device other than one computer, because we cannot monitor it with Proctorio

- 10 points for submitting only on Gradescope and not on Canvas (otherwise, we're not sure you used Proctorio until the end)

- up to 50 points for using generative AI, which includes Google Search

# Exercise 1: string manipulation (10 points)

This function takes a string and converts it to title case. Title case means that the first letter is uppercase and every letter at the start of a word is upper case (unless they are a "stopword", which in this case will only be four of them: "a", "the", "of", "and").

You can use these Python string methods:

- `.upper()` converts to uppercase,
- `.lower()` converts to lower case
- `.split(separator)` splits a string on a separator and returns a list
- `separator.join(some_list)`, which does the opposite of `.split()`: it take a list as argument and returns the elements of the list with `separator` (or any other string) in between them.

You are not allowed to use the built-in Python function `.title()`.

I added one doc-test for you. You will have to add two more.

# Exercise 2: debugging and dictionary manipulation (10 points)

This function is for you to debug; do NOT write doc-tests for it, and do not expect things to go wrong.

CBS has two email adddresses for the same person. These different usernames are called "aliases" (similar to a nickname). For example, for me they could be:

- UNI: mm3509@columbia.edu
- GSB, with graduation year: MMorin26@gsb.columbia.edu

Some students have this GSB email, other students are not from CBS and do not.

This function takes a dictionary with details on students' grades. The keys of the dictionary are the UNIs in lowercase. The value of the dictionary is **another** dictionary with the following keys:

- `"gsb"`: the CBS username with graduation year, if the student is a student at CBS
- `"grade"`: the grade

This function does this search, but it has a bug. Find it and fix it.

# Exercise 3: string manipulation and recursion (15 points)

When I write messages for you on GradeScope, I take care to print them in lines less than 80 characters long. More than 80 characters in a line is hard to read, which is why newspapers print articles in columns. Furthermore, a best practice in programming is to never exceed 80 characters per line (which I'll start enforcing in assignment 3).

Here, we take a string and return a list of lines containing the same contents, but where each line has 80 characters or less. This is called "refilling". Some common sense rules are:

- only split a word across two list elements if it's over 80 characters long. Otherwise, split it at a the last space in the first 80 characters
- do not return a space at the start of an element, because it looks ugly.

You should write a recursive "helper" function that does this work, and a non-recursive "wrapper" function that handles the edge cases and calls the helper/recursive function. Gradescope will ONLY call the wrapper function.

In order to write short doc-tests, the functions also take an argument `max_chars`, set at 80 by default. This way, you do not need to write 80 characters in the doc-tests to check the functionality.

You can use this Python string method:
- `haystack.rfind(needle)` finds the last index of `needle` in `haystack`; it returns -1 if `needle` is not found. It's similar to find but reversed, from the end of `haystack`.

# Exercise 4: NumPy manipulation (12 points)

This file computes the variance of the log-growth rate of a time series. The log growth rate between times s and t is:

```
log_growth_rate = log (X_t / X_s) = log(X_t) - log(X_s)
```

This function takes as argument a NumPy column vector as a 2D array of size `(N, 1)` (comparable to a column vector). Assume that the input is a time series at the yearly frequency, i.e. each observation in the input data corresponds to a year in a continuous sequence. You should compute the log growth rate from one year to the next. You should then return the variance of this log growth rate.

You should use NumPy functions like `numpy.log()` and `numpy.var()`.

# Exercise 5: Integral calculation (13 points)

A Riemann integral is the successive approximation of the integral of a function, as in this image:

![](Riemann_integral_regular.png)

For clarity, I will refer to the function in your exercise as "your Python function", and to the function whose integral you'll compute as the "my analytic function". My analytic function will be an argument to your Python function (indeed, Python can store functions into variables and you can pass them around; it's a programming paradigm called "functions as first-class citizens"). For example, if `fn` is the argument to your Python function, you can get its value at 0 with `fn(0)`.

Your Python function computes one step iteration in this approximation of the integral of a function. Your function takes as arguments:

- my analytic function

- a start for the range (interval) where to compute the integral

- an end for the range (interval) where to compute the integral

- an integer for the number of segments

Your Python function should use the value of my analytic function at the midpoint; for example, if the start is 0, then end is 1, and the number of segments is 5, you should use the values of my analytic function at 0.1, 0.3, 0.5, 0.7, and 0.9.

Your function should have doc-tests. You can use the helper function `square()` that I defined in the file. You can check if a variable is a function with the function `callable()`, e.g. `callable(square)` returns `True`.

Your Python function should return the approximate value of the integral of my analytic function over the given range and with the given step.

# Exercise 6: reading and parsing a CSV file (20 points)

A CSV file (Comma-Separated Values) is a common format for data storage. It is similar to Excel's XLS, but it only stores data or values (no formulas). It has a delimiter, most commonly a comma, to separate columns; and the delimiter to separate rows is usually a newline (the value in Python is `"\n"`).

For example, a CSV file with income by county in the US would look like this:

```
county,state,income
Kings,NY,1234
Queens,NY,6789
```

Reading and understanding a file in this way is called "parsing."

You cannot use module functions like `pandas.readcsv()` nor `csv.reader()`.

## Imperative function

Complete the function `parse_csv_imperative()` in imperative style. It takes as input a string with a line in the CSV file, and returns a list with the value of each cell, for example on the first line it would return:

```
["county", "state", "income"]
```

## Recursive function

Sometimes, the value of a cell has the delimiter itself, for example "Washington, D.C." In this case, the CSV format stores it with quotes around the name, for example:

```
county,state,income
"Washington, D.C.",DC,1234
```

Complete the function `parse_csv_recursive()` to handle this case and remove the quotes. For the second line in the above example, it should return:

```
['Washington, D.C.', 'DC', '1234']
```

Also complete the function `parse_csv_recursive_wrapper()`. It should only check for edge cases, then it should call the recursive function (the "wrapper" function is called so because it wraps around the recursive function).

## Reading from a file

Complete the function `read_csv()` that takes as argument a filepath and returns a list of lists with the contents of the file.

You should check that the filepath exists with `import os` and `os.path.exists()`. If you don't know how to read files, check the Jupyter notebook called `Review` in lecture 6. The function should have no other doc-tests because we can't assume that a file exists on the computer running the system.

The function should call the recursive function. You should ignore empty lines.

# Exercise 7: logistic regression and k-Nearest Neighbors regression (20 points)

In this exercise you do not have to write doc-tests for the functions.

Here we run both logistic regression and 1-nearest neighbors regression and compare the two. We have data on previous applications and want to automate this process or assist a new loan officer in making decisions.

The dataset consists of loan applications. The outcome variable is 0-1, whether the loan officer granted the loan. The explanatory variables for logistic regression are the applicant's income and the loan amount. For simplicity, 1-nearest neighbor regression will only use the applicant's income, which is the first column of the 2D-array (because otherwise we'd have to define a relative weight to sum the distance between the two explanatory variables, which makes it more complicated).

The dataset comes from [this GitHub repository](https://github.com/SandeepHonnali/Loan-Approval-Prediction-using-Machine-Learning/blob/main/1Copy%20of%20loan.csv) and I downloaded it and cleaned it for you. I also split it between train and test data. I added code to get this data in the file; the test data is `y_test` for the outcome and `x_test` for the features; the training data is `y_train` for the outcome and `x_train` for the features (like in assignment 2).

When you complete these functions, read the doc-string to know how they work and what they should return. (The doc-string is a triple-quoted string on the line after a function.)

Complete the functions to perform logistic regression. You can use a package to perform this. Return the two regression coefficients (not the intercept).

Complete the function for 1-Nearest Neighbors (1-NN) prediction. For this function, **YOU CANNOT** use packages like SciKit-Learn or Stats: you must write it from scratch (you can use NumPy and look at the code from Assignment 2). Return the label for the predicted input `x` from training data `x_train` and `y_train`.

Also complete the functions to compute the accuracy of either regression on the **test dataset**. The accuracy should be a sum of binary numbers: 1 if the model's prediction coincides with the outcome, 0 if they do not, and then you divide this sum by the number of observations to get a percentage. Return the accuracy as a float.

For the accuracy of logistic regression, assume a threshold of 0.3: if the probability predicted by the model is greater than or equal to 30%, we approve the loan. This value is in the global variable `LOGISTIC_REGRESSION_THRESHOLD` at the top of the file. You should compute the predicted probability "by hand", from the formula of the sigmoid function and the linear model; you should **not** use a built-in function from a package to do this (because you are running the prediction on the test dataset, which is different from the data you used for prediction).

Submit your file `exercise7.py`. Do NOT submit `exercise7_data.py`.

# Exercise 8 (bonus): web scraping (10 points)

Here we scrape data from an article for sale on Amazon, such as these three pages:

https://www.amazon.com/Practical-Guide-Quantitative-Finance-Interviews/dp/1438236662

https://www.amazon.com/Mostly-Harmless-Econometrics-Empiricists-Companion/dp/0691120358

https://www.amazon.com/Tale-Two-Cities-Charles-Dickens/dp/145153194X

You should check that the argument to the function is a string and a URL similar to the ones above. You can use the string method `.startswith()`.

To help you got faster, I already wrote in a separate file a function that downloads the source of a web page (HTML), or gets it from a file if it's one of the three URLs above. If you have issues, for example if Amazon is limiting your requests, use only those three URLs

If you have difficulty, most HTML tags follow this syntax: `<tagName attributeName=attributeValue ...>some text</tagName>`, where `tagName` can be `a` (for a link or anchor tag), `div` and `span`; and the attribute name can be `id` (and then the value should be unique with a page) and `class` for a CSS class.

Your function should find the title of the product thanks to an ID attribute. An ID attribute follows this syntax `<tagName id=some_id ...` in the HTML and you get it in BeautifulSoup with `soup.select("tagName#id")`. You should also remove leading and trailing spaces from the title with the string method `.strip()`.

If you use Safari as a browser, you may need to enable Developer tools to see the page source of a web page (detailed steps [here](https://www.howtogeek.com/721416/how-to-turn-on-the-develop-menu-in-safari-on-mac/)).

Submit your file `exercise8.py` without changing the name. Do NOT submit `exercise8_data.py`.

# FAQ (not graded)

## What is a doc-test?

A doc-test is "executable documentation" and shows how the function works.

All doc-tests happen in the doc-string; a doc-string is a string after a function definition that starts and ends with triple quotes. Here is an example:

```
def some_function():
    """
    This is a doc-string.
    """"
    return 0
```

A doc-test is a line in the doc-string that starts with triple angled brackets, `>>>`, uses is a valid Python expression, and the next line shows the result expected by the test. For example, here is a function that computes the area and a doc-test that expects the function to return 6 when called with arguments 2 and 3.

```
def compute_area(height, width):
    """
    >>> compute_area(3, 2)
    6
    """"
    return height * width
```

You can add as many doc-tests as you want inside the doc-string.

```
def compute_area(height, width):
    """
    >>> compute_area(3, 2)
    6
    >>> compute_area(2, 5)
    10
    """"
    return height * width
```

## How to write a doc-test in defensive programming?

You should expect thing to go wrong and your function to be called with weird arguments. You can write a doc-test for these cases as follow:

```
def compute_area(height, width):
    """
    >>> compute_area(2, -1)
    Traceback (most recent call last):
    ...
    ValueError: arguments must be positive
    """
```

## How to write a doc-test with a string?

When using strings in doc-tests, please note that Python usually shows strings with single-quotes. So this doc-test will fail:

```
def return_hello_world():
    """
    >>> print_hello_world()
    "Hello world"
    """
    return "Hello world"
```

but if you change the result of the test to single quotes, it will succeed (even though the function uses double quotes):

```
def return_hello_world():
    """
    >>> print_hello_world()
    'Hello world'
    """
    return "Hello world"
```

