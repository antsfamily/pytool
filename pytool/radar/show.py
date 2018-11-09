#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	  : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link	  : http://blog.csdn.net/enjoyyl
# @Version   : $1.0$

from matplotlib import pyplot as plt


def showiq(IQV, adcmod=None):
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
    plt.pause(0.0000001)
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
