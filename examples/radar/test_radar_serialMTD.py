#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import numpy as np
import pytool
from pytool.radar.protocol import UpDataType

com = 'COM7'
baudrate = 1050000
timeout = 0.001
timesleep = 0.0001


SOF = b'$$'
EOF = b'####'
# SOF = '$$'
# EOF = '####'
endian = 'Little'
dtype = type(SOF)


# plt.ion()
# fig = plt.figure(0)
serial = pytool.serialopen(com=com, baudrate=baudrate, timeout=timeout)

cnt = 0
FIR_LEN_MTI = 65

mtd = np.zeros((FIR_LEN_MTI, 256))

while True:
    data = pytool.serialread(serial, size=None, timesleep=timesleep)
    if dtype is 'str':
        data = data.decode("utf-8")
    # print(data)
    s, idxHead, idxTail = pytool.findfrm(
        data, dtype=dtype, SOF=SOF, EOF=EOF)

    # print(type(data), s, idxHead, idxTail)
    data = data[idxHead:idxTail + len(EOF)]
    # print(type(data), len(data), idxHead, idxTail)

    Frame = pytool.unpack(
        data=data, dtype=dtype, endian='Little', SOF=SOF, EOF=EOF, verbose=True)

    if Frame is None:
        continue

    if Frame['DATATYPE'] is UpDataType['UPDT_ORIGECHO']:
        IQV, adcmod = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        if IQV is None:
            print("IIIIIIIIIIIIIi")
            continue
        IQV = np.array(IQV)
        x1 = IQV[0] + 1j * IQV[1]
        y1 = np.fft.fft(x1)
        x2 = IQV[3] + 1j * IQV[4]
        y2 = np.fft.fft(x2)
        print(cnt)
        mtd[cnt, :] = x1
        if cnt < FIR_LEN_MTI-1:
            cnt = cnt + 1
        else:
            cnt = 0
            # mtd = np.abs(np.fft.fft2(mtd))
            pytool.showmtd(mtd, verbose=True)


pytool.serialclose(serial)
