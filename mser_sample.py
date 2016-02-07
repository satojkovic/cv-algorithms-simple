#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

def main():
    img = cv2.imread('toy_in.png')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ms = cv2.MSER()
    msers = ms.detect(gray_img)
    for i in range(len(msers)):
        color = (np.random.randint(0, 256),
                 np.random.randint(0, 256),
                 np.random.randint(0, 256))
        cv2.drawContours(img, msers, i, color)
    cv2.imshow('TEST', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
