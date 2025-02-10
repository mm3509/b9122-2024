from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

import data_tools


def diarize_return(interest_rate):
    """
    No doc-tests needed.
    """

    return np.exp(np.log(1 + interest_rate) / 250) - 1


def get_efficient_portfolio(tickers, p_annual, risk_free_annual):
    """
    No doc-tests needed.
    """

    data = data_tools.get_returns(tickers)  # noqa: F841

    # TODO: complete this function.

    return


if "__main__" == __name__:
    tickers = ["NVDA", "GOOG", "BRK-B", "AAPL", "TSLA"]
    print(get_efficient_portfolio(tickers, 0.3, 0.05))
