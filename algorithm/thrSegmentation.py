import numpy as np
import cv2 as cv

"""
Return the fat ranged mask of a heart image

Parameters
----------
img : numpy.ndarray
    An image in HU scale
    
min_HU : int
    The minimum value of the expected fat range in HU
    
max_HU : int
    The minimum value of the expected fat range in HU
    
Returns
-------
mask : numpy.ndarray
    A binary image
"""
def thrSegmentation(img, min_HU, max_HU):
    upper = np.where(img<=max_HU, True, False)
    down = np.where(img>=min_HU, True, False)
    mask = cv.bitwise_and(upper.astype(np.uint8), down.astype(np.uint8))
    return mask


"""
Return the fat ranged image of a heart image by applying a mask on the original image.

Parameters
----------
img : numpy.ndarray
    An image in HU scale or 8 bit-depth

mask : numpy.ndarray
    A binary image

Returns
-------
    numpy.ndarray
"""
def remove_calcification(img, max_HU):
    mask = img<max_HU
    mask.astype(np.uint8)
    zeros = np.zeros_like(img)
    zeros[mask] = img[mask]
    return zeros


def applyMask(img, mask):
    return cv.bitwise_and(img,img,mask = mask)