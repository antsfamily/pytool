#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$


import os
import shutil
import numpy as np
from scipy.misc import imresize
import cv2


def get_batches(inputs, targets, batchsize, shuffle=True):
    r"""get batch data

    get batch data

    Arguments:
        inputs {[type]} -- net input
        targets {[type]} -- desired output
        batchsize {[type]} -- size of the batch

    Keyword Arguments:
        shuffle {bool} -- shuffle data (default: {True})

    Yields:
        [type] -- [description]
    """

    # iterate_minibatches
    assert len(inputs) == len(targets)
    indices = np.arange(len(inputs))
    if shuffle:
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batchsize + 1, batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt], targets[excerpt]


class DataBatch(object):

    def __init__(self, inputs, targets):
        assert len(inputs) == len(targets)
        self.nsamples = len(inputs)
        self.index = 0
        self.indices = np.arange(self.nsamples)
        self.inputs = inputs
        self.targets = targets

    def next_batch(self, batch_size, shuffle=True, resize=None):
        # Note that the 100 dimension in the reshape call is set by an assumed
        # batch size of 100

        if shuffle:
            if self.index < 1:
                np.random.shuffle(self.indices)

        x = self.inputs[self.indices[self.index:self.index + batch_size]]
        y = self.targets[self.indices[self.index:self.index + batch_size]]
        self.index = (self.index + batch_size) % len(self.inputs)
        # print("---", self.index, x.shape, x.min(), x.max())
        if resize is not None:
            resize = tuple(resize)
            X = []
            for xx in x:
                # X.append(imresize(xx, resize)) # after imresize --> [0, 255]
                X.append(cv2.resize(xx, resize[0:2]))
            x = np.array(X)
            X = None
        # print("---", self.index, x.shape, x.min(), x.max())
        return x, y
