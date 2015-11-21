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


def main():
    args = docopt(__doc__)
    image_file = args['<image_file>']
    if not os.path.exists(image_file):
        print 'Not found:', image_file
        sys.exit(-1)

if __name__ == '__main__':
    main()
