import math
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

'USED FUNCTIONS'
def ellipse(points, xc, yc, img_width):
    point_dst = []
    for idx in range(3):
        dst = int(math.hypot(xc - points[idx][0], yc - points[idx][1]))
        point_dst.append((points[idx], dst))

    if point_dst[0][1] > point_dst[2][1]:
        idx = 0
    else:
        idx = 2

    x_point, width = point_dst[idx]
    height = abs(yc - points[1][1])

    'Offset of angle between center and top extreme point'
    delta_x = x_point[0] - xc
    delta_y = x_point[1] - yc
    offset = int(math.degrees(math.atan2(delta_y, delta_x)))

    if abs(offset) > 90:
        angle = offset - 180
    else:
        angle = -abs(offset)

    'Ellipse paramenters'
    center_coordinates = (xc, yc)
    axesLength = (width, height)
    startAngle = 180
    endAngle = 360
    color = (255, 0, 0)
    thickness = -1

    'Build ellipse'
    zeros = np.zeros((img_width, img_width))
    ellipse = cv.ellipse(zeros, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)

    return ellipse

def redefined_mask(ellipse, previous_mask):
    'Select the right extreme of image as the limit of each half of images'
    y, x = np.where(ellipse == 255)

    'Right point'
    idx = np.argmax(x)
    y_right = y[idx]

    'Left point'
    idx = np.argmin(x)
    y_left = y[idx]

    y_limit = np.min((y_right, y_left))
    sup = ellipse[0:y_limit, :]
    inf = previous_mask[y_limit::, :]
    new_mask = np.vstack((sup, np.uint8(inf) * 255))

    return new_mask

def pericardium_3points(image, xc, yc):
    points = []

    'LEFT POINT'
    'Select the point with minimum x value'
    img_aux = image.copy()

    'Discard margins of 100 px'
    img_aux[0:yc - 100, :] = 0
    img_aux[yc + 100::, :] = 0

    y, x = np.where((img_aux == 1))
    idx = np.argmin(x)
    y_left = y[idx]
    x_left = x[idx]
    points.append((x_left, y_left))

    'TOP POINT'
    'Select the point with minimum y value'
    img_aux = image.copy()
    img_aux[:, 0:xc-100] = 0
    img_aux[:, xc+100:] = 0

    y, x = np.where((img_aux == 1))
    idx = np.argmin(y)
    y_top = y[idx]
    x_top = x[idx]
    points.append((x_top, y_top))

    'RIGHT POINT'
    'Select the point with minimum y value'
    img_aux = image.copy()
    img_aux[0:yc - 100, :] = 0
    img_aux[yc + 100::, :] = 0

    y, x = np.where((img_aux == 1))
    idx = np.argmax(x)
    y_right = y[idx]
    x_right = x[idx]
    points.append((x_right, y_right))

    return points