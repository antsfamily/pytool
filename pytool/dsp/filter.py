from __future__ import absolute_import

import numpy as np


def fir(c, X):
    X = X.transpose()

    M, N = X.shape
    return np.sum(c * X, 1)


if __name__ == '__main__':
    c = np.array([1, 2, 3, 4])
    X = np.ones((4, 5))
    X[2, 3] = 0
    print(fir(c, X))

    a = 2.3
    b = 2 + 3j
    print(a * b)
