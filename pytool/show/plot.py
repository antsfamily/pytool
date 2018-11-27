#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	  : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link	  : http://blog.csdn.net/enjoyyl
# @Version   : $1.0$

import numpy as np
import pytool
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def __init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def __animate(i):
    line.set_ydata(a)  # update the data.
    return line,


def aplot():
    pass


def mesh(Z):

    fig = plt.figure()
    ax = Axes3D(fig)
    # print(type(Z), Z)
    M, N = np.shape(Z)
    print(M, N)

    X = np.arange(0, N, 1)
    Y = np.arange(0, M, 1)
    X, Y = np.meshgrid(X, Y)

    # rstride（row）和cstride(column)表示的是行列的跨度
    ax.plot_surface(X, Y, Z,
                    rstride=1,  # 行的跨度
                    cstride=1,  # 列的跨度
                    cmap=plt.get_cmap('rainbow')  # 颜色映射样式设置
                    )

    # offset 表示距离zdir的轴距离
    # ax.contourf(X, Y, Z, zdir='z', offest=0, cmap='rainbow')
    # ax.set_zlim(0, np.max(Z[:]))

    plt.title("Z")
    plt.xlabel("x")
    plt.xlabel("y")
    plt.show()

if __name__ == '__main__':
    pass
