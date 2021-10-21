import matplotlib.pyplot as plt
import cv2 as cv

def get_red(img):
    heart = cv.imread(img)
    r = heart[:, :, 2]
    g = heart[:, :, 1]
    b = heart[:, :, 0]

    'Get the common gray stuctures'
    common = cv.bitwise_and(r, g)
    common = cv.bitwise_and(common, b)

    'Get the pericardial fat - ONLY RED!'
    red = cv.bitwise_xor(r, common)
    return red > 0

def get_blue(img):
    heart = cv.imread(img)

    r = heart[:, :, 2]
    g = heart[:, :, 1]
    b = heart[:, :, 0]

    'Get the common gray stuctures'
    common = cv.bitwise_and(r, g)
    common = cv.bitwise_and(common, b)

    'Get the pericardial fat - ONLY BLUE!'
    blue = cv.bitwise_xor(b, common)
    return blue > 0

def get_white(img):
    heart = cv.imread(img)

    r = heart[:, :, 2]
    g = heart[:, :, 1]
    b = heart[:, :, 0]

    'Get the pericardial fat - ONLY WHITE!'
    'White = R + G + B'
    rg = cv.bitwise_and(r, g)
    white = cv.bitwise_and(rg, b)

    return white > 0

def count_px(binary_scans):
    count = 0
    for scan in binary_scans:
        count = count + scan.sum()
    return count