#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import sys


def unpickle(file):
    keys = []
    if sys.version_info < (3, 1):
        import cPickle
        with open(file, 'rb') as fo:
            dictobj = cPickle.load(fo)
        for k in dictobj.keys():
            keys.append(k)
        return dictobj, keys
    else:
        import pickle
        with open(file, 'rb') as fo:
            dictobj = pickle.load(fo, encoding='bytes')
        for k in dictobj.keys():
            keys.append(k)
    return dictobj, keys
