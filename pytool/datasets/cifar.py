#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import cPickle
import os
import shutil
import numpy as np


def unpickle2(file):
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict


def read_cifar100(rootdir=None, dataset='train', scalevalue=None, isonehot=False, verbose=False):
    r"""read cifar100 dataset

    read cifar100 dataset

    Keyword Arguments:
        rootdir {str} -- dataset folder (default: {None})
        dataset {str} -- dataset name (default: {'train'})
        scalevalue {float} -- scale value (default: {None})
        isonehot {bool} -- gen one hot label matrix (default: {False})
        verbose {bool} -- show more info (default: {False})

    Returns:
        numpy array X  -- [N, 32, 32, 3]
        numpy array Yf -- [N, 100]
        numpy array Yc -- [N, 20]

    Raises:
        ValueError -- dataset path not available
    """

    print("===reading dataset: " + dataset + "...")
    datasetpath = os.path.join(rootdir, dataset)
    if os.path.exists(datasetpath) is False:
        raise ValueError(datasetpath + " is not exist!")
    print("---dataset path: " + datasetpath)

    obj = unpickle2(datasetpath)

    X = obj['data']
    Yf = obj['fine_labels']
    Yc = obj['coarse_labels']
    N, HWC = X.shape

    clf = np.unique(Yf)  # class label: 0~99
    clc = np.unique(Yc)  # 0~99
    nFineClass = len(clf)
    nCoarseClass = len(clc)

    # print(np.unique(Yf))  # 0~99
    # print(np.unique(Yc))  # 0~19

    X = np.reshape(X, (N, 3, 32, 32))
    X = np.transpose(X, (0, 2, 3, 1))

    if scalevalue:
        X = X / scalevalue

    # print(Yf[0:20], Yf[-20:-1])
    # print(Yc[0:20], Yc[-20:-1])
    if isonehot:
        Yf = np.eye(N, nFineClass)[Yf]  # N-nClass
        Yc = np.eye(N, nCoarseClass)[Yc]  # N-nClass
    # print(Yc[0:20, :])
    if verbose:
        print(X.shape, Yf.shape, Yc.shape)

    return X, Yf, Yc,


def read_cifar10(rootdir=None, dataset='train', scalevalue=None, isonehot=False, verbose=False):
    r"""read cifar10 dataset

    read cifar100 dataset

    Keyword Arguments:
        rootdir {str} -- dataset folder (default: {None})
        dataset {str} -- dataset name (default: {'train'})
        scalevalue {float} -- scale value (default: {None})
        isonehot {bool} -- gen one hot label matrix (default: {False})
        verbose {bool} -- show more info (default: {False})

    Returns:
        numpy array X  -- [N, 32, 32, 3]
        numpy array Y  -- [N, 10]

    Raises:
        ValueError -- dataset path not available
    """
    print("===reading dataset: " + dataset + "...")
    datasetpath = os.path.join(rootdir, dataset)
    if os.path.exists(datasetpath) is False:
        raise ValueError(datasetpath + " is not exist!")

    print("---dataset path: " + datasetpath)

    obj = unpickle2(datasetpath)
    # for k in obj.keys():
    #     print(k)
    # filename = obj['filenames']
    X = obj['data']
    Y = obj['labels']
    N, HWC = X.shape

    cl = np.unique(Y)  # class label: 0~99
    nClass = len(cl)

    # print(np.unique(Yf))  # 0~99
    # print(np.unique(Yc))  # 0~19

    X = np.reshape(X, (N, 3, 32, 32))
    X = np.transpose(X, (0, 2, 3, 1))

    if scalevalue:
        X = X / scalevalue

    # print(Yf[0:20], Yf[-20:-1])
    # print(Yc[0:20], Yc[-20:-1])
    if isonehot:
        Y = np.eye(N, nClass)[Y]  # N-nClass
    # print(Yc[0:20, :])
    if verbose:
        print(X.shape, Y.shape)

    return X, Y


if __name__ == '__main__':
    rootdir = '/mnt/e/DataSets/oi/cifar/cifar100/'
    dataset = 'train'
    read_cifar100(rootdir=rootdir, dataset=dataset,
                  isonehot=True, verbose=True)

    rootdir = '/mnt/e/DataSets/oi/cifar/cifar10/'
    dataset = 'test_batch'
    read_cifar10(rootdir=rootdir, dataset=dataset,
                 isonehot=True, verbose=True)
