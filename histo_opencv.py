#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    histo.py <image_file>
    histo.py -h | --help
Options:
    -h --help    show help message
"""
import cv2
from docopt import docopt
import os
import sys
import numpy as np
import itertools


def calc_histogram(img, n_bins):
    h, w, n_channels = img.shape
    hist = np.zeros((n_channels, n_bins), dtype=np.int)
    for j, i, c in itertools.product(range(h), range(w), range(n_channels)):
        val = img[j, i, c]
        hist[c][val] += 1

    # get the peak value for each channel
    hmax = [max(hist[i]) for i in range(n_channels)]

    return hist, hmax


def show_historam(img, n_bins):
    hist, hmax = calc_histogram(img, n_bins)

    # setup the canvas and dislay the histograms
    n_channels = len(hist)
    rows = img.shape[0] / 2
    canvas = [np.ones((rows, n_bins, n_channels), dtype=np.uint8)
              for i in range(n_channels)]
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    wname = ["blue", "green", "red"]
    for i in range(n_channels):
        for j in range(n_bins):
            cv2.line(canvas[i],
                     (j, rows),
                     (j, rows - np.int((hist[i][j] * rows/np.float(hmax[i])))),
                     colors[i],
                     1, 8, 0)
        cv2.imshow(wname[i], canvas[i])
    cv2.waitKey(0)


def main():
    args = docopt(__doc__)
    image_file = args['<image_file>']
    if not os.path.exists(image_file):
        print 'Not found:', image_file
        sys.exit(-1)

    # load image
    img = cv2.imread(image_file)

    # show histogram
    show_historam(img, 256)


if __name__ == '__main__':
    main()
