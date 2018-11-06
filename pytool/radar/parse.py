#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  :2018-11-01 12:54:00
# @Author  :Zhi Liu(zhiliu.mind@gmail.com)
# @Link  :http://iridescent.ink
# @Verson :$1.0$

import numpy as np
import struct
import time
import binascii


def adcdata(data=None, mod='IQ', verbose=False):
    """[parse adc data]

    [parse adc data]
    
    Keyword Arguments:
        data {[list]} -- [description] (default: {None})
        mod {str} -- [description] (default: {'IQ'})
        verbose {bool} -- [description] (default: {False})
    
    Returns:
        [type] -- [description]
    """

    if data is None:
        ValueError(" Not a valid data list!")
    I1 = []
    I2 = []
    Q1 = []
    Q2 = []
    V1 = []
    V2 = []
    cnt = 0
    if mod is 'IQ':
        for x in data:
            if cnt is 0:
                I1.append(x)
            else:
                Q1.append(x)
            cnt = 1 - cnt 
        return I1, Q1
        print("===========IQ============")
    if mod is 'QI':
        for x in data:
            if cnt is 0:
                I1.append(x)
            else:
                Q1.append(x)
            cnt = 1 - cnt
        print("===========QI============")
        return I1, Q1
    if mod is 'IQIQ':
        for x in data:
            if cnt%4 is 0:
                I1.append(x)
            elif cnt%4 is 1:
                Q1.append(x)
            elif cnt%4 is 2:
                I2.append(x)
            elif cnt%4 is 3:
                Q2.append(x)
            cnt = cnt + 1
        print("===========IQIQ============")
        return I1, Q1, I2, Q2
    if mod is 'QIQI':
        for x in data:
            if cnt%4 is 0:
                Q2.append(x)
            elif cnt%4 is 1:
                I2.append(x)
            elif cnt%4 is 2:
                Q1.append(x)
            elif cnt%4 is 3:
                I1.append(x)
            cnt = cnt + 1
        print("===========QIQI============")
        return I1, Q1, I2, Q2
    if mod is 'IQVIQV':
        for x in data:
            if cnt%6 is 0:
                I1.append(x)
            elif cnt%6 is 1:
                Q1.append(x)
            elif cnt%6 is 2:
                V1.append(x)
            elif cnt%6 is 3:
                I2.append(x)
            elif cnt%6 is 4:
                Q2.append(x)
            elif cnt%6 is 5:
                V2.append(x)
            cnt = cnt + 1
        print("===========I1 Q1 V1 I2 Q2 V2============")
        return I1, Q1, V1, I2, Q2, V2
    if mod is 'QIVQIV':
        for x in data:
            if cnt%6 is 0:
                Q1.append(x)
            elif cnt%6 is 1:
                I1.append(x)
            elif cnt%6 is 2:
                V1.append(x)
            elif cnt%6 is 3:
                Q2.append(x)
            elif cnt%6 is 4:
                I2.append(x)
            elif cnt%6 is 5:
                V2.append(x)
            cnt = cnt + 1
        print("===========Q1 I1 V1 Q2 I2 V2============")
        return I1, Q1, V1, I2, Q2, V2


if __name__ == '__main__':
    pass

