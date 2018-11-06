#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link	: http://blog.csdn.net/enjoyyl
# @Version : $1.0$
import time
import pytool
from matplotlib import pyplot as plt


hostAddr = '192.168.31.104'
# hostAddr = None
port = 8087
udps = pytool.udpbuild(hostAddr, port)

SOF = b'$$'
EOF = b'####'
# SOF = '$$'
# EOF = '####'

dtype = type(SOF)


plt.ion()
fig = plt.figure(0)
while True:
	data, addr = pytool.udprecv(udps=udps, recvsize=10240)
	# print('Received from %s:%s.' % addr)
	# print('Received %s.' % data)
	if dtype is 'str':
		data = data.decode("utf-8")

	s, idxHead, idxTail = pytool.findfrm(data, dtype=dtype, SOF=SOF, EOF=EOF)

	# print(type(data), s, idxHead, idxTail)
	data = data[idxHead:idxTail+len(EOF)]
	Frame = pytool.unpack(data=data, dtype=dtype, endian='Little', SOF=SOF, EOF=EOF)
	IQV = pytool.parsing(Frame=Frame, endian='Little', SOF=None, EOF=None)

	plt.clf()
	plt.plot(IQV[0], 'r')
	plt.plot(IQV[1], 'b')
	plt.plot(IQV[2], 'g')
	plt.title("echoes of radar")
	plt.legend(['I', 'Q', 'VGA'])
	plt.pause(0.000000001)
	plt.ioff()


udpclose(udps)
