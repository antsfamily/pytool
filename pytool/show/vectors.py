#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version   : $1.0$

import numpy as np
import pytool
from matplotlib import pyplot as plt


def plot_vectors2d(vectors, xse=None, yse=None, nPoints=None, title=None, colorlines=None):

    if nPoints is None:
        for vector, colorline in zip(vectors, colorlines):
            print(vector)
            plt.plot([0, vector[0]], [0, vector[1]], colorline)
    else:
        x = np.linspace(xse[0], xse[1], nPoints)
        for vector, colorline in zip(vectors, colorlines):
            if vector[0] == 0:
                k = 10e38
                x = np.zeros(nPoints) + (xse[1] + xse[0]) / 2
                y = np.linspace(yse[0], yse[1], nPoints)
                plt.plot(x, y, colorline)
            else:
                k = vector[1] / vector[0]
                # print(vector, k)
                y = k * x
                plt.plot(x, y, colorline)

    if yse is not None:
        plt.axis(xse + yse)
    plt.title(title)
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
