from keras.datasets import mnist

import knn


(TRAIN_X, TRAIN_y), (TEST_X, TEST_y) = mnist.load_data()

SAMPLE_IMAGES_WITH_BUG = [1, 4, 6, 7, 8, 9, 10]


def autograder_test_with_image(i):
    test_image = TEST_X[i]
    student_solution, _ = knn.kNN1(test_image, TRAIN_X, TRAIN_y)
    if TEST_y[i] != student_solution:
        print("You still have a bug on image %d" % i)


def autograder_sample_test():
    for i in SAMPLE_IMAGES_WITH_BUG:
        autograder_test_with_image(i)


if __name__ == "__main__":
    autograder_sample_test()
