#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link	: http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import socket
import threading
import time


def tcpsbuild(hostAddr=None, port=None, nConnections=None):
    r"""TCP sever

    [description]

    Keyword Arguments:
            hostAddr {[type]} -- [description] (default: {None})
            port {[type]} -- [description] (default: {None})
            nConnections {[type]} -- [description] (default: {None})

    Returns:
            [type] -- [description]
    """
    if hostAddr is None:
        print("Use default host address: 127.0.0.1")
        hostAddr = '127.0.0.1'
    if port is None:
        port = 999
        print("Use default port: 999")
    if nConnections is None:
        nConnections = 3
        print("Use default Max connection number: " + str(nConnections))

    # build IPv4, UDP socket
    tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    tcps.bind((hostAddr, port))
    tcps.listen(nConnections)
    print('Bind TCP sever on port ', port)
    print('Waiting for connection, listening... ')

    return tcps


def tcpcbuild(hostAddr=None, port=None):
    """[TCP client]

    [description]

    Keyword Arguments:
            hostAddr {[type]} -- [description] (default: {None})
            port {[type]} -- [description] (default: {None})
            nConnections {[type]} -- [description] (default: {None})

    Returns:
            [type] -- [description]
    """

    if hostAddr is None:
        print("Use default host address: 127.0.0.1")
        hostAddr = '127.0.0.1'
    if port is None:
        port = 999
        print("Use default port: 999")
    if nConnections is None:
        nConnections = 3
        print("Use default Max connection number: " + str(nConnections))

    # build IPv4, UDP socket
    tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    tcps.connect((hostAddr, port))
    print('Bind TCP sever on port ', port)

    return tcps


def tcplink(sock=None, addr=None, recvsize=None):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        data = sock.recv(recvsize)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print('Connection from %s:%s closed.' % addr)


def tcprecv(tcps=None, recvsize=None):
    if tcps is None:
        tcps = tcpsbuild(hostAddr=None, port=None)
    if recvsize is None:
        recvsize = 1024
    print("recvsize: ", recvsize)
    # accept new connection
    sock, addr = tcps.accept()
    data = sock.recv(recvsize)
    print("----------------------")
    # create new thread for connection
    # t = threading.Thread(target=tcplink, args=(sock, addr, recvsize))
    # t.start()
    # data = t.join()
    return data, sock, addr


def tcpclose(tcps=None):
    tcps.close()


if __name__ == '__main__':

    hostAddr = '192.168.31.104'
    # hostAddr = None
    port = 8087
    s = udpbuild(hostAddr, port)

    while True:
        data, addr = udprecv(tcps=s, recvsize=10240)
        # print('Received from %s:%s.' % addr)
        print('Received %s.' % data)
        # s.sendto(b'hello, %s!' % data, addr)
