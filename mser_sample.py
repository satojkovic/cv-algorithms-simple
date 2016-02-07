#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2


def main():
    img = cv2.imread('checker_board.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ms = cv2.MSER()
    msers = ms.detect(gray_img)
    for i in range(len(msers)):
        color = (np.random.randint(0, 256),
                 np.random.randint(0, 256),
                 np.random.randint(0, 256))
        for j in range(len(msers[i])):
            pos = (msers[i][j][0], msers[i][j][1])
            cv2.circle(img, pos, 1, color)
    cv2.imshow('TEST', img)
    cv2.waitKey(0)

    cv2.imwrite('checker_board_gray_result.jpg', img)


if __name__ == '__main__':
    main()
