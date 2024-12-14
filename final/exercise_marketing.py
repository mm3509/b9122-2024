import os
import pathlib

import numpy as np
import pandas as pd
import sklearn.linear_model
import sklearn.preprocessing


PROPENSITY = "propensity"
VISIT = "visit"

THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, 'doctors.ft')

FEATURES = ['scripts1', 'specialty_CARD', 'specialty_ENDO',
            'specialty_FP', 'specialty_GP', 'specialty_IM', 'specialty_OBGYN',
            'region_Midwest', 'region_Northeast', 'region_South',
            'region_West', 'degree_date']


def load_data(data_filepath=DATA_FILEPATH):
    """
    No doc-tests.
    """
    return pd.read_feather(data_filepath)


def naive(df):
    """
    No doc-tests.
    """

    df["diff"] = df["scripts2"] - df["scripts1"]

    visited = df.loc[df[VISIT]]
    non_visited = df.loc[~df[VISIT]]

    visited["diff"].mean() - non_visited["diff"].mean()


def propensity(df):
    """
    No doc-tests.
    """

    # TODO: complete this function and add a column with name
    # "propensity" to the dataframe.

    return df


def compute_propensity_distance(row, propensity):
    """
    This function the distance for propensity score matching for
    1-nearest neighbor. If the row was visited, the distance is
    infinite, so it's not selected.

    No doc-tests.

    """

    # Students: Don't change this.

    if row[VISIT]:
        return np.inf

    return (row[PROPENSITY] - propensity) ** 2


def find_non_visited_clone(df, propensity):
    """
    This function returns the non-visited doctors closest in propensity score
    to the one given.

    No doc-tests.
    """

    # Students: don't change this function.

    distances = df.apply(
        lambda row: compute_propensity_distance(row, propensity), axis=1
    )

    return distances.argmin()


def estimate_causal(df):
    """
    No doc-tests.
    """

    # TODO: complete this function.

    return 0


def main():
    df = load_data()
    print("Naive estimation:", naive(df))

    df = propensity(df)

    print("Causal estimation:", estimate_causal(df))


if '__main__' == __name__:
    main()
