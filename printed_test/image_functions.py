# this will be a module with a bunch of functions for applying filters and what
# not to images 
# all the input to functions should be a path to a *.png image.
# all the functions should return a list of the new images
from scipy.misc import imread, imsave
from scipy import ndimage
import numpy as np
import cv2

def rotations(img, size=100):
    return [ndimage.rotate(img,i,mode='nearest') for i in np.arange(30.0, 50.0, 2)]
def fourier(img, size=100):
    return [ndimage.fourier_ellipsoid(img,size),
            ndimage.fourier_shift(img,size),
            ndimage.fourier_uniform(img,size)]
def filters(img, size=100):
    l = [ndimage.gaussian_filter(img, i) for i in np.arange(0,4,0.5)] + \
        [ndimage.maximum_filter(img, i) for i in np.arange(1,4,0.2)] + \
        [ndimage.median_filter(img, i) for i in np.arange(1,4,0.2)] + \
        [ndimage.minimum_filter(img, i) for i in np.arange(1,4,0.2)]
    return l
            
def zoom(img, size=100):
    return [ndimage.zoom(img, i) for i in np.arange(1,5,0.5)]

def blur(img, size=100):
    blurs = [cv2.blur(img, (5,5)), cv2.GaussianBlur(img, (5,5), 0)]
    return blurs

def get():
    return [rotations, blur, filters, zoom]
"""
    70 word part
    1000
    filters: 
        smoothing - blare
"""
