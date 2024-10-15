import numpy as np
from keras.datasets import mnist

import matplotlib.pyplot as plt

###########################################################################
#
# TODO: Find the bug in the functions in this file (doc-tests omitted
# on purpose, to avoid indicating the location of the bug.)
#
###########################################################################


(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Convert the original white ink on black background to the more
# natural black ink, white background.
train_X = 255 - train_X
test_X = 255 - test_X


# Show a single image.
def image_show(data):
    x = data.reshape((28, 28))  # reshape it into 28x28 format
    plt.imshow(x, cmap='gray')  # show the image
    plt.show()


def distance(x, y):
    """Euclidean distance.
    """
    return np.sum(np.square(x.astype(np.uint32) - y.astype(np.uint32)))


def kNN1(x, data, label):
    """
    Simple 1-nearest neighbor algorithm.
    """

    distances = [distance(x, data[i]) for i in range(len(data))]
    nearest = np.argmin(distances)

    return label[nearest], nearest


def kNN(x, k, data, label):
    """
    Nearest-neighbors for the general case of k.
    """
    distances = [distance(x, data[i]) for i in range(len(data))]

    # To save time, use numpy.argpartition. It does not sort the entire
    # array; it only guarantees that the kth element is in sorted
    # position and all smaller elements will be moved before it. So
    # the first k elements will be the k-smallest elements.
    argsorted = np.argpartition(distances, k)

    # Find the most frequent class among the first k data points.
    classes, freq = np.unique(label[argsorted[:k]], return_counts=True)
    return classes[np.argmax(freq)]


def find_missed_images():
    """
    Find images that the kNN algorithm misses, maybe because of a
    bug.
    """

    missed = []
    for i in range(len(test_y)):
        x = test_X[i]
        label = test_y[i]

        prediction, nearest = kNN1(x, train_X, train_y)
        if prediction != label:
            print(i)
            missed.append(str(i))

            with open("debugged_images.txt", 'w+') as f:
                f.write("\n".join(missed))
