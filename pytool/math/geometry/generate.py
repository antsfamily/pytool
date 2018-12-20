#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-17 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import random
import numpy as np


def circle1(x0, y0, r, nps):
    r"""Generates circle (x, y)

    :math:`(x-x_0)^2 + (y-y_0)^2 = r^2`

    Arguments:
       x0 {Float} -- x coordinate of circle center
       y0 {Float} -- y coordinate of circle center
       r {Float} -- radius of circle
       nps {Integer} -- number of points
    """

    xmin = x0 - r
    xmax = x0 + r

    x = np.linspace(xmin, xmax, nps)
    y1 = y0 - np.sqrt(r * r - (x - x0) ** 2)
    y2 = y0 + np.sqrt(r * r - (x - x0) ** 2)

    x = np.concatenate((x, x), axis=0)
    y = np.concatenate((y1, y2), axis=0)
    return x, y


def circle2(x0, y0, r):
    r"""Generates circle (x, y)

    :math:`(x-x_0)^2 + (y-y_0)^2 = r^2`

    Arguments:
       x0 {Float} -- x coordinate of circle center
       y0 {Float} -- y coordinate of circle center
       r {Float} -- radius of circle
       nps {Integer} -- number of points
    """

    angles_circle = [i * np.pi / 180 for i in range(0, 360)]
    x = x0 + r * np.cos(angles_circle)
    y = y0 + r * np.sin(angles_circle)

    return x, y


def ellipse(a, b):
    """[summary]

    [description]

    Arguments:
       a {[type]} -- [description]
       b {[type]} -- [description]
    """
    pass


def ellipse_surface(a, b, x0, y0, nps, mod):
    """generates ellipse surface

    :math:`\frac{(x-x_0)^2}{a^2} + \frac{{y-y_0}^2}{b^2} \ngt 1`

    Arguments:
       a {float} -- axis of ellipse
       b {float} -- axis of ellipse
       x0 {float} -- x center of ellipse
       y0 {float} -- y center of ellipse
       nps {Integer} -- number of points
       mod {float} -- mode: 'rand' or 'order'
    """

    if mod is None:
        mod = 'order'

    aa = a ** 2
    bb = b ** 2

    xmin = x0 - a
    xmax = x0 + a
    ymin = y0 - b
    ymax = y0 + b

    x = []
    y = []

    if mod is 'order':
        xx = np.linspace(xmin, xmax, nps)
        yy = np.linspace(ymin, ymax, nps)
        for xi in xx:
            for yj in yy:
                if (xi - x0) ** 2 / aa + (yj - y0) ** 2 / bb <= 1:
                    x.append(xi)
                    y.append(yj)

    cnt = 0
    if mod is 'rand':
        for i in range(0, 10 * nps):
            # print(i)
            xi = (xmax - xmin) * np.random.rand(1) + xmin
            yi = (ymax - ymin) * np.random.rand(1) + ymin
            if (xi - x0) ** 2 / aa + (yi - y0) ** 2 / bb <= 1:
                x.append(xi[0])
                y.append(yi[0])
            if cnt < nps:
                cnt = cnt + 1
            else:
                break
    return x, y


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    x, y = circle1(0, 0, 1, 1000)
    plt.figure()
    plt.plot(x, y, '.')
    plt.title('circle')
    plt.show()

    x, y = circle2(0, 0, 1)
    plt.figure()
    plt.plot(x, y, '.r')
    plt.title('circle')
    plt.show()

    x, y = ellipse_surface(8, 2, 1, 1, 1000, 'rand')
    x, y = ellipse_surface(8, 2, 1, 1, 100, 'order')
    plt.figure()
    plt.scatter(x, y, c='g', marker='+')
    plt.axis('equal')
    plt.title('ellipse surface')
    plt.show()
