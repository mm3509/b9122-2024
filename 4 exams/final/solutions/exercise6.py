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
    random.seed(42, version=2)
    np.random.seed(seed=42)


def prepare_data(data_filepath=exercise5.DATA_FILEPATH):
    """
    No doc-tests.
    """

    df = exercise5.prepare_data(data_filepath)
    
    # Students: this line converts a string to categorical codes,
    # 0-10. Leave it as is.
    y = df[SECTOR].astype('category').cat.codes

    x = df[FEATURES].values

    x_rescaled = sklearn.preprocessing.scale(x)

    return x_rescaled, y


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

    logistic = sklearn.linear_model.LogisticRegression()

    logistic.fit(x_train, y_train)

    return logistic


def fit_knn(x_train, y_train):

    set_seed()
    
    knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(x_train, y_train)

    return knn


def fit_mlp(x_train, y_train):

    set_seed()
    
    mlp = sklearn.neural_network.MLPClassifier(
        hidden_layer_sizes=(128, 64, 32),
        activation="logistic",
        max_iter=int(1e4),
        random_state=42
    )
    mlp.fit(x_train, y_train)

    return mlp


def compute_accuracy(model, x_test, y_test):

    predicted = model.predict(x_test)
    accuracy = sklearn.metrics.accuracy_score(y_test, predicted)

    return accuracy


if "__main__" == __name__:

    set_seed()
    x, y = prepare_data()
    x_train, x_test, y_train, y_test = split_data(x, y)

    # TODO: remove this before publishing. It serves to get data for
    # Autograder.
    chosen = random.sample(list(range(len(y_test))), 10)
    input_list = [list(x_test[i, :]) for i in chosen]
    
    #print(input_list[0])
    #assert False
    print(x)

    point0 = np.array([-0.490893632144405, -0.037160448730479384, -0.43545196480320064, -1.0590465507558866, -0.011524346184616169, -0.922526967678399, -0.596478960997876]).reshape(1, -1)  # noqa: E501
    
    for model in ["knn", "logistic", "knn", "mlp"]:
        model_fit = eval("fit_" + model + "(x_train, y_train)")
        print(model_fit.predict(point0))
        assert False
        accuracy = compute_accuracy(model_fit, x_test, y_test)
        print("Accuracy of %s model: %.2f" % (model, accuracy))
