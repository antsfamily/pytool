#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import pytool
from pytool.radar.protocol import UpDataType

com = 'COM7'
baudrate = 1050000
timeout = 0.000000001
timesleep = 0.0000001


SOF = b'$$'
EOF = b'####'
# SOF = '$$'
# EOF = '####'
endian = 'Little'
dtype = type(SOF)


# plt.ion()
# fig = plt.figure(0)
serial = pytool.serialopen(com=com, baudrate=baudrate, timeout=timeout)
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
        data=data, dtype=dtype, endian='Little', SOF=SOF, EOF=EOF)

    if Frame is None:
    	continue

    if Frame['DATATYPE'] is UpDataType['UPDT_TGINFO']:
        targets, nTGs = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        pytool.showtgs(targets)
    if Frame['DATATYPE'] is UpDataType['UPDT_ORIGECHO']:
        IQV, adcmod = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        pytool.showiq(IQV, adcmod)
    if Frame['DATATYPE'] is UpDataType['UPDT_ANALYSIS']:
        mti, cfarth = pytool.parsing(
            Frame=Frame, endian=endian, SOF=None, EOF=None)
        pytool.showana(mti, cfarth)
pytool.serialclose(serial)
