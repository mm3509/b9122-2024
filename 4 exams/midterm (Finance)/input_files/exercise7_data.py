# Don't submit this file.

import os
import random
import numpy as np


def load_data():

    random.seed(42, version=2)

    d = os.path.dirname(__file__)

    y = np.loadtxt(os.path.join(d, "y.txt"))
    x = np.loadtxt(os.path.join(d, "x.txt"))

    n = y.shape[0]
    test_indices = random.sample(list(range(n)), int(n * 0.3))
    train_indices = [i for i in range(n) if i not in test_indices]

    x_test = x[test_indices, :]
    y_test = y[test_indices]
    x_train = x[train_indices, :]
    y_train = y[train_indices]

    return (x_test, y_test), (x_train, y_train)
