import os
import pathlib

import numpy as np
import pandas as pd
import fredapi
import yfinance
import matplotlib.pyplot as plt

THIS_DIR = pathlib.Path(__file__).resolve().parent
RISK_FREE = "risk_free"
MARKET_RATE = "market_rate"
DATA_FILEPATH = "risk_free_rate.ft"
FED_FUNDS = "DFF"
SP500 = "^SPX"

START_DATE = "1986-01-02"
TODAY = "2024-11-07"

def download_yfinance(ticker):

    # Download financial data from Yahoo Finance. No need for API key.
    data = yfinance.download(ticker, start=START_DATE, end=TODAY)[["Close"]]

    # Use this redundant syntax to avoid a warning from Pandas.
    data = data.rename(columns={"Close": ticker})

    return data


def get_risk_free_and_market_rates():

    if os.path.exists(DATA_FILEPATH):
        return pd.read_feather(DATA_FILEPATH)

    with open(os.path.join(THIS_DIR, "api_key.txt")) as f:
        api_key = f.read().strip()

    fred = fredapi.Fred(api_key)
    risk_free = fred.get_series(FED_FUNDS)
    risk_free = np.exp(np.log(1 + risk_free.div(100)) / 250) - 1
    risk_free.name = RISK_FREE

    market = download_yfinance(SP500)
    market[SP500] = market[SP500].pct_change()
    market = market.rename(columns={SP500: MARKET_RATE})

    merged = pd.merge(market,
                      risk_free,
                      how="inner",
                      left_index=True,
                      right_index=True)

    merged.to_feather(DATA_FILEPATH)

    return merged



if "__main__" == __name__:
    get_risk_free_and_market_rates()
