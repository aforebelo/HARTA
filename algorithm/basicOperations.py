import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters.thresholding import threshold_otsu

'@param image: dtype different of np.uint8'
'@return 3-channel image'
def convert_image_to_rgb(image, filename, output_folder):
    plt.imsave(f'{output_folder}{filename}.png', image, cmap='gray')
    return cv.imread(f'{output_folder}{filename}.png')

'@param mask: numpy.ndarray with values 0 (non-fat pixels) and 1 (fat pixels)'
'@param img: 3-channel image'
'@return 3-channel image mask+img'
def add_images(mask, img):
    mask_rgb = np.dstack((mask, mask, mask))
    img[np.where((mask_rgb == [1, 1, 1]).all(axis=2))] = [172, 16, 12]
    return img

'@param img: 3-channel image'
'@return binary image'
def otsu_mask(img):
    thr = threshold_otsu(img)
    binary = img > thr

    'Uncoment to plot results'
    # fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
    # ax = axes.ravel()
    # ax[0] = plt.subplot(1, 3, 1)
    # ax[1] = plt.subplot(1, 3, 2)
    # ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])
    #
    # ax[0].imshow(img, cmap=plt.cm.gray)
    # ax[0].set_title('Original')
    #
    # ax[1].hist(img.ravel(), bins=3000)
    # ax[1].set_title('Histogram')
    # ax[1].axvline(thr, color='r')
    #
    # ax[2].imshow(binary, cmap='gray')
    # ax[2].set_title('Thresholded')
    #
    # plt.show()

    return binary

'@param img: 3-channel image'
'@param mask: numpy.ndarray with values 0 and 1'
'@return binary image'
def connect_components(binary):
    new_img = np.zeros_like(binary)
    for val in np.unique(binary)[1:]:
        mask = np.uint8(binary == val)
        labels, stats = cv.connectedComponentsWithStats(mask, 4)[1:3]
        largest_label = 1 + np.argmax(stats[1:, cv.CC_STAT_AREA])
        new_img[labels == largest_label] = val
    return new_img

'@param img: 3-channel image'
'@param mask: numpy.ndarray with values 0 and 1'
'@return binary image'
def segmentation(img, mask):
    zeros = np.zeros_like(img)-300
    zeros[mask] = img[mask]
    return zeros

'@param hull: binary (boolean) image'
'@param mask: numpy.ndarray with values 0 and 1'
def opening(hull):
    hull = np.uint8(hull)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (40, 40))
    opening = cv.morphologyEx(hull, cv.MORPH_ELLIPSE, kernel, iterations=3)
    return opening