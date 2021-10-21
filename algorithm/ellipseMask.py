import cv2 as cv
import numpy as np

def center_of_mass(binary_img):
    'Find indices where we have mass'
    mass_x, mass_y = np.where(binary_img > 0)
    cent_x = np.average(mass_x)
    cent_y = np.average(mass_y)

    return cent_x, cent_y

def ellipse_mask(width, height):
    mask = np.zeros((width, height))
    center = (250, 250)
    axesLength = (250, 220)
    angle = 0
    startAngle = 0
    endAngle = 360
    color = (255, 255, 255)
    tickness = -1
    circunference = cv.ellipse(mask, center, axesLength, angle, startAngle, endAngle, color, tickness)
    roi = circunference > 254
    return roi

def ellipse_mask_top(width, height, centroid):
    center = (int(centroid[0]), int(centroid[1]))
    mask = np.zeros((width, height))
    axesLength = (180, 180)
    angle = 0
    startAngle = 0
    endAngle = 360
    color = (255, 255, 255)
    tickness = -1
    ellipse = cv.ellipse(mask, center, axesLength, angle, startAngle, endAngle, color, tickness)
    roi = ellipse > 254
    return roi

def circle_crop(roi, img):
    return cv.bitwise_and(img, img, mask=roi.astype(np.uint8))