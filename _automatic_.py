'**********************************************************************************************************************'
'This file contains the automatic method for epicardial fat segmentation'
'**********************************************************************************************************************'
import numpy as np
import cv2 as cv
from skimage.morphology import convex_hull_image

#MY FUNCTIONS
from algorithm.basicOperations import convert_image_to_rgb, add_images, otsu_mask, connect_components, segmentation, opening
from algorithm.findTemplate import find_template_sternal, find_template_spine, cut_image_from_top, cut_image_from_bottom
from algorithm.loadScan import load_scan
from algorithm.getPixelsHU import get_pixels_hu
from algorithm.pericardiumDelineation import pericardium_3points, ellipse, redefined_mask
from algorithm.contourAnalysis import draw_contours, moment
from algorithm.discardSlices import doTouchInMargin, countDiscardSlices
from algorithm.thrSegmentation import thrSegmentation
from algorithm.volume import volume
from algorithm.plot3D import plot_3d
from algorithm.sampleStack import sample_stack

'Parameters:'
'@param INPUT_FOLDER: string. Folder path with DICOM dataset'

'Returns'
'@param no_slices: int. Number of slices of a dataset.'
'@param images_png: PNG files. Original images of slices'
'@param patient_id: string. ID that identify the patient'
'@param vol: float. Volume of epicardial fat'
'@param combined_images: PNG files. Original slices with epicardial enhanced'

def segmentEpicardialFat(DICOM_DATASET = 'path/dicom_file.dcm', OUTPUT_FOLDER='aux_img/'):
    'Select the patient dataset'
    patient = load_scan(DICOM_DATASET)

    'Thickness and pixel spacing'
    thickness = patient[0].SliceThickness
    px_spacing = patient[0].PixelSpacing[0]
    patient_id = patient[0].PatientID
    no_slices = len(patient)

    'Get image in HU scale'
    patients_hu = get_pixels_hu(patient)

    'Constants'
    WIDTH = patients_hu[0].shape[0]
    HEIGHT = patients_hu[0].shape[1]
    MID_HEIGHT = int(HEIGHT / 2)

    ### CONSTANTS
    MAX_FAT = -30
    MIN_FAT = -200

    ### PRE-PROCESSING
    median = np.stack([cv.medianBlur(patient, 5) for patient in patients_hu])
    ### 1. ROI SELECTION
    'Matching template to detect sternal and spine'
    template_sternal = cv.imread('resources/template_sternum.png')
    template_spine = cv.imread('resources/template_spine.png')

    'Convert imagens to rgb channels'
    images_png = np.stack([convert_image_to_rgb(dicom, f'slices/{patient_id}_{i}', OUTPUT_FOLDER) for dicom, i in zip(median, range(0,no_slices))])

    top_points = find_template_sternal(images_png, template_sternal, method='cv.TM_CCOEFF_NORMED')[1]
    bottom_points = find_template_spine(images_png, template_spine, method='cv.TM_CCOEFF_NORMED')[0]

    'Remove the lungs'
    remove_lung_mask = np.stack([otsu_mask(patient) for patient in median])

    'Remove torax'
    remove_torax_mask = np.stack([cut_image_from_top(slice, point[1], WIDTH, y_reject=0) for slice, point in
                                  zip(remove_lung_mask, top_points)])

    'Remove spine'
    remove_spine_mask = np.stack(
        [cut_image_from_bottom(slice, MID_HEIGHT + point[1], WIDTH, y_reject=MID_HEIGHT) for slice, point in
         zip(remove_torax_mask, bottom_points)])

    ### 2. HEART ROI
    'Find contours with ellipse morphology'
    contours = np.stack([draw_contours(img.astype(np.uint8)) for img in remove_spine_mask])

    'Selection of the bigger component regarding the component with the heart'
    bigger_component = np.stack([connect_components(mask) for mask in contours])

    'Apply masks of ROI to segmentate the heart'
    masks = np.stack([contour > 0 for contour in bigger_component])
    heart = np.stack([segmentation(i, m) for i, m in zip(patients_hu, masks)])

    ### 3. PERICARDIUM DELIMITATION
    # -44 a 18 HU
    'Pericardium thresholding'
    pericardium_mask = np.stack([thrSegmentation(r, -44, -1) for r in heart])
    'Get pericardium contour'
    pericardium_contour = np.stack([convex_hull_image(mask) for mask in pericardium_mask])
    pericardium_opening = np.stack([opening(mask) for mask in pericardium_contour])

    'Redefine ROI of heart'
    new_contours = np.stack([contour > 0 for contour in pericardium_opening])

    'Discard slices that touch left or right margins'
    processed_slices = np.stack([doTouchInMargin(slice) for slice in new_contours])
    discard_slices = countDiscardSlices(processed_slices)

    'Convert imagens to rgb channels'
    np.stack([convert_image_to_rgb(cnt, f'contours/{patient_id}_{i}_c', OUTPUT_FOLDER) for cnt, i in zip(processed_slices, range(0,no_slices))])

    'Discard slices that touch left or right margins'
    new_masks = np.stack([contour > 0 for contour in processed_slices])
    new_heart = np.stack([segmentation(i, m) for i, m in zip(patients_hu, new_masks)])

    ### 4. EAT SEGMENTATION
    'Fat thresholding'
    fat_masks = np.stack([thrSegmentation(r, MIN_FAT, MAX_FAT) for r in new_heart])

    'To show the final result of segmentation'
    np.stack([convert_image_to_rgb(mask, f'fat/{patient_id}_{i}_fat', OUTPUT_FOLDER) for mask, i in zip(fat_masks, range(0, no_slices))])

    'Add slice image with segmentation mask'
    combined_images = np.stack([add_images(m, img) for m, img in zip(fat_masks, images_png)])

    'Save image with segmentation enhanced'
    np.stack([convert_image_to_rgb(img, f'combined/{patient_id}_{i}_combined', OUTPUT_FOLDER) for img, i in zip(combined_images, range(0,no_slices))])

    ### 6. VOLUME CALCULATION
    vol = volume(fat_masks, thickness, px_spacing)

    return patient_id, no_slices, vol

