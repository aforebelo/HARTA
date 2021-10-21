'**********************************************************************************************************************'
import matplotlib.pyplot as plt

'This file contains the semiautomatic method for epicardial fat segmentation'
'**********************************************************************************************************************'
import numpy as np
import cv2 as cv

#MY FUNCTIONS
from algorithm.basicOperations import convert_image_to_rgb, add_images, segmentation
from algorithm.loadScan import load_scan
from algorithm.getPixelsHU import get_pixels_hu
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


'Convert 3-channel image to binary image'
'@param filename: 3-channel image'
'@return T/F binary image'
def rgb_to_binary(filename):
    rgb = cv.imread(filename)
    bw_img = rgb[:,:,0] > 0
    return bw_img

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

    ### CONSTANTS
    MAX_FAT = -30
    MIN_FAT = -200

    ### 1. ROI SELECTION
    'Get contours redifined by user'
    new_masks = np.stack([rgb_to_binary(f'{OUTPUT_FOLDER}contours/{patient_id}_{i}_c.png') for i in range(0, no_slices)])

    i = patients_hu[0]
    m = new_masks[0]
    nh= segmentation(i, m)
    plt.imshow(nh)

    new_heart = np.stack([segmentation(i, m) for i, m in zip(patients_hu, new_masks)])

    ### 4. EAT SEGMENTATION
    'Fat thresholding'
    fat_masks = np.stack([thrSegmentation(r, MIN_FAT, MAX_FAT) for r in new_heart])

    'To show the final result of segmentation'
    np.stack([convert_image_to_rgb(mask, f'fat/{patient_id}_{i}_fat', OUTPUT_FOLDER) for mask, i in zip(fat_masks, range(0, no_slices))])
    'Read the slice images already save in automatic method'
    images_png = np.stack([cv.imread(f'{OUTPUT_FOLDER}slices/{patient_id}_{i}.png') for i in range(0, no_slices)])

    'Add slice image with segmentation mask'
    combined_images = np.stack([add_images(m, img) for m, img in zip(fat_masks, images_png)])

    'Save image with segmentation enhanced'
    np.stack([convert_image_to_rgb(img, f'combined/{patient_id}_{i}_combined', OUTPUT_FOLDER) for img, i in zip(combined_images, range(0,
                                                                                                                                       no_slices))])
    ### 6. VOLUME CALCULATION
    vol = volume(fat_masks, thickness, px_spacing)

    return patient_id, no_slices, vol

