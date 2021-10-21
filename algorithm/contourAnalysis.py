import cv2 as cv

def find_contours(img):
    contours = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    return contours

def draw_contours(img):
    contours = find_contours(img)
    for contour in contours:
        cv.drawContours(img, [contour], 0, (255, 255, 255), -1)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (65, 70))
    opening = cv.morphologyEx(img, cv.MORPH_ELLIPSE, kernel, iterations=2)
    return opening

def moment(mask):
    M = cv.moments(mask)
    cx = M["m10"] / M["m00"]
    cy = M["m01"] / M["m00"]
    return int(cx), int(cy)