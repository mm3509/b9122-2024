import pathlib
import datetime
import os


import fredapi
import yfinance as yf
import pandas as pd
import numpy as np

###############################################################################
#
# TODO: edit these lines with your data, until the next heading like this one.
#
# TODO: get an API key for the Federal Reserve Economic Database (FRED)
# following these steps, and save it in the same folder as `api_key.txt`
#
###############################################################################

YAHOO_OUTCOME = "EDD"  # Morgan Stanley Emerging Markets Domestic Debt Fund
FRED_FEATURE = "TEDRATE"  # Spread of Treasury over Libor, measure of risk
START_DATE = "1986-01-02"
TODAY = "2022-01-21"

###############################################################################
#
# !! ATTENTION: When submitting to Autograder, do not edit the file below this
# line, or Autograder will fail !!
#
###############################################################################

DATA_FILEPATH = "data.csv"

def setup(data_filepath=DATA_FILEPATH):

    fred = fredapi.Fred()
    feature = fred.get_series(FRED_FEATURE)
    feature.name = FRED_FEATURE

    # Download financial data from Yahoo Finance. No need for API key.
    outcome = yf.download(YAHOO_OUTCOME, start=START_DATE, end=TODAY)[["Close"]]

    # Use this redundant syntax to avoid warning from Pandas.
    outcome = outcome.rename(columns={"Close": YAHOO_OUTCOME})

    # Merge the two series and save to NumPy.
    merged = pd.merge(feature, outcome, how="inner", left_index=True, right_index=True)
    merged.sort_index(inplace=True)
    merged.dropna(inplace=True)
    merged_numpy = merged.to_numpy()

    np.savetxt(DATA_FILEPATH, merged_numpy)


if "__main__" == __name__:
    setup()
