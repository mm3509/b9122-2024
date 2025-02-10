import knn


def compute_accuracy(test_X=knn.test_X,
                     test_y=knn.test_y,
                     train_X=knn.train_X,
                     train_y=knn.train_y):
    """
    Compute the accuracy of the k-Nearest Neighbor algorithm on MNIST images.
    """

    cnt = 0

    for x, label in zip(test_X, test_y):
        prediction, nearest = knn.kNN1(x, train_X, train_y)
        if prediction == label:
            cnt += 1

    return cnt / len(test_y)
