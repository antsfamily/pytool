#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link	: http://blog.csdn.net/enjoyyl
# @Version : $1.0$
import time
import pytool
from pytool.radar.protocol import UpDataType


hostAddr = '192.168.31.104'
# hostAddr = '192.168.1.15'
# hostAddr = None
port = 8087
# port = 50001
udps = pytool.udpbuild(hostAddr, port)

SOF = b'$$'
EOF = b'####'
# SOF = '$$'
# EOF = '####'
endian='Little'
dtype = type(SOF)


# plt.ion()
# fig = plt.figure(0)
while True:
	data, addr = pytool.udprecv(udps=udps, recvsize=20480)
	# print('Received from %s:%s.' % addr)
	# print('Received %s.' % data)
	if dtype is 'str':
		data = data.decode("utf-8")
	# print(data)
	s, idxHead, idxTail = pytool.findfrm(data, dtype=dtype, SOF=SOF, EOF=EOF)

	# print(type(data), s, idxHead, idxTail)
	data = data[idxHead:idxTail+len(EOF)]

	Frame = pytool.unpack(data=data, dtype=dtype, endian='Little', SOF=SOF, EOF=EOF)

	if Frame['DATATYPE'] is UpDataType['UPDT_TGINFO']:
		targets, nTGs = pytool.parsing(Frame=Frame, endian=endian, SOF=None, EOF=None)
		pytool.showtgs(targets)
	if Frame['DATATYPE'] is UpDataType['UPDT_ORIGECHO']:
		IQV, adcmod = pytool.parsing(Frame=Frame, endian=endian, SOF=None, EOF=None)
		pytool.showiq(IQV, adcmod)
	if Frame['DATATYPE'] is UpDataType['UPDT_ANALYSIS']:
		mti, cfarth = pytool.parsing(Frame=Frame, endian=endian, SOF=None, EOF=None)
		pytool.showana(mti, cfarth)
udpclose(udps)
