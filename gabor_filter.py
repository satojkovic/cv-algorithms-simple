#-*- coding: utf-8 -*-
import argparse
import os
import sys
import cv2


def main():
    parser = argparse.ArgumentParser(
        description='Gabor filter sample script',
    )

    parser.add_argument(
        help='image file',
        dest='img_file',
    )

    args = parser.parse_args()

    if not os.path.isfile(args.img_file):
        print 'Not found: %s' % args.img_file
        sys.exit()

    img = cv2.imread(args.img_file)
    cv2.imshow('Original', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
