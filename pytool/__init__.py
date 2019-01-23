# Copyright (c) 2016-2018, Zhi Liu.  All rights reserved.
from __future__ import absolute_import

# from .version import __version__

# __all__ = ['__version__']

from . import file
from .file.copy import copyfile, copyfiles
from .file.list import getfile, listxfile
from .file.binfile import loadbin

from . import box
from .box.draw import drawbox

from . import math
from .math.rand import randperm

from .math.geometry.generate import circle1, circle2, ellipse, ellipse_surface

from .math.matrix.eigen import gerschgorin



from .radar.parse import adcdata
from .radar.protocol import findfrm, unpack, parsing
from .radar.show import showiq, showtgecho, showmti, showana, showmtd, showtgs
from .radar.display import radar_display, display_mtd

from .comm.udp import udpbuild, udprecv, udpclose
from .comm.tcp import tcpsbuild, tcpcbuild, tcplink, tcprecv, tcpclose
from .comm.seri import serialopen, serialread, serialwrite, serialclose


from . import datasets
from .datasets.mnist import read_mnist
from .datasets.batches import get_batches

from . import nn
from .nn.activations import linear, sigmoid, tanh, softplus, softsign, elu, relu, relu6, selu, crelu, leaky_relu

from .show.plot import aplot, mesh
from .show.vectors import plot_vectors2d
from .show.geometry import plot_circles


