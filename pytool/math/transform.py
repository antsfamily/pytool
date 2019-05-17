#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import numpy as np


def normalize(X, mean=None, std=None):
    """normalize data

    .. math::
        X = \frac{X-mean}{std}

    Arguments:
        X {numpy array} -- data to normalized, N-H-W-C
        mean {list or tuple} -- mean of each channel (default: {None}, auto computed)
        std {list or tuple} -- standard deviation of each channel (default: {None}, auto computed)

    Returns:
        numpy array -- normalized
    """
    print("===normalize...")
    if np.ndim(X) is 3:
        H, W, C = X.shape
        X = X.reshape(1, H, W, C)

    N, H, W, C = X.shape
    if mean is None:
        mean = []
        for i in range(C):
            mean.append(np.mean(X[:, :, :, i]))
    if std is None:
        std = []
        for i in range(C):
            std.append(np.std(X[:, :, :, i]))

    print("---X.min(), X.max()", X.min(), X.max(), X.dtype)
    for i in range(C):
        X[:, :, :, i] = (X[:, :, :, i] - mean[i]) / std[i]
    print("---X.min(), X.max()", X.min(), X.max(), X.dtype)
    return X


if __name__ == '__main__':

    X = np.random.randn(5, 3, 4, 2)
    X = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[1, 2, 3], [4, 5, 6]],
                  [[1, 2, 3], [4, 5, 6]],
                  [[1, 2, 3], [4, 5, 6]]])
    print(X, X.shape)
    X = normalize(X)

    print(X)
