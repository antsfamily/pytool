#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import os
import shutil
import numpy as np
from scipy.misc import imread


def read_mnist(rootdir=None, dataset='train', scalevalue=None, isonehot=False, verbose=False):
    r"""read mnist dataset

    read mnist dataset

    Keyword Arguments:
        rootdir {str} -- dataset folder (default: {None})
        dataset {str} -- dataset name (default: {'train'})
        scalevalue {float} -- scale value (default: {None})
        isonehot {bool} -- gen one hot label matrix (default: {False})
        verbose {bool} -- show more info (default: {False})

    Returns:
        numpy array X  -- [N, 28, 28]
        numpy array Y  -- [N, 10]

    Raises:
        ValueError -- dataset path not available
    """

    cnt = -1
    nClass = 10
    print("reading dataset: " + dataset + "...")
    X = []
    Y = []
    datasetpath = os.path.join(rootdir, dataset)
    if os.path.exists(datasetpath) is False:
        raise ValueError(datasetpath + " is not exist!")
    for parent, dirnames, filenames in os.walk(datasetpath):
        if cnt == -1:
            labels = dirnames
            if verbose:
                print(parent, dirnames, filenames)
        else:
            if verbose:
                print(parent, dirnames, filenames)

            # gen label class
            label = int(labels[cnt])
            if isonehot:
                yy = np.zeros((nClass))
                yy[label] = 1
            else:
                yy = label
            # read image
            for filename in filenames:
                filepath = parent + '/' + filename
                # read image
                img = imread(filepath, 'L')  # RGB --> Gray
                # print(img.dtype, img.shape)
                X.append(img)

                Y.append(yy)
        cnt = cnt + 1
        if verbose:
            print(cnt)
    X = np.array(X)
    Y = np.array(Y)

    if scalevalue:
        X = X / scalevalue
        print(np.min(X), np.max(X))
        print("=============scaled!")

    if verbose:
        print(X.shape, Y.shape)
    return X, Y


if __name__ == '__main__':
    rootdir = '/home/liu/ws/tf/study/tfstudy/data/mnist/'
    dataset = 'demo'
    X, Y = read_mnist(rootdir=rootdir, dataset=dataset,
                      isonehot=True, verbose=True)
    print(X.shape, Y.shape)
    print(Y)
