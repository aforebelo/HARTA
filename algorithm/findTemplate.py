import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math

'@param image: dtype np.uint8'
'@param template: dtype np.uint8'
'@param method: string'
'@return top left and botom right points of found template'
def find_template_sternal(dataset, template, method):
    method = eval(method)
    h, w = template.shape[0:2]

    not_first = False
    distance = 0
    previous_top_left = (0, 0)
    top = []
    bottom = []

    # i = 0
    for image in dataset:
        mid_height = int(image.shape[1]/2)
        image = image[0:mid_height, :]
        res = cv.matchTemplate(image, template, method)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc

        distance = math.sqrt(((top_left[0] - previous_top_left[0]) ** 2) + ((top_left[1] - previous_top_left[1]) ** 2))
        if not_first:
            pass

        if top_left[1] > 0.5*mid_height or distance > 150:
            top_left = previous_top_left
            top.append(top_left)
        else:
            previous_top_left = top_left
            top.append(previous_top_left)

        bottom_right = (top_left[0] + w, top_left[1] + h)
        bottom.append(bottom_right)
        not_first = True

        'Uncomment to plot the image with the found template with a square'
        # if i == 6:
        #     cv.rectangle(image, top_left, bottom_right, 255, 2)
        #     plt.subplot(121), plt.imshow(res, cmap='gray')
        #     plt.title('Matching result'), plt.xticks([]), plt.yticks([])
        #     plt.subplot(122), plt.imshow(image, cmap='gray')
        #     plt.title('Sternal detected'), plt.xticks(np.arange(0, 512, step = 100)), plt.yticks(np.arange(0, 256,
        #                                                                                                  step=100))
        #     # plt.show()
        #     plt.savefig(f'imagens/matchingtemplate_sternal_{i}.pdf')
        # i = i + 1

    return top, bottom

def find_template_spine(dataset, template, method):
    method = eval(method)
    h, w = template.shape[0:2]
    mid_height = 256
    previous_top_left = (mid_height, mid_height)

    not_first = False
    distance = 0
    top = []
    bottom = []

    # i = 0
    for image in dataset:
        image = image[mid_height::, :]
        res = cv.matchTemplate(image, template, method)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc

        if not_first:
            distance = math.sqrt(((top_left[0] - previous_top_left[0]) ** 2) + ((top_left[1] - previous_top_left[1]) ** 2))

        if top_left[1] < 0.1*mid_height or distance > 20:
            top_left = previous_top_left
            top.append(top_left)
        else:
            previous_top_left = top_left
            top.append(previous_top_left)

        bottom_right = (top_left[0] + w, top_left[1] + h)
        bottom.append(bottom_right)
        not_first = True

        'Uncomment to plot the image with the found template with a square'
        # if i == 12:
        #     cv.rectangle(image, top_left, bottom_right, 255, 2)
        #     plt.subplot(121), plt.imshow(res, cmap='gray')
        #     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        #     plt.subplot(122), plt.imshow(image, cmap='gray')
        #     plt.title('Detected Point'), plt.xticks(np.arange(0, 512, step = 100)), plt.yticks(np.arange(0, 256,
        #                                                                                                  step=100))
        #     # plt.show()
        #     plt.savefig(f'imagens/matchingtemplate_spine_{i}.pdf')
        # i = i + 1

    return top, bottom

'@param img: any dtype'
'@param y: the point from which will be cutted the image in vertical direction'
'@param WIDTH: WIDTH of original image where the template will be found'
'@return cutted image'
def cut_image_from_top(img, y, width, y_reject):
    if y == 0:
        new = img
    else:
        y = int(y*0.85)
        remove = np.zeros((y, width))
        heart = img[y::, :]
        new = np.vstack((remove, heart))
    return new

'@param img: any dtype'
'@param y: the point from which will be cutted the image in vertical direction'
'@param WIDTH: WIDTH of original image where the template will be found'
'@param y_reject: y value that means the image do not have the template in image'
'@return cutted image'

def cut_image_from_bottom(img, y, width, y_reject):
    if y == y_reject:
        new = img
    else:
        heart = img[0:y, :]
        remove = np.zeros((width - y, width))
        new = np.vstack((heart, remove))
    return new