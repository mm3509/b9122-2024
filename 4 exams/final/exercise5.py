import os
import pathlib

import numpy as np
import pandas as pd
import sklearn.linear_model


THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, "sp500.csv")


SECTOR = "Sector"
PRICE = "Price"
DIVIDEND_YIELD = "Dividend Yield"
EARNINGS_PER_SHARE = "Earnings/Share"
MARKET_CAP = "Market Cap"
ASSETS = "Assets"
REVENUE = "Revenue"
EBITDA = "EBITDA"

FEATURES = [DIVIDEND_YIELD, EARNINGS_PER_SHARE, MARKET_CAP, EBITDA,
            ASSETS, REVENUE]


def prepare_data(data_filepath=DATA_FILEPATH):

    df = pd.read_csv(data_filepath)

    # Students: drop rows with negative EBITDA, for simplicity.
    df.drop(df[df[EBITDA] <= 0].index, inplace=True)

    # TODO: complete this function to treat the data (no scaling).

    return df


def run_linear_regression(data_filepath=DATA_FILEPATH):

    data = prepare_data(data_filepath)  # noqa: F841

    # TODO: complete this function.

    return


if "__main__" == __name__:
    print(run_linear_regression())
