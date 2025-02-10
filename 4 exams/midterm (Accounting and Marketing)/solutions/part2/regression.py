import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model


from get_data import DATA_FILEPATH

def load_data(data_filepath):
    """
    Reads data from NumPy text format.
    """

    return np.loadtxt(data_filepath)


def prepare_data(data_filepath):

    data = load_data(data_filepath)

    y_raw = data[:, 0].reshape((-1, 1))
    x_raw = data[:, 1].reshape((-1, 1))

    y_log = np.log(y_raw)

    # Use np.diff() or this code (same thing):
    # x = x[1:,] - x[:-1,]

    x = np.diff(x_raw, axis=0)
    y = np.diff(y_log, axis=0)

    return x, y


def add_constant(x):
    return np.hstack([np.ones(x.shape), x])


def regression_numpy(data_filepath):

    x, y = prepare_data(data_filepath)

    x_with_constant = add_constant(x)

    xx = np.matmul(x_with_constant.T, x_with_constant)
    xx_inv = np.linalg.inv(xx)
    xy = np.matmul(x_with_constant.T, y)

    beta_hat = np.matmul(xx_inv, xy)

    return beta_hat[1, 0]


def regression_sklearn(data_filepath):

    x, y = prepare_data(data_filepath)

    reg = sklearn.linear_model.LinearRegression().fit(x, y)

    return reg.coef_[0, 0]


def regression_covariance(data_filepath):

    x_array, y_array = prepare_data(data_filepath)

    # Convert to 1-D array for computing covariance.
    x = x_array[:, 0]
    y = y_array[:, 0]

    covariance_matrix = np.cov(x, y, bias=True)

    beta_hat = covariance_matrix[0, 1] / covariance_matrix[0, 0]

    return beta_hat


def compare_floats_with_precision(a, b, precision=1e-14):
    return abs(a - b) < precision


def check_results(data_filepath):
    """Confirm that the results are the same with the three methods.

    If not, this function raises an AssertionError (not a ValueError,
    because the issue is the logic inside your code, and ValueErrors
    are mean that the arguments passed by some one outside your own
    code do not conform to your expectations.

    """

    coeff_numpy = regression_numpy(data_filepath)
    coeff_sklearn = regression_sklearn(data_filepath)
    coeff_covariance = regression_covariance(data_filepath)

    assert compare_floats_with_precision(coeff_numpy, coeff_sklearn)
    assert compare_floats_with_precision(coeff_numpy, coeff_covariance)


    with open("part2_exercise3.txt", "w+") as f:
        f.write(str(coeff_covariance))


def plot(fn, data_filepath, output_filepath):

    coeff = fn(data_filepath)
    x, y = prepare_data(data_filepath)

    beta_hat = fn(data_filepath)
    constant = np.mean(y - beta_hat * x)
    y_predicted = constant + beta_hat * x

    plt.figure()
    plt.scatter(x, y)
    plt.plot(x, y_predicted, c="r")
    plt.savefig(output_filepath, dpi=72)


def main():
    # This function runs the three regression and saves the plots. You
    # don't have to change it, but you can if you want.
    check_results(data_filepath=DATA_FILEPATH)
    counter = 0
    for fn in [regression_numpy, regression_sklearn, regression_covariance]:
        counter += 1
        plot(fn, DATA_FILEPATH, "plot%d.png" % counter)


if __name__ == "__main__":
    # If you run this file from the shell, it will run the three
    # regressions and save the three plots.
    main()
