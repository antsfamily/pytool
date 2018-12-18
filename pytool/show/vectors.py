#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version   : $1.0$

import numpy as np
import pytool
from matplotlib import pyplot as plt


def plot_vectors(vectors, startx, endx, nPoints=None, title=None, colorlines=None):

    if nPoints is None:
        for vector, colorline in zip(vectors, colorlines):
            plt.plot(vector, colorline)
    else:
        x = np.linspace(startx, endx, nPoints)
        for vector, colorline in zip(vectors, colorlines):
            k = vector[1] / vector[0]
            print(vector, k)
            y = k * x
            plt.plot(y, colorline)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
