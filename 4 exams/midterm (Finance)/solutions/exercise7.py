import random


import numpy as np
import requests
import sklearn.linear_model


import exercise7_data


LOGISTIC_REGRESSION_THRESHOLD = 0.3


def run_logistic(x, y):

    reg = sklearn.linear_model.LogisticRegression()
    reg.fit(x, y)

    print("Logistic regression coefficients: ", reg.coef_)
    return reg.coef_


def compute_accuracy(true_outcomes, predicted_outcomes):

    n = true_outcomes.shape[0]
    return 1 - np.sum(np.abs(true_outcomes - predicted_outcomes)) / n    


def compute_accuracy_logistic(x_test, y_test, x_train, y_train):

    coef = run_logistic(x_train, y_train)

    arg_predicted = np.matmul(x_test, coef.T)
    y_predicted = 1 / (np.exp(-arg_predicted) + 1)
    
    yes_no = (y_predicted >= LOGISTIC_REGRESSION_THRESHOLD).astype(int)[:, 0]

    acc = compute_accuracy(yes_no, y_test)
    print("Logistic regression accuracy: ", acc)
    return acc
    

def predict_knn1(x, x_train, y_train):

    distances = np.square(x - x_train)
    nearest = np.argmin(distances)

    return y_train[nearest], nearest


def compute_accuracy_knn1(x_test, y_test, x_train, y_train):

    x_train_knn = x_train[:, 0]
    x_test_knn = x_train[:, 0]

    y_predicted = []
    for i in range(y_test.shape[0]):
        x = x_test_knn[i]
        prediction, _ = predict_knn1(x, x_train_knn, y_train)
        y_predicted.append(prediction)

    acc = compute_accuracy(y_test, np.array(y_predicted))
    print("k-Nearest neighbors accuracy: ", acc)

    return acc

    
if "__main__" == __name__:
    (x_test, y_test), (x_train, y_train) = exercise7_data.load_data()

    # You can complete this code here to develop and debug your
    # regressions, using data x_train and y_train.
    compute_accuracy_logistic(x_test, y_test, x_train, y_train)
    compute_accuracy_knn1(x_test, y_test, x_train, y_train)
