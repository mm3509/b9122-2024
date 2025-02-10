import datetime
import os
import pathlib


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

YAHOO_OUTCOME = "^SPX"
FRED_FEATURE = "DFF"
START_DATE = "1954-07-01"
TODAY = datetime.date.today().isoformat()[:len(START_DATE)]

###############################################################################
#
# !! ATTENTION: When submitting to Autograder, do not edit the file below this
# line, or Autograder will fail !!
#
###############################################################################

THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, "data.csv")

with open(os.path.join(THIS_DIR, "api_key.txt")) as f:
    API_KEY = f.read().strip()


def setup(data_filepath=DATA_FILEPATH):

    fred = fredapi.Fred(API_KEY)
    feature = fred.get_series(FRED_FEATURE)
    feature.name = FRED_FEATURE

    # Download financial data from Yahoo Finance. No need for API key.
    yahoo_data = yf.download(YAHOO_OUTCOME,
                             start=START_DATE,
                             end=TODAY)
    outcome = yahoo_data[["Close"]]

    # Use this redundant syntax to avoid warning from Pandas.
    outcome = outcome.rename(columns={"Close": YAHOO_OUTCOME})

    # Merge the two series and save to NumPy.
    merged = pd.merge(outcome, feature,
                      how="inner",
                      left_index=True,
                      right_index=True)
    merged.sort_index(inplace=True)
    merged_numpy = merged.to_numpy()

    np.savetxt(DATA_FILEPATH, merged_numpy)


if "__main__" == __name__:
    setup()
