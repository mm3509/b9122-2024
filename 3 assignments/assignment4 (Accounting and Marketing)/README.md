---
title: 'Assignment 4 - B9122, PhD Computing for Business Research'
subtitle: 'Miguel Morin, (c) 2024'
geometry: margin=2cm
numbersections: true
colorlinks: true
header-includes:
- \pagenumbering{gobble}
- \setlength{\parskip}{\baselineskip}
- \usepackage{hyperref}
- \usepackage{xcolor}
- \newcommand{\link}[1]{{\color{blue}\underline{\href{#1}{#1}}}}
---

**Preliminaries**

This assignment downloads historical stock price data and risk-free interest rates. To help you, I already wrote the basic functions that do it in the file `data_tools.py`. You need to:

- read that file to become familiar with the two functions;

- download the data `rates.ft` (in Pandas "feather" format) from this repository, which contains a column for the risk-free rate and a column for the market rate, and save it in the same directory as the file for exercise 2;

- install `yfinance`, version 0.2.44 (in the shell, either with `pip install yfinance==0.2.44` or `pip install -r requirements.txt`). If you get a MultiLevel index error like `Cannot join tz-naive with tz-aware DatetimeIndex`, uninstall your version (`pip uninstall yfinance`) and then install this version.

- import this file in exercises 1 and 2.

# Exercise 1: pandas (70 points)

The function in this file takes multiple tickers, calls the function from `data_tools.py` to download data for each of them, and merges all tickers into a pandas dataframe such that there are no missing data (e.g., discarding observations before a company went public). The function returns the merged dataframe.

You DO NOT need to write doc-tests or apply defensive programming.

Example input inside Python:

``` python
download_and_merge(["AAPL", "GOOG", "MSFT"])
```

Example output:

```
                  AAPL        GOOG        MSFT
Date                                          
2004-08-19    0.548393    2.499133   27.120001
2004-08-20    0.550000    2.697639   27.200001
2004-08-23    0.555000    2.724787   27.240000
2004-08-24    0.570536    2.611960   27.240000
2004-08-25    0.590179    2.640104   27.549999
...                ...         ...         ...
2024-10-28  233.399994  168.339996  426.589996
2024-10-29  233.669998  171.139999  431.950012
2024-10-30  230.100006  176.139999  432.529999
2024-10-31  225.910004  172.690002  406.350006
2024-11-01  222.910004  172.649994  410.369995
```

# Exercise 2: CAPM and regression (70 points)

This file has two functions. The first function takes a list of ticker codes for stock prices, downloads their data using the function from exercise 1 and from `data_tools.py`, and computes the percentage growth (not log-growth) in the stock price.

The second function runs a regression of the CAPM, Capital Asset Pricing Model, one for each stock return, and returns a tuple of dictionaries with the alphas and the betas of each stock.

The CAPM is written as a linear regression of the stock's excess return (the difference between the stock's return between `t-1` and `t` and the risk-free rate at time `t`) on the market's excess return (the difference between the market return and the risk-free rate at time `t`):

```
return_i_t - riskfree_t = alpha_i + beta_i * (market_t - riskfree_t) + error
```

The file `rates.ft` contains a column for the risk-free rate and a column for the market rate. I already converted the Fed's annual interest rate to a daily interest rate; you should do all calculations in daily growth rates.

Example input inside Python:

``` python
run_capm_regression(["NVDA", "GOOG", "BRK-B"])
```

Example output (alphas first, then betas):

```
(
  {'NVDA': 0.0013109622087666872, 'GOOG': 0.0006142673872072932, 'BRK-B': 0.000176164740692681},
  {'NVDA': 1.549295222737986, 'GOOG': 1.016520036209327, 'BRK-B': 0.7556350654778884}
)
```

# Exercise 3: Python (bonus, 15 points)

This bonus question is optional and will increase your final grade up to a maximum of 140 points.

This Python function determines wether a string `s` has valid bracket delimiters, square and curly brackets: `[`, `]`, `{`, and `}`. The string is valid if all the following conditions apply:

- it only contains those brackets;

- the opening bracket must be closed by a closing bracket of the same type;

- opening brackets must be closed in the correct order;

- every right bracket has a corresponding left bracket of the same type.

You need to apply defensive programming.

For examples of inputs and outputs, please see the doc-tests of the function.
