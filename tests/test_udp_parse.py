#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import pytool

hostAddr = '192.168.31.104'
# hostAddr = None
port = 8087
udps = pytool.udpbuild(hostAddr, port)

SOF = b'$$'
EOF = b'####'

while True:
    data, addr = pytool.udprecv(udps=udps, recvsize=10240)
    # print('Received from %s:%s.' % addr)
    print('Received %s.' % data)
    
    # data = data.decode("utf-8")

    # udps.sendto(b'hello, %s!' % data, addr)

udpclose(udps)
