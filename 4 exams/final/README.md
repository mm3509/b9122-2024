# Final exam

These exercises are grouped by language: SQL, Python, C, and bash. In the Python group, they are ordered roughly by increasing difficulty. I strongly suggest you read all the questions first to make a plan on how you can tackle them most efficiently.

You need to apply defensive programming only in questions 2, 3, and 7, i.e. only in Python and only in questions without data analysis (the template files have doc-tests, and this document mentions that example input and output are in the doc-tests). Each question has the exact number of doc-tests you must add, and Autograder will tell you as well.

## Exercise 1: SQL (10 points)

This question is similar to the SQL queston in assignment 5.

Import the world database in `world.sql` in this repository. Write an SQL query, starting with `SELECT` and using a `JOIN`, that lists all cities with over half a million in population and in countries that contain `land` in their name (e.g., Finland, Switzerland, Swaziland, etc; you can use lower-case, because there are no countries with a variation of `land` in upper case). If needed, use `DESCRIBE` to get information on the tables.

Notes:
- This exercise assumes you are using SQLFiddle.com. If you use another SQL online compiler or a local installation, follow [these steps](https://dev.mysql.com/doc/world-setup/en/world-setup-installation.html).
- On SQLFiddle.com, you'll need to create the whole database each time you write a query. But Autograder already has the database, so you should submit only your query, starting with `SELECT`.
- Autograder uses MySQL, so make sure to use MySQL also (not PostgreSQL, or any other implementation).
- The Autograder MySQL database is case-sensitive while SQLFiddle.com is case-insensitive. So you'll need to use `country` and not `Country`, for example.

Example output:

```
city_name	country_name
Amsterdam	Netherlands
Rotterdam	Netherlands
Warszawa	Poland
Lódz	Poland
Kraków	Poland
Wroclaw	Poland
Poznan	Poland
Helsinki [Helsingfors]	Finland
Bangkok	Thailand
```

## Exercise 2: Python and strings (10 points)

Complete the function to check if a string has only unique characters, ignoring case. You can use primitive types like `set()` and `list()`, but you should not call outside functions like `numpy.unique()` or `sorted()`.

See the doc-tests for sample input and output. You must use defensive programming and add one more doc-test for it.

## Exercise 3: Python and tuples (15 points)

This function takes a list of intervals (each represented as a tuple of two integers) and merges all overlapping intervals. It returns a new list of merged intervals. To help you, I added a line of code that sorts the list of tuples by the first element, then the second element (called "lexicographic order").

For sample inputs and outputs, please consult the doc-tests. You must use defensive programming and add four more doc-tests for them.

## Exercise 4: logistic regression (plain English, graded manually, 15 points)

Please write your answer in plain English, save it as a `.txt` file, and submit it.

In binary classification, what is the main advantage of using cross-entropy loss (i.e., negative log-likelihood) instead of squared loss? That is, what is the main advantage of using logistic regression instead of ordinary least squares?

## Exercise 5: Python and regression (20 points)

This dataset contains data on fundamentals of companies in the S&P 500.

Complete the function to predict the logarithm of the stock price, using as dependent variables:

- the dividend yield
- the earnings/share ratio
- the logarithm of the market capitalization
- the logarithm of (1 + EBITDA)
- the logarithm of assets
- the logarithm of revenue

Because this is linear regression, you do not need to scale the features.

The function returns a dictionary with the coefficients for each of these variables.

Example output:

```
{'Dividend Yield': -0.02492165443761143, 'Earnings/Share': 0.023650171485154737, 'Market Cap': 0.0023854960242144963, 'EBITDA': 0.001310565350556841, 'Assets': 0.0020790127484804685, 'Revenue': 0.0027036808972507663}
```

## Exercise 6: Python and classification (25 points)

We'll use the same data, and predict the economic sector of a company. For example, many information technology companies, like Google, do not pay dividends; we can infer that a company is in the tech sector if the dividend yield is zero. You should use the converted variables from the previous exercise, i.e. use the log-price and not the price. Don't optimize the hyper-parameters; just use the specifications below.

We have seen three classifiers: k-nearest neighbors, logistic regression, and neural networks. Complete the parts in the file:

- preprocess the data to scale it like we saw in class;
- fit a model for each classifier on the training data to predict the sector of a company:
  * for k-nearest neighbors, use `k=3`;
  * for the multi-layer perceptron, use 3 hidden layers with sizes 128, 64 and 32, the default relu function as activation or the logistic function as activation, a maximum of 10,000 iterations, and random state 42 (for reproducible results)
- compute the accuracy of the model on test data.

Example output from running the code in `__main__`:

```
Accuracy of logistic model: 0.30
Accuracy of knn model: 0.31
Accuracy of mlp model: 0.38
```

## Exercise 7: Python and algorithms (MSFE and Engineering only, 25 points)

Complete the function to return the length of the longest substring without repeating characters (ignoring case). You do not have to optimize the function for speed or complexity, as long as you stay under quadratic speed (exponential speed will not do). You can use keywords `break` to exit a loop or `continue` to skip the rest of the code in the loop.

See the doc-tests for sample input and output. You must use defensive programming and add one more doc-test for it.

## Exercise 8: C (MSFE and engineering only, 10 points)

This file approximates the value of `pi` via Monte Carlo simulation of the area of the unit circle (with radius 1). It draws `n` random pairs of numbers `x` and `y` between 0 and 1. If the numbers are inside the "unit circle", they will count towards the calculation of the area of the unit circle and of `pi`. An approximation for `pi`, using the area of the unit circle as `pi / 4`, is then:

```
pi ~ 4 * # {x, y in unit circle} / n
```

Complete the function, which takes a number `n` of pairs of numbers to draw, and returns an approximation of `pi`.

Example output:

```
Approximation at 10^1: 3.200000
Approximation at 10^2: 3.120000
Approximation at 10^3: 3.132000
Approximation at 10^4: 3.171200
Approximation at 10^5: 3.141520
Approximation at 10^6: 3.141664
Approximation at 10^7: 3.141130
```

## Exercise 9: bash (MSFE and engineering only, 10 points)

Complete the bash script that grabs the first argument from the command-line, and prints the number of text files in the folder (you can use `ls /path/to/folder/*.txt` to list all files ending in `.txt`). If the argument does not exist, or is not a folder, it should print -1. You can assume that the user will always pass one argument (no need for defensive programming).

Below is example input and output. `$` stands for shell prompt; lines starting with `$` are commands run on the shell; the rest are results from the shell). Your results will vary depending on your machine.

