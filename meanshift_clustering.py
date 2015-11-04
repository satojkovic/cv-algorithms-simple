#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.cluster import estimate_bandwidth
import cv2
import numpy as np
from meanshift import mean_shift_clustering
import matplotlib.pyplot as plt


def main():
    # load a sample image
    img = cv2.imread('toy_in.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, ch = img.shape

    # estimate bandwidth
    flat_img = np.reshape(img, [-1, 3])
    bandwidth = estimate_bandwidth(flat_img, n_samples=500)

    # mean shift clustering
    cluster_centers, points_labels = mean_shift_clustering(flat_img,
                                                           bandwidth)
    plt.imshow(np.reshape(points_labels, [h, w]))
    plt.show()


if __name__ == '__main__':
    main()
