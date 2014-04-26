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
    ALL_COLORS = 64

    def __init__(self, image_file):
        self._im_org = Image.open(image_file)

    def extract(self):
        self.blur()

    def blur(self):
        self._im = self._im_org.copy()
        w, h = self._im.size

        for y in xrange(1, h-1):
            for x in xrange(1, w-1):
                adj_pixels = [self._im_org.getpixel((i, j))
                              for i in xrange(x-1, x+2)
                              for j in xrange(y-1, y+2)]

                # replace pixel value
                self._im.putpixel((x, y),
                                  tuple(
                                      map(int,
                                          np.mean(adj_pixels, 0).tolist()
                                          )
                                  ))


def main():
    ccv = CCV('snow_leopard.jpg')
    ccv.extract()

if __name__ == '__main__':
    main()
