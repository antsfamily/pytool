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


def read_mnist(rootdir=None, dataset='train', scale=False, isonehot=False, verbose=False):

    cnt = -1
    nClass = 10
    print("reading dataset: " + dataset + "...")
    X = []
    Y = []
    if os.path.exists(rootdir + dataset) is False:
        ValueError(rootdir + dataset, " is not exist!")
    for parent, dirnames, filenames in os.walk(rootdir + dataset):
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

    if scale:
        X = X / 255.0

    if verbose:
        print(X.shape, Y.shape)
    return X, Y


if __name__ == '__main__':
    rootdir = '../../data/mnist/'
    dataset = 'demo'
    read_mnist(rootdir=rootdir, dataset=dataset, isonehot=True, verbose=True)


