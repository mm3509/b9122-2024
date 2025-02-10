import random

import pandas as pd
import numpy as np
import sklearn.linear_model
import sklearn.metrics
import sklearn.preprocessing
import sklearn.neighbors
import sklearn.neural_network

import exercise5
from exercise5 import SECTOR, PRICE, DIVIDEND_YIELD, EBITDA
from exercise5 import MARKET_CAP, ASSETS, REVENUE, EARNINGS_PER_SHARE


CATEGORY = "Category"
FEATURES = [PRICE, DIVIDEND_YIELD, EARNINGS_PER_SHARE, MARKET_CAP, ASSETS,
            REVENUE, EBITDA]


def set_seed():
    """
    This function sets the seeds and ensures reproducible results
    on Autograder.

    No doc-tests.

    """
    random.seed(42, version=2)
    np.random.seed(seed=42)


def prepare_data(data_filepath=exercise5.DATA_FILEPATH):
    """
    No doc-tests.
    """

    df = exercise5.prepare_data(data_filepath)

    # Students: this line converts a string to categorical codes,
    # 0-10. Leave it as is.
    y = df[SECTOR].astype('category').cat.codes  # noqa: F841, E501

    # TODO: complete this function to return a tuple with X and Y.

    return


def split_data(x, y):
    """
    No doc-tests.
    """
    set_seed()
    return sklearn.model_selection.train_test_split(x, y, test_size=0.2)


def fit_logistic(x_train, y_train):
    """
    No doc-tests.
    """
    set_seed()

    # TODO: complete this function to retun the logistic model fit to
    # the data.

    return


def fit_knn(x_train, y_train):
    """
    No doc-tests.
    """
    set_seed()

    # TODO: complete this function to retun the kNN model fit to
    # the data.

    return


def fit_mlp(x_train, y_train):
    """
    No doc-tests.
    """
    set_seed()

    # TODO: complete this function to retun the Multi-Layer Perceptron
    # model fit to the data.

    return


def compute_accuracy(model, x_test, y_test):
    """
    No doc-tests.
    """

    # TODO: complete this function

    return


if "__main__" == __name__:

    x, y = prepare_data()
    x_train, x_test, y_train, y_test = split_data(x, y)
    for model in ["logistic", "knn", "mlp"]:

        # Students: this line uses `eval()` in order to be DRY.
        # If you don't understand, don't worry, you don't have to change it.
        model_fit = eval("fit_" + model + "(x_train, y_train)")
        accuracy = compute_accuracy(model_fit, x_test, y_test)
        print("Accuracy of %s model: %.2f" % (model, accuracy))
