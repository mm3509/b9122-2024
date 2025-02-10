import random


import numpy as np
import requests
import sklearn.linear_model


import exercise7_data


LOGISTIC_REGRESSION_THRESHOLD = 0.3


def run_logistic(x, y):
    """
    Run logistic regression and return a NumPy array with coefficients.
    """

    # Note: no doc-tests.

    # TODO: complete this function.
    return None


def compute_accuracy(true_outcomes, predicted_outcomes):
    """
    Compute accuracy from predictions relative to true values.
    """
    # Note: no doc-tests.

    # TODO: complete this function.
    return None


def compute_accuracy_logistic(x_test, y_test, x_train, y_train):
    """
    Computes accuracy of logistic regression on training data
    using the test dataset as a benchmark.
    """
    # Note: no doc-tests.

    # TODO: complete this function.
    return None


def predict_knn1(x, x_train, y_train):
    """
    Predicts 1-nearest neighbor on new input x from training data.
    """
    # Note: no doc-tests.

    # TODO: complete this function.
    return None


def compute_accuracy_knn1(x_test, y_test, x_train, y_train):
    """
    Computes accuracy of 1-nearest neighbor from training data
    using the test dataset as a benchmark.
    """
    # Note: no doc-tests.

    # TODO: complete this function.
    return None


if "__main__" == __name__:
    (x_test, y_test), (x_train, y_train) = exercise7_data.load_data()

    # You can complete this code here to develop and debug your
    # regressions, using data x_train and y_train.
