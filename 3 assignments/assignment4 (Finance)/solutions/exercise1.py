import os

import pandas as pd

import data_tools


USE_CACHE = False


def download_and_merge(tickers):

    if USE_CACHE:
        fp = ",".join(tickers) + ".ft"
        if os.path.exists(fp):
            return pd.read_feather(fp)

    first = True
    for ticker in tickers:
        if first:
            merged = data_tools.download_yfinance(ticker)
            first = False
            continue

        data = data_tools.download_yfinance(ticker)
        merged = pd.merge(merged,
                          data,
                          how="inner",
                          left_index=True,
                          right_index=True)

    if USE_CACHE:
        merged.to_feather(fp)

    return merged


if "__main__" == __name__:
    print(download_and_merge(["AAPL", "GOOG", "MSFT"]))
