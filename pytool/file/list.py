#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import os
import shutil


def getfile(rootdir, names):
    """[summary]

    [description]

    Arguments:
        rootdir {[type]} -- [description]
        names {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    for parent, dirnames, filenames in os.walk(rootdir):
        pass
    files = []
    for file in filenames:
        (shotname, extension) = os.path.splitext(file)
        if shotname in names:
            # print(file)
            files.append(file)
    return files


def listxfile(rootdir, ext=None):
    """list file of ext

    [description]

    Arguments:
        rootdir {[type]} -- [description]

    Keyword Arguments:
        ext {[type]} -- [description] (default: {None})
    """

    pass




