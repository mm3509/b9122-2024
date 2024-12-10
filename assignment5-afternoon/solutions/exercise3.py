import os
import pathlib


from sklearn import preprocessing, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron

import pandas as pd


THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, "loans.csv")

OUTCOME = "Loan_Status"
ID_COLUMN = "Loan_ID"


def load_data(data_filepath=DATA_FILEPATH, verbose=True):
    df = pd.read_csv(data_filepath)
    df.dropna(inplace=True)

    # Drop Property_Area, which has 3 categories; to include it, you'd
    # need to use `pd.get_dummies()` and add columns for the dummy
    # variables, 0/1.
    df.drop(columns=["Property_Area"], inplace=True)

    # Preprocess binary categories from strings to integers.
    for column in df.columns:
        if "object" != df.dtypes[column]:
            continue

        df[column] = df[column].astype("category").cat.codes

    x = df.drop([OUTCOME, ID_COLUMN], axis=1).values
    x_rescaled = preprocessing.scale(x)

    y = df[OUTCOME].values

    return x_rescaled, y


def split_data(x, y):

    return train_test_split(x, y, test_size=0.2, random_state=42)


def fit_data(x_train, y_train, eta=0.1):

    # TODO: complete this function.
    model = Perceptron(eta0=eta)
    model.fit(x_train, y_train)

    return model


def compute_accuracy(model, x_test, y_test):

    # TODO: complete this function.
    y_predicted = model.predict(x_test)
    return metrics.accuracy_score(y_test, y_predicted)


if __name__ == "__main__":
    x, y = load_data()
    x_train, x_test, y_train, y_test = split_data(x, y)

    model = fit_data(x_train, y_train)
    print(compute_accuracy(model, x_test, y_test))
