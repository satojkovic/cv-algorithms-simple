#-*- coding: utf-8 -*-

"""
1. Blur the image
   replacing each pixel's value with the average value of the
   8 adjacent pixels
2. Discretize the colorspace into n(64 in paper) distinct colors
3. Classify pixels as either coherent or incoherent
   - Computing a connected components C for each distinct color
     C is a maximal set of pixels with same color
     (count if two pixels are eight closest neighbors)
     (C can be computed in a single pass over the image)
   - Detemine Tau's value(25 in paper)
   - C is coherent if the size of C exceeds a Tau, otherwise C is incoherent
4. Compute the CCV
   alpha is the number of coherent pixels
   beta is the number of incoherent pixels

   CCV = <(alpha_1, beta_1), ..., (alpha_n, beta_n)>
"""


from PIL import Image, ImageFilter
import numpy as np


class CCV(object):
    def __init__(self, image_file):
        self._im = Image.open(image_file)
        self._ccv = []

    def extract(self):
        self._blurred_im = self._im.filter(ImageFilter.BLUR)
        self._ccv


def main():
    ccv = CCV('snow_leopard.jpg')
    print ccv.extract()

if __name__ == '__main__':
    main()
