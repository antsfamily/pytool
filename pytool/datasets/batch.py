#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$


import os
import shutil
import numpy as np


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
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batchsize + 1, batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt], targets[excerpt]
