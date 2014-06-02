#-*- coding: utf-8 -*-

import argparse
import cv2
import sys


def color_gist_scaletab(img, w, n_scale, n_orientation):
    desc = [0 for i in xrange(960)]
    return desc
    
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
    if img == None:
        print 'Could not load image: %s' % args.imgfile
        sys.exit(-1)

    nblocks = 4
    n_scale = 3
    orientations_per_scale = [0 for i in xrange(50)]
    orientations_per_scale[0] = 8
    orientations_per_scale[0] = 8
    orientations_per_scale[0] = 4

    desc = color_gist_scaletab(img,
                               nblocks,
                               n_scale,
                               orientations_per_scale)

    descsize = 0
    for i in xrange(n_scale):
        descsize += nblocks*nblocks*orientations_per_scale[i]
    descsize *= 3

    for i in xrange(descsize):
        print "%.4f" % desc[i]
    print "\n"

if __name__ == '__main__':
    main()
