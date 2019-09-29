#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link	: http://blog.csdn.net/enjoyyl
# @Version : $1.0$
import time
import pytool
from pytool.radar.protocol import UpDataType
import pytool as pt
import numpy as np
from numpy.fft import fft, fftshift
from matplotlib import pyplot as plt


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


# N = 1024
N = 400

Coefs = [
	0.000029, 0.000014, 0.000015, 0.000014, 0.000011, 0.000006, -0.000002, -0.000012, -0.000023, -0.000035, -0.000047, -0.000056, -0.000062, -0.000062, -0.000057, -0.000045,
	# 0.0000, 0.000, 0.000, 0.000, 0.000, 0.0000, -0.000, -0.000012, -0.000023, -0.000035, -0.000047, -0.000056, -0.000062, -0.000062, -0.000057, -0.000045,
	-0.000026, 0.000000, 0.000031, 0.000064, 0.000098, 0.000128, 0.000151, 0.000164, 0.000164, 0.000148, 0.000115, 0.000067, 0.000004, -0.000069, -0.000147, -0.000223,
	-0.000290, -0.000340, -0.000367, -0.000364, -0.000328, -0.000258, -0.000154, -0.000023, 0.000128, 0.000286, 0.000439, 0.000573, 0.000672, 0.000724, 0.000718, 0.000648,
	0.000513, 0.000316, 0.000070, -0.000211, -0.000505, -0.000787, -0.001032, -0.001213, -0.001309, -0.001301, -0.001179, -0.000943, -0.000600, -0.000171, 0.000317, 0.000826,
	0.001314, 0.001738, 0.002054, 0.002224, 0.002219, 0.002024, 0.001638, 0.001074, 0.000366, -0.000439, -0.001281, -0.002091, -0.002798, -0.003330, -0.003627, -0.003642,
	-0.003349, -0.002745, -0.001853, -0.000724, 0.000568, 0.001927, 0.003245, 0.004405, 0.005297, 0.005820, 0.005896, 0.005480, 0.004561, 0.003170, 0.001383, -0.000690,
	-0.002899, -0.005073, -0.007027, -0.008575, -0.009548, -0.009809, -0.009262, -0.007869, -0.005655, -0.002715, 0.000790, 0.004637, 0.008549, 0.012216, 0.015308, 0.017498,
	0.018485, 0.018015, 0.015900, 0.012038, 0.006421, -0.000857, -0.009597, -0.019508, -0.030215, -0.041279, -0.052219, -0.062542, -0.071766, -0.079453, -0.085230, -0.088814,
	0.909971, -0.088814, -0.085230, -0.079453, -0.071766, -0.062542, -0.052219, -0.041279, -0.030215, -0.019508, -0.009597, -0.000857, 0.006421, 0.012038, 0.015900, 0.018015,
	0.018485, 0.017498, 0.015308, 0.012216, 0.008549, 0.004637, 0.000790, -0.002715, -0.005655, -0.007869, -0.009262, -0.009809, -0.009548, -0.008575, -0.007027, -0.005073,
	-0.002899, -0.000690, 0.001383, 0.003170, 0.004561, 0.005480, 0.005896, 0.005820, 0.005297, 0.004405, 0.003245, 0.001927, 0.000568, -0.000724, -0.001853, -0.002745,
	-0.003349, -0.003642, -0.003627, -0.003330, -0.002798, -0.002091, -0.001281, -0.000439, 0.000366, 0.001074, 0.001638, 0.002024, 0.002219, 0.002224, 0.002054, 0.001738,
	0.001314, 0.000826, 0.000317, -0.000171, -0.000600, -0.000943, -0.001179, -0.001301, -0.001309, -0.001213, -0.001032, -0.000787, -0.000505, -0.000211, 0.000070, 0.000316,
	0.000513, 0.000648, 0.000718, 0.000724, 0.000672, 0.000573, 0.000439, 0.000286, 0.000128, -0.000023, -0.000154, -0.000258, -0.000328, -0.000364, -0.000367, -0.000340,
	-0.000290, -0.000223, -0.000147, -0.000069, 0.000004, 0.000067, 0.000115, 0.000148, 0.000164, 0.000164, 0.000151, 0.000128, 0.000098, 0.000064, 0.000031, 0.000000,
	-0.000026, -0.000045, -0.000057, -0.000062, -0.000062, -0.000056, -0.000047, -0.000035, -0.000023, -0.000012, -0.000002, 0.000006, 0.000011, 0.000014, 0.000015, 0.000014,
	0.000029,
]

# Coefs = [-1., 2., -1.]

M = len(Coefs)
nTaps = M
K = M
R = round(0.4 * K)

ptime = 1e-16

S = pt.mti_init(Coefs, nTaps)
X1 = np.zeros((M, N), dtype='complex64')
Y = np.zeros((K, N))

print(X1.shape)

plt.ion()
plt.figure(1)

k = 0
cnt = 0
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
		# pytool.showtgs(targets)
	if Frame['DATATYPE'] is UpDataType['UPDT_ORIGECHO']:
		IQV, adcmod = pytool.parsing(Frame=Frame, endian=endian, SOF=None, EOF=None)
		print(len(IQV[0]))
		pytool.showiq(IQV, adcmod)
	if Frame['DATATYPE'] is UpDataType['UPDT_ANALYSIS']:
		mti, cfarth = pytool.parsing(Frame=Frame, endian=endian, SOF=None, EOF=None)
		pytool.showana(mti, cfarth)
	if Frame['DATATYPE'] is UpDataType['UPDT_TGECHO']:
		x1, x2 = pytool.parsing(Frame=Frame, endian=endian, SOF=None, EOF=None)
		x = x1[:N]
		y = pytool.slide_mti(S, X1, x)
		y = np.abs(y)
		yy, k = pytool.accumulation(Y, y, k, R)
		
		cnt = cnt + 1
		pytool.showmti2(x, y, yy, k=cnt, ptime=ptime)
plt.ioff()

udpclose(udps)