```
$ bash exercise_bash.sh $HOME/Downloads
49
$ bash exercise_bash.sh $HOME/Downloads-missing
-1
```

## Exercise for marketing students only (45 points)

Please remember to submit a file with name `marketing.txt` for Autograder to consider the right exercises and assign the correct points.

Read the [paper by Rubin and Waterman (2016)](https://www-jstor-org.ezproxy.cul.columbia.edu/stable/27645750?seq=12) on using logistic regression and propensity score matching. Make sure you understand the details of the procedure.

The dataset is a small an simulated version of the data used in that paper. The categorical variables like the doctors' geographical region and specialty are already in 0/1 format, using one-hot encoding.

The file `exercise_marketing.py` is for you to complete. It has a function `naive()` that estimates the effect of a visit naively, by comparing the doctors who received a visit with those who did not. As the paper explains, this suffers from selection bias and is akin to "polishing the Ferraris" and is indeed an over-estimate.

You need to complete the file to perform the following tasks:

- In the function `propensity()`, perform a logistic regression using all the features in the global variable `FEATURES` to predict the visit to a doctor. Use the method `.predict_proba()` to get the estimated probabilities of a visit (in the global variable `VISIT`) and add it to a column (with the global variable `PROPENSITY`).

- In the function `estimate_causal()`, call the function `find_non_visited_clone()` to get a clone of each visited doctor (but drop those with propensity below 0.1 or above 0.9), then estimate the causal effect of a visit on the inscrease in the number of prescriptions at time 2.

Example output from running the file:

```
Naive estimation: 4.74
Causal estimation: 4.487603305785124
```

## Exercise for accounting students only (45 points)

Please remember to submit a file with name `afternoon.txt` for Autograder to consider the right exercises and assign the correct points.

Portfolio optimization is an important topic for investment management firms, who want to optimize their portfolio and maximize their returns. The mean-variance portfolio theory from Harry Markowitz is the most well-known and well-studied portfolio optimization problem.

This Python file computes the optimal mean-variance portfolio from stock returns, a target yearly return, and a risk-free yearly interest rate. It uses the solution to assignment 4, which downloads stock price data from Yahoo finance and computes the daily stock returns. You should use the function `diarize_return()` to convert a return from yearly to daily.

Follow the math in section 1.2 of [this summary](https://www.columbia.edu/~mh2078/FoundationsFE/MeanVariance-CAPM.pdf) and return the weights of the optimal portfolio.

Example output for a target return of 30% per year and a risk-free rate of 5% per year:

```
# The input is:
# print(get_efficient_portfolio(["NVDA", "GOOG", "BRK-B", "AAPL", "TSLA"], 0.3, 0.05))
[ 0.27730712  0.00338955 -0.06631429  0.13449474  0.12137712]
```
