#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import numpy as np


def linear(x):
    """linear activation

    y = x

    Arguments:
        x {lists or array} -- inputs

    Returns:
        array -- outputs
    """
    return x


def sigmoid(x):
    """sigmoid function

    :math:`y = e^x / (e^x + 1)` 


    Arguments:
        x {[type]} -- [description]
    """
    ex = np.exp(x)
    return ex


def tanh(x):
    r"""Computes sigmoid of `x` element-wise.

    Specifically, `y = 1 / (1 + exp(-x))`.

    Args:
      x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
      name: A name for the operation (optional).

    Returns:
      A `Tensor`. Has the same type as `x`.
    """

    return x


def softplus(x):
    pass


def softsign(x):
    pass


def elu(x):
    pass


def relu(x):
    pass


def relu6(x):
    pass


def selu(x):
    pass


def crelu(x):
    pass


def leaky_relu(x):
    pass


if __name__ is '__main__':

    activations = ['linear', 'tanh', 'sigmoid', 'softplus', 'softsign',
                   'elu', 'relu', 'selu', 'crelu', 'relu6', 'leaky_relu']
    x = np.linespace(-10, 10, 200)

    for activation in activations:
        globals()[activation]()
