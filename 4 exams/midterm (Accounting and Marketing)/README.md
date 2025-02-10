---
title: 'Midterm exam (take-home, afternoon section)'
author: 'Miguel Morin, (c) 2024'
geometry: margin=2cm
numbersections: false
header-includes:
- \pagenumbering{gobble}
- \setlength{\parskip}{\baselineskip}
- \usepackage{hyperref}
- \usepackage{xcolor}
- \newcommand{\link}[1]{{\color{blue}\underline{\href{#1}{#1}}}}
---

# Midterm exam (take-home, afternoon section)

Bonus questions are optional, but will increase your grade up to a maximum of 100 points. They serve as insurance **within** the exam and compensate when you get less than full marks on another question. They DO NOT serve as insurance **across** exams and DO NOT compensate when you get less than full marks on another exam.

You should download this repository. If you use `git pull`, you should NOT edit the files here, as I may push updates that will cause you to lose your work.

Please note that I flipped the format of the exam: instead of part 1 being about 5 hours and part 2 being around 15 hours, part 1 should now take 2-3 times as long as part 2 and the balance of points reflects that change. I made this decision because:

- I want to make sure that you master a lot of basic Python material, so I had a lot of questions in Part 1

- you raised a valid concern of how part 2 would be graded: it is now graded just like any of the other exercises you've had.

## Part 1: 70 points

This part covers your basic practice with Python and should give you a lot of practice.

For all these questions:
1. complete the Python function in the relevant file and submit it on Gradescope without changing file or function name;
2. do not use any modules or libraries, please write the functions from scratch (exceptions are `doctest`, `sys` and `os`, which you are allowed to import);
3. the exception to the above banning of modules is other files you wrote in this assignment: you should be importing to be DRY;
4. all your functions should have doc-tests and apply defensive programming.

Please note that, to avoid repetition and be DRY, the files do not contain the usual boilerplate to run doc-tests. Instead, you can run your doc-tests with this command in a shell, passing the filename as an argument

```
cd <path-to-the-folder-with-files>
python -m doctest exercise11.py
```

If you see no error and nothing prints, then your doc-tests pass.

You can also run the doctests in all files with:

```
python -m doctest *.py
```

Doc-tests do not have to be DRY, i.e. you can copy-paste doc-tests
from one file to another. Doc-tests belong to a specific function and
you should not try to refactor them to be DRY.

Similarly, the code handling edge cases does not have to be DRY,
i.e. you can copy-paste the code handling edge cases from previous
questions (and the overall code is less DRY), or you can refactor the
code handling edge cases into another file that you import and use its
function (the code is slightly less readable). You will not lose
points if you do either of these; this edge case is a constraint of
the format of an exam.

Each exercise is worth 3 points, except the last exercise (21), which is worth 10 points.

### Exercise 1: List manipulation

This function takes a list of integers as input and returns a new list containing only the numbers that are even. To check if a number is even, use the modulo operator, `%`, which gives the remainder of an integer division, i.e. `5 % 2` gives 1.

Do not use any built-in functions like `filter()` or list comprehensions.

### Exercise 2: Booleans and conditionals

This function determines whether a year is a leap year, i.e. if it fulfills both of these conditions:

- it is divisible by 4,
- it is not divisible by 100 (unless it is also divisible by 400)

### Exercise 3: List manipulation

This function rotates a list to the right by a given number of steps. It should return a new list. It should also wrap around the initial list.

You can use "slicing" (define a list `a` and check what `a[:2]` and `a[2:]` do), and built-in operators.

### Exercise 4: List slicing

This function takes a list and a positive integer `n` and returns every `n`-th element from the list, starting from 0. For example, if `n` is 2, you should return elements at every even position, starting from 0. You can use slicing notation, i.e. if `a = list(range(10))`, then check what is `a[::3]`.

### Exercise 5: Dictionary manipulation

This function takes a string and counts the frequency of each character. It should return a dictionary with each character as the key and its frequency as the value.

A character is anything represented in a string: space, punctuation, numbers (in string format). An uppercase letter and the same letter in lowercase are different characters.

Do not use any built-in functions like `collections.Counter` .

### Exercise 6: Tuple manipulation

This function takes a tuple of integers and returns a new tuple containing only the unique integers from the original tuple, in the order they first appeared.

For speed, you can use the built-in function `set()`, which checks if an element is in a set. Run `pydoc set` from a shell or `help(set)` from a Python interpreter to read the documentation.

### Exercise 7: For loop

This function takes a list of integers and returns the sum of all the even integers in the list.

### Exercise 8: While loop

This function takes a positive integer and returns the sum of all integers from 1 to that number (inclusive) using a `while` loop.

### Exercise 9: String manipulation

This function takes a string as input and returns a new string with all vowels removed, all other letters in lower case, and all other elements unchanged.

In English, the letter "y" is sometimes a vowel (as in "by") and sometimes a consonant (as in "yard"). For this exercise, it's considered a vowel.

### Exercise 10: User input

This function repeatedly asks the user for a positive number (using built-in function `input()`; to learn about it, run `pydoc input` from a shell or `help(input)` from a Python interpreter) until the user enters something that is not a positive number (a zero, a negative number, nothing at all, or not a number). The function should then return the total sum of all the positive numbers entered.

### Exercise 11: Empty string

Write a Python function that checks if a given string is a palindrome. A palindrome is a string that reads the same forwards and backwards. Case should not matter, i.e. `"Abba"` is a palindrome. The function should also handle the case of an empty string, i.e. `""` which is a string of length 0, and should also be considered a palindrome.

You can assume that the string has no spaces and Autograder will not pass a string with a space.

### Exercise 12: In-place

This function removes all occurrences at even indices from a list. The function should work **"in-place"** and modify the original list.

Hint: if you are sure your function has the right logic but Gradescope gives you errors, read about "local scoping".

### Exercise 13: Module imports

This function takes a list of years and returns another list of years containing all the years in the original list that are not leap years.

This function should not modify the original list.

**DO NOT** copy-paste code from the question above. Instead, write an `import ` to use the function you defined above.

### Exercise 14: View vs. copy

This function does the same thing as the previous one, EXCEPT that it modifies the original list and does not return anything; i.e., it uses **a view and not a copy** of the original list, and operates **"in-place"**.

This question is trickier: if you iterate on the index of a list, find that index 0 has a leap year, and remove it, then the year at index 0 has now changed. There are a few ways to do this and you can choose any of them.

### Exercise 15: Copy / return (not "in-place")

These two functions do the same thing and reverse a list. One works in-place and is tricky to program. The other function does not work in-place and returns a new list.

This exercise is meant to teach that, in this case, "in-place" seems clunky and returning a new list is much easier.

### Exercise 16: List sorting

This function takes two lists of integers, and returns a sorted list with the same elements as the two lists. The initial lists should stay unchanged, i.e. your function should not operate in-place.

You should use built-in functions or methods for sorting and concatenation.

### Exercise 17: recursion

The first function calculates the sum of all elements in a list of integers using recursion. Do not use imperative style: your function has to call itself. It should not have doc-tests.

The second function is a "wrapper" around this first function. It should have doc-tests, handle edges cases, and then call the first function. (The second function is called a "wrapper" function because it "wraps" around the first function.)

### Exercise 18: List comprehensions

This function takes a list of integers and returns a new list containing the squares of all the even integers from the original list. It should be one line and use list comprehension.

### Exercise 19: file reading and writing

This function takes two filepaths: one to read from and one to write to. Each line of the output file consists of a line from the input file with the vowels removed and all consonants in lower case.

Because this function handles files from the system (called "input-output" or I/O), it should not have doc-tests. It's difficult to ensure that all systems have the same files to make the doc-tests pass, so we skip them entirely (for now; later if we see "unit tests", we can add tests to functions like this).

You should check that the input file exists and that the output file does not exist, and raise a `ValueError` otherwise. To check the existence of a filepath, use this code:

```python
import os

os.path.exists("/path/to/file")
```

### Exercise 20: debugging

This function removes all occurrences of an item from a list. It has a bug because it does not perform as we expected, and does not pass the doc-tests. Find the bug and fix it.

### Exercise 21: more string manipulation, imports, system arguments, and dunder variables (10 points)

This function that checks whether two strings are anagrams. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. Case does not count (i.e., uppercase "A" is the same as lowercase "a") and spaces do not count: for example, "The Morse Code" is an anagram of "Here come dots".

If this file is called directly, it should get the two arguments passed by the shell `sys.argv[1]` and `sys.argv[2]`
(the first argument, `sys.argv[0]`, is the path to the Python file),
and print a Boolean for whether they are anagrams.

That is, if you run this in a shell:

```
python exercise21.py "The Morse Code" "Here come dots"
```

it should print

```
True
```

But, if you import this file somewhere else, it should not do anything. In particular, it should not throw an error.

Also, your code must handle the corner case where not exactly two arguments are passed to the function. Check this with `python exercise21.py 1` and `python exercise21.py 1 2 3`.

## Part 2: 30 points

### Exercise 1: 25 points

In this part, we are interested in the correlation between the Federal Funds Rate, controlled by the Federal Reserve Board, and the stock market from 1954 to today. I wrote a Python file `get_data.py` to download the data and save it as a NumPy matrix. The first column is the index of the S&P 500, one of the main indices for the US Stock Market. The second column is the Federal Funds Rate. (Note: You don't have to do this step again, i.e. don't donwload data for this exerise, just use `data.csv`.)

Now you have to do the rest.

In particular, you should prepare the data in the function `prepare_data()` with these steps:

- compute the growth in the stock market with the change in the logarithm of the index (use function `np.log()` and slicing notation)

- compute the percentage point change in the federal funds rate (not in growth rates, and use slicing notation)

You then have to complete the functions that compute a linear regression in three different ways. The regression model is the same for all three ways: a linear regression (Ordinary Least Squares) of the stock market on the federal funds rate. The three different ways are:

- via matrix manipulation in NumPy and the formula for beta (i.e., (X'X)^-1 * X'Y) as we saw in class;

- via the Python package Sci-Kit Learn and its sub-module `sklearn.linear_model`, which runs the same linear regression (you can import it; the restriction on modules only applied to part 1);

- via a calculation of variance and covariance in NumPy (see the FAQ at the end of this document about it).

Each function should return a value for the regression coefficient only (i.e., not the constant, only the slope), and save a plot of the regression to a filepath passed as an argument.

You should also complete the function `check_results()` that checks that the three methods give similar results, up to numerical error.

The `main()` function runs all these functions and saves the results. You don't have to change it.

Complete the Python file `regression.py` and submit it on Gradescope. Also submit the images of your plots without changing the name.

### Exercise 2: 5 points

Inspect the plots of the regression and answer these questions:

1. Why do the plots look the way they do?
2. What is the main disadvantage of the linear model with "Ordinary Least Squares" (which is the linear regression we used) in this case? (I am looking for one particularly obvious disadvantage; if you find several disadvantages and none stands out, please list them all.)
3. How can you fix this disadvantage?

Write your answer into a text file called `part2_exercise2.txt` and submit it.

### Exercise 3: bonus (5 points)

In this optional exercise, you'll run the same linear regression using other variables.

As dependent variable, run the file `get_ticker.py` and enter your UNI: it will give you three letters and you have to find a stock market ticker that has these three letters. (If, for your thesis, you really want to have another outcome variable, please come see me in Office Hours.) Find the code for this ticker in Yahoo Finance.

As explanatory variable, peruse the gallery of economic variables from the [Federal Reserve Economic Database (FRED)](https://fred.stlouisfed.org) and find another explanatory variable, different from the Federal Funds Rate, that seems interesting to you. Get the code for this variable in the URL of the series or in the parenthesis next to the name on the webpage (for example, the [Federal Funds target rate](https://fred.stlouisfed.org/series/DFF) has code `DFF`).

Edit the file `get_data.py` to download data with these two codes, one from Yahoo Finance and another from FRED. You will also need to [create a free account on FRED](https://fredaccount.stlouisfed.org/login/secure/) and [get an API key](https://fredaccount.stlouisfed.org/apikey). Save the value of that API key to a file, and add code in `get_data.py` to read that API key, then pass that value when initializing the FRED downloader. That is, instead of `fred = fredapi.Fred()` on line 25, you should have `fred = fredapi.Fred(your_api_key)`; you should pass this as a variable, you should NEVER write API keys or other credentials in the source code (this would be called "embedded credentials" and many data breaches come from this poor practice).

You can modify the variables `START_DATE` and `TODAY` to fit your
case. Do not submit the file with the text data, nor the API key: I
will use my own API key to get the data. You may need to drop missing values (`NaN` from the data; if you have issues with multi-level merging in pandas, please come see us during Office hours).

This file then saves the data in NumPy and you can run the code above again. You're allowed to edit the levels of precision in the call to `check_results()` to fit your case.

Save one of the coefficients to a text file. Gradescope will use this value to compare the results of your code, with a tolerance of `1e-5` (i.e., I use the default value of `1e-5` relative tolerance in the function `numpy.isclose()` to compare the values). All three methods give the same answer, so it does not matter which you use. Do not save anything other than this number, otherwise Gradescope cannot read it and compare to your code.

Submit these files:
- `get_data.py`, edited with your data series codes;
- `part2_exercise3.txt`, with the resulting coefficient from your linear regression;
- `part2_exercise3.png`, with one of the images from your linear regression.

Do NOT submit `regression.py` for this exercise. Instead, I will use your submitted file from exercise 1 to confirm the coefficient.

## FAQ

### How do I compute the regression coefficient variance and covariance?

Our case is a "univariate linear regression": one explained variable (stock market) and one explanatory variable (Federal Funds Rate). This case is called "Simple linear regression", or "univariate linear regression" ("univariate" for only one variable) and you can read more about it [here](https://en.wikipedia.org/wiki/Simple_linear_regression).

In this case, the regression coefficient equals the covariance between `x` and `y` divided by the variance of `x`. 

You should implement this calculation in NumPy using functions `numpy.mean`, `numpy.var` and `np.cov`. When you read the help on these functions, an "axis" is a dimension. For example, if you have a 2-D array of size (2, 3) and you want the mean, you have to specify if you want to average along the vertical dimension (axis 0) and get 2 numbers, or along the horizontal dimension (axis 1) and get 3 numbers.

The result from this calculation should be similar to the other two, up to 14 digits of precision.

If you get different results from the other two methods: When you use `np.cov()`, by default NumPy divides by `N-1` instead of `N` to provide an unbiased estimate, and then when you divide by the variance (which divides by `N` instead of `N-1`) and the result is different. You should pass the keyword argument `bias=True` to avoid this issue.

### How do I compute the constant from a linear regression?

Once you have the coefficient of the linear regression, the constant is the average of the difference between the output values and the coefficient times the input value.

For automated assessment, please compute this constant within the plotting function.

### What is a doc-test?

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

### How to write a doc-test in defensive programming?

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

### How to write a doc-test with a string?

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

### What are the deliverables for part 2?

Submit the following files:

- exercise 1: `regression.py`, `plot1.png`, `plot2.png`, and `plot3.png`.

- exercise 2: `part2_exercise2.txt` answering the three questions

- exercise 3: `get_data.py` customized to your case, `part2_exercise3.txt` with the regression coefficient, and `part2_exercise3.png` with the plot.

### I get the error `SyntaxError: f-string: unmatched '('`

This is a problem caused by an update to Yahoo Finance on October 20th, 2024. Please use the previous version, `0.2.44` instead. I updated the file `requirements.txt` to install this version, and if you installed a previous version, please run this in a shell:

``` bash
pip uninstall -y yfinance
pip install yfinance==0.2.44
```

