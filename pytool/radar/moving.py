from __future__ import absolute_import
from ..dsp.filter import fir
import numpy as np


def slide_mti(S, X, x):
    X[S['State'], :] = x

    if S['State'] == S['nTaps'] - 1:
        S['State'] = 0
    else:
        S['State'] = S['State'] + 1

    S1 = S['Coefs'][S['nTaps'] - S['State']:S['nTaps']]
    S2 = S['Coefs'][0:S['nTaps'] - S['State']]

    X1 = X[0:S['State'], :]
    X2 = X[S['State']:S['nTaps'], :]

    y1 = fir(S1, X1)
    y2 = fir(S2, X2)
    y = y1 + y2

    return y


def mti_init(Coefs, nTaps):

    S = dict()
    S['State'] = 0
    S['Coefs'] = np.array(Coefs)
    S['nTaps'] = nTaps

    return S


def accumulation(Y, y, k, nAvg):

    K, N = Y.shape

    Y[k, :] = np.abs(y)

    idxE1 = k
    idxE2 = K
    if k - nAvg >= 0:
        idxS1 = k - nAvg
        idxS2 = K
    else:
        idxS1 = 0
        idxS2 = K - (nAvg - k)

    Y1 = Y[idxS1:idxE1, :]
    Y2 = Y[idxS2:idxE2, :]
    YY = np.vstack((Y1, Y2))

    k = k + 1

    if k == K:
        k = 0

    return np.mean(YY, 0), k
