import numpy as np

def doTouchInMargin(slice):
    margin_right = slice[:,0].sum()
    margin_left = slice[:, -1].sum()
    if margin_right > 0 and margin_left > 0:
        new_slice = np.zeros_like(slice)
    elif margin_right > 255*100 or margin_left > 255*100:
        new_slice = np.zeros_like(slice)
    else:
        new_slice = slice
    return new_slice

def countDiscardSlices(dataset_binary):
    no = 0
    for slice in dataset_binary:
        if slice.sum() == 0:
            no = no + 1
        else:
            pass
    return no

def contourArea(contour):
    mask = np.uint8(contour > 0)
    white = mask.sum()
    total = contour.shape[0]*contour.shape[1]
    area = white/total
    print(area)

    if area > 0.45:
        new_contour = np.zeros_like(contour)
    else:
        new_contour = contour
    return new_contour