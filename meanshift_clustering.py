#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.cluster import estimate_bandwidth
import cv2
import numpy as np


def main():
    # load a sample image
    img = cv2.imread('toy_in.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # estimate bandwidth
    flat_img = np.reshape(img, [-1, 3])
    bandwidth = estimate_bandwidth(flat_img, n_samples=500)


if __name__ == '__main__':
    main()
