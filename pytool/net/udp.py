#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import socket


def udpbuild(hostAddr=None, port=None):

	if hostAddr is None:
		print("Use default host address: 127.0.0.1")
		hostAddr = '127.0.0.1'
	if port is None:
		port = 999
		print("Use default port: 999")

	# build IPv4, UDP socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# bind port
	s.bind((hostAddr, port))
	print('Bind UDP on port ', port)

	return s


def udprecv(udps=None, recvsize=None):
	if udps is None:
		udps = udpbuild(hostAddr=None, port=None)
	if recvsize is None:
		recvsize = 1024
	data, addr = udps.recvfrom(recvsize)
	return data, addr

def udpclose(udps=None):
	udps.close()


if __name__ == '__main__':

	hostAddr = '192.168.31.104'
	# hostAddr = None
	port = 8087
	s = udpbuild(hostAddr, port)

	while True:
	    data, addr = udprecv(udps=s, recvsize=10240)
	    # print('Received from %s:%s.' % addr)
	    print('Received %s.' % data)
	    # s.sendto(b'hello, %s!' % data, addr)
