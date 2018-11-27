#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	  : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link	  : http://blog.csdn.net/enjoyyl
# @Version   : $1.0$

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def showiq(IQV, adcmod=None, verbose=True):
    if adcmod is None:
        print("use default ADC mode: " + str(adcmod))
    plt.clf()
    if adcmod is 0x03:
        plt.plot(IQV[0], '-r')
        plt.plot(IQV[1], '-b')
        plt.plot(IQV[2], '.-r')
        plt.plot(IQV[3], '.-b')
        plt.grid()
        plt.title("echoes of radar")
        plt.legend(['I1', 'Q1', 'I2', 'Q2'])
    if adcmod is 0x13:
        plt.plot(IQV[0], '-r')
        plt.plot(IQV[1], '-b')
        plt.plot(IQV[2], '-g')
        plt.plot(IQV[3], '.-r')
        plt.plot(IQV[4], '.-b')
        plt.plot(IQV[5], '.-g')
        plt.title("echoes of radar")
        plt.legend(['I1', 'Q1', 'VGA1', 'I2', 'Q2', 'VGA2'])
    if verbose is True:
        plt.pause(0.01)
    plt.ioff()


def showtgecho(tgecho1, tgecho2, verbose=True):
    plt.clf()
    N = len(tgecho1)
    print(N)
    real = []
    imag = []
    for x in range(0, N, 2):
        real.append(tgecho1[x])
    for x in range(1, N, 2):
        imag.append(tgecho1[x])
    real = np.array(real)
    imag = np.array(imag)
    y1 = np.abs(real + 1j * imag)
   
    real = []
    imag = []
    for x in range(0, N, 2):
        real.append(tgecho1[x])
    for x in range(1, N, 2):
        imag.append(tgecho1[x])
    real = np.array(real)
    imag = np.array(imag)
    y2 = np.abs(real + 1j * imag)
    plt.plot(y1, '-r')
    plt.plot(y2, '-b')
    plt.title("FFT of orig echo")
    plt.legend(['RX1', 'RX2'])
    if verbose is True:
        plt.pause(0.01)
    plt.ioff()

def showmti(mti, verbose=True):
    if adcmod is None:
        print("use default ADC mode: " + str(adcmod))
    plt.clf()
    plt.plot(mti, '-r')
    plt.title("MTI")
    plt.legend(['mti'])
    if verbose is True:
        plt.pause(0.01)
    plt.ioff()

def showmtd(mtd, verbose=True):
    fig = plt.figure(0)
    ax = Axes3D(fig)
    # print(type(mtd), mtd)
    M, N = np.shape(mtd)
    print(M, N)

    X = np.arange(0, N, 1)
    Y = np.arange(0, M, 1)
    X, Y = np.meshgrid(X, Y)

    # rstride（row）和cstride(column)表示的是行列的跨度
    ax.plot_surface(X, Y, mtd, 
                    rstride=1,  # 行的跨度
                    cstride=1,  # 列的跨度
                    cmap=plt.get_cmap('rainbow')  # 颜色映射样式设置
                   )

    # offset 表示距离zdir的轴距离
    ax.contourf(X, Y, mtd, zdir='z', offest=-2, cmap='rainbow')
    ax.set_zlim(0, np.max(mtd[:]))

    plt.title("MTD")
    plt.xlabel("range")
    plt.title("velocity")
    if verbose is True:
        plt.pause(0.01)

def showana(mti, cfarth, verbose=True):
    plt.clf()
    plt.plot(cfarth, '-r')
    plt.plot(mti, '-b')
    plt.grid()
    plt.legend(['TH of CFAR', 'abs(MTI)'])
    if verbose is True:
        plt.pause(0.000000000001)
    plt.ioff()


def showtgs(tgs):
    """show targets

    tg = {'r': -1, 'a': 3.4e38, 'v': 3.4e38, 's': -1}
    """
    nfract = 2
    nTGs = len(tgs)
    for i in range(0, nTGs):
        print("===target " + str(i) + " of " + str(nTGs) + " targets.===")
        print('{r: ', round(tgs[i]['r'], nfract), ', a: ', round(tgs[i]['a'], nfract), ', v: ', round(
            tgs[i]['v'], nfract), ', s: ', round(tgs[i]['s'], nfract), '}')
