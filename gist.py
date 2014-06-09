#-*- coding: utf-8 -*-

import argparse
from PIL import Image
import leargist


def main():
    parser = argparse.ArgumentParser(
        description='compute gist descriptor',
    )

    parser.add_argument(
        help='image file name',
        dest='imgfile',
    )

    args = parser.parse_args()

    im = Image.open(args.imgfile)
    desc = leargist.color_gist(im)

    print desc.shape
    print desc[:4]

if __name__ == '__main__':
    main()
