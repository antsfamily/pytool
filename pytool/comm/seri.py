#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 2018-11-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link : http://iridescent.ink
# @Version : $1.0$


import serial
from time import sleep


def serialopen(com=None, baudrate=None, timeout=None):
    import serial
    if com is None:
        com = 'COM1'
    if baudrate is None:
        baudrate = 9600
    if timeout is None:
        timeout = 0.0000005
    serial = serial.Serial(com, baudrate, timeout=timeout)  # /dev/ttyUSB0
    if serial.isOpen():
        print("open " + com + " success!")
    else:
        print("open " + com + " failed!")
    return serial


def serialread(serial, size=None, timesleep=None):

    if size is None:
        data = serial.read_all()
    else:
        data = serial.read(size)
    if timesleep is not None:
        sleep(timesleep)
    return data


def serialwrite(serial, data):
    while True:
        flag = serial.write(data)
        # sleep(0.0002)
    return flag


def serialclose(serial):
    serial.close()

if __name__ == '__main__':

    com = 'COM7'
    baudrate = 115200
    timeout = 0.05
    timesleep = 0.005

    serial = serialopen(com=com, baudrate=baudrate, timeout=timeout)
    while True:
        data = serialread(serial, size=1024, timesleep=timesleep)
        if data != b'':
            print("receive : ", data)
            # serialwrite(serial, data)  # 数据写回
    print("Over!")
