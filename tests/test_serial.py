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
while True:
    data = pytool.serialread(serial, size=None, timesleep=timesleep)
    print(len(data))
pytool.serialclose(serial)
