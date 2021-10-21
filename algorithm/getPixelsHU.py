import numpy as np

def get_pixels_hu(scans):
    image = np.stack([s.pixel_array for s in scans])

    'Convert to int16'
    image = image.astype(np.int16)

    'Set outside-of-scan pixels to 1'
    'The intercept is usually -1024, so air is approximately 0'
    image[image == -2000] = 0

    'Convert to Hounsfield units (HU)'
    intercept = scans[0].RescaleIntercept
    slope = scans[0].RescaleSlope
    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)
    image += np.int16(intercept)

    return np.array(image, dtype=np.int16)