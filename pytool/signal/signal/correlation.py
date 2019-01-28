#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 17:35:36
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$


def corrmtx():

    pass


def xcorr(x, y, scalemod=None):
    """Cross-correlation function estimates.

    XCORR produces an estimate of the correlation between two random
    (jointly stationary) sequences:

    .. math::
         C
           C(m) = E[A(n+m)*conj(B(n))] = E[A(n)*conj(B(n-m))]
    It is also the deterministic correlation between two deterministic
    signals.

    Arguments:
       x {[type]} -- [description]
       y {[type]} -- [description]

    Keyword Arguments:
       scalemod {[type]} -- [description] (default: {None})
    """
