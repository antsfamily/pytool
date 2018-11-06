#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  :2018-11-01 12:54:00
# @Author  :Zhi Liu(zhiliu.mind@gmail.com)
# @Link  :http://iridescent.ink
# @Verson :$1.0$

import numpy as np
import struct
# from pytool.binfile import loadbin
# from pytool.parse import parsedata
import pytool
from matplotlib import pyplot as plt


dbsize = 2
offsets = 60

dtype = 'h'
endian = 'Little'
filename = '../data/data.bin'
# filename = './data/data_REGV2.bin'

mod = 'QIQI'

A = pytool.loadbin(filename=filename, dtype=dtype, dbsize=dbsize, endian=endian, offsets=offsets, verbose=True)

I1, Q1, I2, Q2 = pytool.parsedata(A, mod)
# print(I1)
# print(Q1)

plt.figure()
plt.plot(I1, '-xr')
plt.plot(I2, '-+m')
plt.plot(Q1, '-xb')
plt.plot(Q2, '-+g')
plt.legend(['I1', 'I2', 'Q1', 'Q2'], loc = 0, ncol = 2)
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.show()
