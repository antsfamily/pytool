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
# hostAddr = '192.168.1.15'
# hostAddr = None
port = 8087
# port = 50001
tcps = pytool.tcpsbuild(hostAddr, port)

SOF = b'$$'
EOF = b'####'
# SOF = '$$'
# EOF = '####'
endian='Little'
dtype = type(SOF)


plt.ion()
fig = plt.figure(0)
while True:
	data, addr, _ = pytool.tcprecv(tcps=tcps, recvsize=20480)
	if dtype is 'str':
		data = data.decode("utf-8")
	s, idxHead, idxTail = pytool.findfrm(data, dtype=dtype, SOF=SOF, EOF=EOF)

	print(type(data), s, idxHead, idxTail)
	if s < 0:
		print(data)
		continue;
	data = data[idxHead:idxTail+len(EOF)]
	print("========")
	Frame = pytool.unpack(data=data, dtype=dtype, endian='Little', SOF=SOF, EOF=EOF)
	IQV, adcmod = pytool.parsing(Frame=Frame, endian=endian, SOF=None, EOF=None)

	# print(adcmod)
	# plt.clf()
	# if adcmod is 0x03:
	# 	plt.plot(IQV[0], '-r')
	# 	plt.plot(IQV[1], '-b')
	# 	plt.plot(IQV[2], '.-r')
	# 	plt.plot(IQV[3], '.-b')
	# 	plt.grid()
	# 	plt.title("echoes of radar")
	# 	plt.legend(['I1', 'Q1', 'I2', 'Q2'])
	# if adcmod is 0x13:
	# 	plt.plot(IQV[0], '-r')
	# 	plt.plot(IQV[1], '-b')
	# 	plt.plot(IQV[2], '-g')
	# 	plt.plot(IQV[3], '.-r')
	# 	plt.plot(IQV[4], '.-b')
	# 	plt.plot(IQV[5], '.-g')
	# 	plt.title("echoes of radar")
	# 	plt.legend(['I1', 'Q1', 'VGA1', 'I2', 'Q2', 'VGA2'])
	# plt.pause(0.0000001)
	# plt.ioff()

print("===============")
pytool.tcpclose(tcps)
