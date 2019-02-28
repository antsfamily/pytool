#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 20:22:27
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://blog.csdn.net/enjoyyl
# @Version : $1.0$

import cv2
import numpy as np
import matplotlib.pyplot as plt


def drawbox(img, bbox, clsl, mod='ltrb', colors=None):
    r"""draw box o image img

    draw box o image img

    Arguments:
        img {[array]} -- [image]
        bbox {[list]} -- [bonding box]
        clsl {[list]} -- [classlabel]

    Keyword Arguments:
        mod {str} -- [label mode:
            'ltrb'-->lettop rightbottom
            'ltwh'-->lettop width height
            'cwh' -->center width height
            'cwhnorm' -->center width height with norm
             (default: {'ltrb'})
        colors {[type]} -- [draw colors] (default: {None})

    Returns:
        [type] -- [description]
    """

    if colors is None:
        colors = plt.cm.hsv(np.linspace(0, 1, len(clsl))).tolist()
    imgshape = img.shape
    H = imgshape[0]
    W = imgshape[1]
    if mod is 'ltrb':
        for target in bbox:
            # print(bbox[target])
            if bbox[target] is None:
                continue
            label0 = clsl[target]
            color = colors[label0]
            # print(color)
            display_txt = '%s' % (target)
            for box in bbox[target]:
                xmin0 = int(box[0])
                ymin0 = int(box[1])
                xmax0 = int(box[2])
                ymax0 = int(box[3])

                cv2.putText(img, display_txt, (xmin0, ymax0),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

                cv2.rectangle(img, (xmin0, ymin0),
                              (xmax0, ymax0), color, 1)
    if mod is 'ltwh':
        for target in bbox:
            # print(bbox[target])
            if bbox[target] is None:
                continue
            label0 = clsl[target]
            color = colors[label0]
            # print(color)
            display_txt = '%s' % (target)
            for box in bbox[target]:
                xmin0 = int(box[0])
                ymin0 = int(box[1])
                xmax0 = min(imgshape[1], xmin0 + int(box[2]))
                ymax0 = min(imgshape[0], ymin0 + int(box[3]))

                cv2.putText(img, display_txt, (xmin0, ymax0),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

                cv2.rectangle(img, (xmin0, ymin0),
                              (xmax0, ymax0), color, 1)

    if mod is 'cwh':
        for target in bbox:
            # print(bbox[target])
            if bbox[target] is None:
                continue
            label0 = clsl[target]
            color = colors[label0]
            # print(color)
            display_txt = '%s' % (target)
            for box in bbox[target]:
                xmin0 = max(0, int(box[0]) - int(box[2]) / 2.0)
                ymin0 = max(0, int(box[1]) - int(box[3]) / 2.0)
                xmax0 = min(imgshape[1], int(box[0]) + int(box[2]) / 2.0)
                ymax0 = min(imgshape[0], int(box[1]) + int(box[3]) / 2.0)

                cv2.putText(img, display_txt, (xmin0, ymax0),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

                cv2.rectangle(img, (xmin0, ymin0),
                              (xmax0, ymax0), color, 1)

    if mod is 'cwhnorm':
        for target in bbox:
            # print(bbox[target])
            if bbox[target] is None:
                continue
            label0 = clsl[target]
            color = colors[label0]
            # print(color)
            display_txt = '%s' % (target)
            for box in bbox[target]:
                print(box, "=====++++============")
                box[0] = box[0] * W
                box[1] = box[1] * H
                box[2] = box[2] * W
                box[3] = box[3] * H

                xmin0 = max(0, box[0] - box[2] / 2.0)
                ymin0 = max(0, box[1] - box[3] / 2.0)
                xmax0 = min(W, box[0] + box[2] / 2.0)
                ymax0 = min(H, box[1] + box[3] / 2.0)
                xmin0 = int(xmin0)
                ymin0 = int(ymin0)
                xmax0 = int(xmax0)
                ymax0 = int(ymax0)
                cv2.putText(img, display_txt, (xmin0, ymax0),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

                cv2.rectangle(img, (xmin0, ymin0),
                              (xmax0, ymax0), color, 1)

    img = np.uint8(img * 255)
    return img
