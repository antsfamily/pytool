#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  :2018-11-01 12:54:00
# @Author  :Zhi Liu(zhiliu.mind@gmail.com)
# @Link  :http://iridescent.ink
# @Verson :$1.0$

import numpy as np
import pytool
from pytool.radar.protocol import UpDataType

SOF = b'$$'
EOF = b'####'
# SOF = '$$'
# EOF = '####'
endian = 'Little'
dtype = type(SOF)


global cnt
global FIR_LEN_MTI
global mtd
cnt = 0
FIR_LEN_MTI = 65
mtd = np.zeros((FIR_LEN_MTI, 256))

def radar_display(data, dtype=None, SOF=None, EOF=None):
    if dtype is None:
        dtype = 'bytes'
    if dtype is 'bytes':
        if SOF is None:
            SOF = b'$$'
        if EOF is None:
            EOF = b'####'

    if dtype is 'str':
        # data = data.decode("utf-8") ## byte like --> string
        if SOF is None:
            SOF = '$$'
        if EOF is None:
            EOF = '####'

    s, idxHead, idxTail = pytool.findfrm(
        data, dtype=dtype, SOF=SOF, EOF=EOF)

    print(type(data), s, idxHead, idxTail)
    data = data[idxHead:idxTail + len(EOF)]
    # print(type(data), len(data), idxHead, idxTail)

    Frame = pytool.unpack(
        data=data, dtype=dtype, endian='Little', SOF=SOF, EOF=EOF)

    if Frame is None:
        return

    if Frame['DATATYPE'] is UpDataType['UPDT_TGINFO']:
        targets, nTGs = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        pytool.showtgs(targets)
    if Frame['DATATYPE'] is UpDataType['UPDT_ORIGECHO']:
        IQV, adcmod = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        pytool.showiq(IQV, adcmod)
    if Frame['DATATYPE'] is UpDataType['UPDT_TGECHO']:
        tgecho1, tgecho2 = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        pytool.showtgecho(tgecho1, tgecho2)
    if Frame['DATATYPE'] is UpDataType['UPDT_ANALYSIS']:
        mti, cfarth = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        pytool.showana(mti, cfarth)


def display_mtd(data, dtype=None, SOF=None, EOF=None):
    global cnt
    global FIR_LEN_MTI
    global mtd
    if dtype is None:
        dtype = 'bytes'
    if dtype is 'bytes':
        if SOF is None:
            SOF = b'$$'
        if EOF is None:
            EOF = b'####'

    if dtype is 'str':
        # data = data.decode("utf-8") ## byte like --> string
        if SOF is None:
            SOF = '$$'
        if EOF is None:
            EOF = '####'

    s, idxHead, idxTail = pytool.findfrm(
        data, dtype=dtype, SOF=SOF, EOF=EOF)

    print(type(data), s, idxHead, idxTail)
    data = data[idxHead:idxTail + len(EOF)]
    # print(type(data), len(data), idxHead, idxTail)

    Frame = pytool.unpack(
        data=data, dtype=dtype, endian='Little', SOF=SOF, EOF=EOF)

    if Frame is None:
        return
    if Frame['DATATYPE'] is UpDataType['UPDT_ORIGECHO']:
        IQV, adcmod = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        if IQV is None:
            print("IIIIIIIIIIIIIi")
            return
        IQV = np.array(IQV)
        # x1 = IQV[0] + 1j * IQV[1]
        x1 = IQV[0]
        # y1 = np.fft.fft(x1)
        # x2 = IQV[3] + 1j * IQV[4]
        x2 = IQV[3]
        # y2 = np.fft.fft(x2)
        print(cnt)
        # mtd[cnt, :] = x1
        mtd[cnt, :] = x2
        if cnt < FIR_LEN_MTI-1:
            cnt = cnt + 1
        else:
            cnt = 0
            mtd = np.abs(np.fft.fft2(mtd))
            mtd[0, 0] = 0
            print(mtd)
            pytool.showmtd(mtd, verbose=True)
