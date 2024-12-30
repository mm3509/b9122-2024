from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

import data_tools


def diarize_return(interest_rate):

    return np.exp(np.log(1 + interest_rate) / 250) - 1


def get_efficient_portfolio(tickers, p, risk_free):
    """
    No doc-tests needed.
    """

    # TODO: complete and use data_tools.RISK_FREE as the name of the
    # column in the dataframe with the risk-free rate.

    data = data_tools.get_returns(tickers)

    p_daily = diarize_return(p)
    risk_free_daily = diarize_return(risk_free)

    #p_daily = p
    #risk_free_daily = risk_free

    returns = data.values

    p_excess = p_daily - risk_free_daily
    mu = np.mean(returns, 0)
    
    mu_excess = mu - risk_free_daily
    Sigma = np.cov(returns.T)
    Sigma_inv = np.linalg.inv(Sigma)

    Sigma_min = p_excess ** 2 / (mu_excess.T @ Sigma_inv @ mu_excess)
    eta = Sigma_min / p_excess

    weights_array = eta * Sigma_inv @ mu_excess

    return weights_array

"""
    weights = {}
    for i in range(len(tickers)):
        weights[tickers[i]] = weights_array[i]

    return weights
"""


if "__main__" == __name__:
    tickers = ["NVDA", "GOOG", "BRK-B", "AAPL", "TSLA"]
    print(get_efficient_portfolio(tickers, 0.3, 0.05))
