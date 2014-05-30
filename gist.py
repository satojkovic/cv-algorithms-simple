#-*- coding: utf-8 -*-

import argparse
import cv2
import sys

NBLOCKS = 4
NSCALE = 3

def color_gist_scaletab(img, w, n_scale, n_orientation):
    src_width, src_height = img.shape[0], img.shape[1]

    if src_width < 8 or src_height < 8:
        print 'Error: color_gist_scaletab() - Image not big enough'
        sys.exit(-1)

    numberBlocks = w
    tot_oris = 0
    for i in xrange(n_scale):
        tot_oris += n_orientation[i]

    copy_img = img.copy()
    
def main():
    parser = argparse.ArgumentParser(
        description='compute gist descriptor',
    )

    parser.add_argument(
        help='image file name',
        dest='imgfile',
    )

    args = parser.parse_args()

    img = cv2.imread(args.imgfile)
    if img:
        print 'Could not load image: %s' % args.imgfile
        sys.exit(-1)

if __name__ == '__main__':
    main()
