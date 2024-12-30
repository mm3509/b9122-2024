# Assignment 5

In this assignment, you need to implement good style and defensive programming only in the Python questions. For SQL and C, you don't need to worry about following a style guide or defensive programming; but your code should still be readable like a Python code (for example: if you write your C code all in one line, the TA will have a hard time reading it and you will lose points).

Some exercises are common to both sections, so we have one Autograder for both sections (which will also help with code comparison across sections). To run the right autograder, you should upload an empty file, either `morning.txt` or `afternoon.txt`. If not, the Autograder will assume you are in the morning section.

__Note__: If you have never heard about the time-complexity of algorithms, or if you are no longer preparing for interviews, you can ignore this paragraph. Exercises 4 and 5 have solutions with different levels of efficiency: a trivial solution in `O(n^2)` and a non-trivial (or sneaky) solution in `O(n)`. Both solutions are valid and will earn you full marks. You can try to optimize the efficiency of the algorithm, similar to what you did with prime numbers and the Sieve of Erathostenes. If you submit the fast algorithm, you will get __5 bonus points__ for each question during manual grading (10 in total, up to the maximum of 140 points). This may be especially relevant if you want a career in quantitative finance, data science and software engineering: interviewers typically expect you to improve the efficiency of your code with this kind of optimization. In addition, both fast solutions use ideas that are often useful and are not one-off tricks. Therefore, the fast algorithms will be useful for you to know and practice. Nevertheless, do not try to optimize the algorithm speed in exercise 6: C is already complicated enough at this stage.

# Exercise 1: SQL (20 points)

Import the world database in `world.sql` in this repository. Write an SQL query, starting with `SELECT` and using a `JOIN`, that lists all countries that do not have any cities.

Notes:
- This exercise assumes you are using SQLFiddle.com. If you use another SQL online compiler or a local installation, follow [these steps](https://dev.mysql.com/doc/world-setup/en/world-setup-installation.html).
- On SQLFiddle.com, you'll need to create the whole database each time you write a query. But Autograder already has the database, so you should submit only your query, starting with `SELECT`.
- Autograder uses MySQL, so make sure to use MySQL also (not PostgreSQL, or any other implementation).
- The Autograder MySQL database is case-sensitive while SQLFiddle.com is case-insensitive. So you'll need to use `country` and not `Country`, for example.

If needed, Use `DESCRIBE` to get information on the tables.

Example output:

```
Antarctica
French Southern territories
Bouvet Island
Heard Island and McDonald Islands
British Indian Ocean Territory
South Georgia and the South Sandwich Islands
United States Minor Outlying Islands
```

# Exercise 2: web crawling and scraping (40 points)

In this exercise, we will crawl the newsroom on the Apple website and get all press releases, for example for quarterly returns.

The template file `exercise2.py` is similar the web crawler from lecture. One difference is the addition of a function to check if a URL is a press release (and, for simplicity, we download the webpage again, so the doc-tests are self-contained and you can get the right results).

Read and understand the file, then complete the sections marked as `# TODO` in the following functions:

- `is_url_valid()`: if a URL is a string starting with `"http"`, it is valid. You should also call this function from another point in the file.
- `clean_url()`: make it pass the third doc-test (when a URL ends with a slash).
- `should_visit_url()`: exclude from crawling the webpages ending in `.pdf`, `.mp4`, and `.zip`.
- `is_press_release()`: detect if a URL is a press release.
- `crawl()`: collect the URLs that are press releases, and return them at the end.

Notes:
- Autograder will call the `crawl()` function, so you can also modify the `main()` to suit your needs when developing.
- Autograder takes a few minutes to run your crawling code, so you may want to submit this file independently of the other exercises, and then again only in your last submission.
- If you get an error `Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.`, print the URL that threw this error, and consider whether your crawler should be visiting this URL.
- The order of the press release URLs does not matter; Autograder will sort them before comparing.

Example output (9 URLs):

```
['https://www.apple.com/newsroom/2024/10/new-macbook-pro-features-m4-family-of-chips-and-apple-intelligence', 'https://www.apple.com/newsroom/2024/10/apple-introduces-powerful-new-ipad-mini-built-for-apple-intelligence', 'https://www.apple.com/newsroom/2024/10/apples-new-mac-mini-is-more-mighty-more-mini-and-built-for-apple-intelligence', 'https://www.apple.com/newsroom/2021/04/apple-and-partners-launch-first-ever-200-million-restore-fund', 'https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac', 'https://www.apple.com/newsroom/2024/10/apple-reports-fourth-quarter-results', 'https://www.apple.com/newsroom/2024/09/apple-introduces-groundbreaking-health-features', 'https://www.apple.com/newsroom/2024/10/apple-introduces-new-imac-supercharged-by-m4-and-apple-intelligence', 'https://www.apple.com/newsroom/2024/10/apple-introduces-m4-pro-and-m4-max']
```

# Exercise 3: neural network (15 points)

This file has a function `load_data()` that takes a filepath, `loans.csv` (with data on loan applications and whether they were granted or not), loads it, and processes it in Pandas.

You have to create and train a simple Perceptron neural network model to predict the outcome of the loan application.

Complete the function `fit_data()`. Complete the function `compute_accuracy()` to gauge the accuracy of your neural network on the test data.

You do not need to add doc-tests to the functions. If you get different results, make sure not to use the argument `random_state` in the Perceptron.

Example output:

```
0.7291666666666666
```

# Exercise 4: Python (20 points)

This function takes a list of prices of a given stock: `prices[i]` is the price of the stock on day `i`. The function maximizes profit by choosing a single day to buy a stock and a different day to sell it. The function returns the maximum profit you can achieve from this strategy, or 0 if you cannot make a profit.

For example inputs and outputs, please see the doc-tests. You need to apply defensive programming and have at least 5 doc-tests in total.

# Exercise 5: Python (20 points)

This function takes a list of numbers, which are returns of a stock, and finds the contiguous sub-list with the largest cumulative return (a simple sum, without compounding). The function returns a tuple with the start index, the end index, and the cumulative return.

Many trading systems, e.g. at hedge funds or trading desks, need such an algorithm to benchmark the performance of real or simulated trading strategies. Therefore, this is a favorite question of interviewers.

For example inputs and outputs (including if you cannot make a profit), please see the doc-tests. You need to apply defensive programming and have at least 6 doc-tests in total.

__Note__: this is Kadane's algorithm, or the ["Maximum subarray problem"](https://en.wikipedia.org/wiki/Kadane%27s_Algorithm).

# Exercise 6: C (25 points)

This exercise is an example of "dynamic programming", where recursion is a natural solution. In this example, you do not need to worry about time efficiency, accumulators, or memoization; the benchmark on Autograder is from a trivial algorithm without any speed optimization.

Imagine you are at the bottom of a staircase with `n` steps. You can go up one step at a time, two steps at a time, or three steps at a time. Complete the function that counts the number of different ways to go up the stairs. You should count steps in one direction only, and reach exactly at the top of the stairs (i.e., you should not "overshoot": going up `n` times three steps each does not add up to `n`, this is not a valid way to go up the stairs, and should not count towards the total number).

Example output:

```
Number of ways to go up 1 steps: 1
Number of ways to go up 2 steps: 2
Number of ways to go up 3 steps: 4
Number of ways to go up 4 steps: 7
Number of ways to go up 5 steps: 13
Number of ways to go up 6 steps: 24
Number of ways to go up 7 steps: 44
Number of ways to go up 8 steps: 81
```
