from sklearn.linear_model import LinearRegression

import pandas as pd

import data_tools
import exercise1


def get_capm_data(tickers):
    """
    No doc-tests needed.
    """
    rates = data_tools.get_risk_free_and_market_rates()

    stock_data = exercise1.download_and_merge(tickers)

    # TODO: complete this function.

    return


def run_capm_regression(tickers):
    """
    No doc-tests needed.
    """
    data = get_capm_data(tickers)

    # TODO: complete this function

    return


if "__main__" == __name__:
    print(run_capm_regression(["NVDA", "GOOG", "BRK-B"]))
