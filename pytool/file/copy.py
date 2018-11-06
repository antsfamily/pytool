#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import os
import shutil


def copyfiles(srcdir, dstdir, filenames):
    """copy files from srcdir to dstdir

    copy filenames specified files from srcdir to dstdir.

    Arguments:
        srcdir {path str} -- [source path]
        dstdir {path str} -- [destnation path]
        filenames {list} -- [filenames to be copied]
    """
    for filename in filenames:
        srcfile = os.path.join(srcdir, filename)
        dstfile = os.path.join(dstdir, filename)
        # print(srcfile, dstfile)
        shutil.copyfile(srcfile, dstfile)


def copyfile(srcfile, dstfile):
    """copy file from srcfile to dstfile

    copy file from srcfile to dstfile.

    Arguments:
        srcfile {path str} -- [source file]
        dstfile {path str} -- [destination file]
    """
    shutil.copyfile(srcfile, dstfile)

if __name__ == '__main__':
    pass

