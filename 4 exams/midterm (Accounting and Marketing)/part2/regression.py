import matplotlib.pyplot as plt
import numpy as np


from get_data import DATA_FILEPATH


def load_data(data_filepath):
    """
    Reads data from NumPy text format.
    """

    return np.loadtxt(data_filepath)


def prepare_data(data_filepath):

    data = load_data(data_filepath)

    # TODO: complete this function

    return None


def regression_numpy(data_filepath):

    # TODO: complete this function.
    return None


def regression_sklearn(data_filepath):

    # TODO: complete this function.
    return None


def regression_covariance(data_filepath):

    # TODO: complete this function.
    return None


def check_results(data_filepath):
    """Confirm that the results are the same with the three methods.

    If not, this function raises an AssertionError (not a ValueError,
    because the issue is the logic inside your code, and ValueErrors
    are mean that the arguments passed by some one outside your own
    code do not conform to your expectations.

    """

    # TODO: complete this function.
    return None


def plot(fn, data_filepath, output_filepath):

    coeff = fn(data_filepath)
    x, y = prepare_data(data_filepath)

    # TODO: complete this function to compute y_predicted,
    # instead of it being an array of zeroes.

    y_predicted = np.zeros(y.shape)

    # When you have y_predicted, you can plot it here. You can edit
    # these lines if you want to play with Matplotlib, but you don't
    # have to.
    plt.figure()
    plt.scatter(x, y)
    plt.plot(x, y_predicted, c="r")
    plt.savefig(output_filepath, dpi=72)


def main():
    """
    Run the three regression and saves the plots. You don't have to
    change this function, but you can if you want.
    """
    check_results(data_filepath=DATA_FILEPATH)
    counter = 0
    for fn in [regression_numpy, regression_sklearn, regression_covariance]:
        counter += 1
        plot(fn, DATA_FILEPATH, "plot%d.png" % counter)


if __name__ == "__main__":
    # If you run this file from the shell, it will run the three
    # regressions and save the three plots.
    main()
