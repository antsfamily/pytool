#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version   : $1.0$

import numpy as np
from matplotlib import pyplot as plt


def plot_circles(Cis=None, Ris=None, colorlines=None, dTheta=None, title=None, legend=None, isplot=None):
    """2d circles Visualization

    plot 2d circles

    Arguments:
        Cis {list} -- [center1, center2, ...] , centeri: x0 + jy0

    Keyword Arguments:
        Ris {list} -- radius of circles
        yse {list} -- start and end of y (default: {None})
        colorlines {list} -- such as ['-r', '-b'] (default: {None})
        dTheta {float} -- angle accuracy in radian (default: {None, 0.01})
        title {string} -- figure title (default: {None})
    """

    if dTheta is None:
        dTheta = 0.01

    theta = np.arange(0, 2 * np.pi, dTheta)
    xs = []
    ys = []
    for Ci, Ri in zip(Cis, Ris):

        a = np.real(Ci)
        b = np.imag(Ci)
        r = np.abs(Ri)

        x = a + r * np.cos(theta)
        y = b + r * np.sin(theta)

        xs.append(x)
        ys.append(y)

    if isplot is True:
        for x, y, colorline in zip(xs, ys, colorlines):
            plt.plot(x, y, colorline)
        plt.grid()
        plt.title(title)
        plt.axis('equal')
        plt.xlabel('real axis/x')
        plt.ylabel('image axis/y')
        plt.legend(legend)
        plt.show()
    return xs, ys
