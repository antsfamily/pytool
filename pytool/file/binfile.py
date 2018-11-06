#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  :2018-11-01 12:54:00
# @Author  :Zhi Liu(zhiliu.mind@gmail.com)
# @Link  :http://iridescent.ink
# @Verson :$1.0$

import numpy as np
import struct
import time
import binascii


def loadbin(filename=None, dtype='i', dbsize=4, endian='Little', offsets=0, verbose=False):
    """[load binary file]

    [load binary file]

    Keyword Arguments:
            filename {str} -- [description] (default: {None})
            dtype {str} -- [c:char, b:schar, B:uchar, h:short, H:ushort, 
                                            i:int, I:uint, l:long, L:ulong, q:longlong],
                                            Q:ulonglong, f:float, d:double, s:char[], 
                                            p:char[], P:void* (default: {'i'})
            dbsize {number} -- [bits of per number] (default: {4})
            offsets {number} -- [offsets index] (default: {0})
    """
    if filename is None:
        ValueError(" Not a valid file!")
    nums = []
    if endian is 'Little':
        dtype = '<' + dtype
        # dtype = '@' + dtype
    if endian is 'Big':
        dtype = '>' + dtype
        # dtype = '!' + dtype
    f = open(filename, 'rb')
    try:
        while True:
            data = f.read(dbsize)
            # print(data)
            # value = struct.unpack(dtype, data)[0]
            # print(dtype)
            value = struct.unpack(dtype, data)[0]
            nums.append(value)
            if verbose is True:
	            print(data)
	            print(value)
    except:
        print("End of file!")		
    f.close()
    return nums[offsets:len(nums)]


if __name__ == '__main__':
    pass
