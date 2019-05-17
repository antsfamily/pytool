# Copyright (c) 2016-2018, Zhi Liu.  All rights reserved.
from __future__ import absolute_import

# from .version import __version__

# __all__ = ['__version__']

#from . import file
from .file.copy import copyfile, copyfiles
from .file.lookfile import getfile, listxfile
from .file.binfile import loadbin
from .file.pickle import unpickle



#from . import box
from .box.draw import drawbox

#from . import math
from .math.rand import randperm

from .math.geometry.generate import circle1, circle2, ellipse, ellipse_surface

from .math.matrix.eigen import gerschgorin


from .math.transform import normalize

#from . import signal

from .signal import signal
from .signal.signal.correlation import corrmtx

from .signal import spectral
from .signal.spectral.music import music, computeeig, music_options, determine_signal_space
from .signal.spectral.pmusic import pmusic, pseudospectrum, computespectrumrange


from .radar.parse import adcdata
from .radar.protocol import findfrm, unpack, parsing
from .radar.show import showiq, showtgecho, showmti, showana, showmtd, showtgs
from .radar.display import radar_display, display_mtd

from .comm.udp import udpbuild, udprecv, udpclose
from .comm.tcp import tcpsbuild, tcpcbuild, tcplink, tcprecv, tcpclose
from .comm.seri import serialopen, serialread, serialwrite, serialclose


#from . import datasets
from .datasets.mnist import read_mnist
from .datasets.cifar import read_cifar100, read_cifar10
from .datasets.batch import get_batches, DataBatch

#from . import nn
from .nn.activations import linear, sigmoid, tanh, softplus, softsign, elu, relu, relu6, selu, crelu, leaky_relu

from .show.plot import aplot, mesh
from .show.vectors import plot_vectors2d
from .show.geometry import plot_circles
