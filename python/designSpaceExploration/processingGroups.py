from binning import *
from radiometricCalibration import *
from compression import *
from dimensionalReduction import *
from georeferencing_and_geometricRegistration import *
from pixelMitigation import *
from smileAndKeystone import *
from targetDetection import *
from classification import *
from anomalyDetection import *

def g11_algorithm(algorithm, frames, framesamples, bands, accuracy, binningfactor, camera_linse_binning):
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "spectral_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spectral_binning(frames, framesamples, bands, binningfactor)
        new_accuracy = A_spectral_binning(bands, binningfactor, camera_linse_binning)
        cost = OC_spectral_binning(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error spec: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g12_algorithm(algorithm, frames, framesamples, bands, accuracy, binningfactor, whatToBin):
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "spatial_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)
        new_accuracy = A_spatial_binning(frames, framesamples, binningfactor, whatToBin)
        cost = OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error spat: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g21_algorithm(algorithm, frames, framesamples, bands, accuracy):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "thumbnails"):
        new_frames, new_frame_samples, new_bands = DOS_thumbnails(frames, framesamples, bands)
        new_accuracy = 1
        cost = OC_thumbnails(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error thumb: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g22_algorithm(algorithm, frames, framesamples, bands, accuracy, gLast):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "radiometric_calibration"):
        new_frames, new_frame_samples, new_bands = DOS_radiometricCalibration(frames, framesamples, bands)
        if(gLast == "SAM_sw" or gLast == "CEM_sw" or gLast == "ACE_sw" or gLast == "SAM_hw" or gLast == "CEM_hw" or gLast == "ACE_hw" or gLast == "ASMF_hw"):
            new_accuracy = 1.05
        elif(gLast == "GRX_sw"): # usikker på om denne er i pipelinen
            new_accuracy = 1.02
        cost = OC_radiometricCalibration(frames, framesamples, bands)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error R-cal: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g31_algorithm(algorithm_detection, algorithm_correction, frames, framesamples, bands, accuracy, num_regions, bad_samples, neigbourlevel, cardinal):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    

    new_frames, new_frame_samples, new_bands = DOS_pixel_mitigation(frames, framesamples, bands)

    #detection:
    if (algorithm_detection == "statisical_threshold_detection"):
        new_accuracy = 1
        cost = OC_statisical_threshold_detection(frames, framesamples, bands, num_regions)
    elif(algorithm_detection == "correlation_detection"):
        new_accuracy = 1
        cost = OC_correlation_detection(frames, framesamples, bands, num_regions)
    elif(algorithm_detection == "mean_threshold_detection"):
        new_accuracy = 1
        cost = OC_mean_threshold_detection(frames, framesamples, bands)
    elif (algorithm_detection == "x" or algorithm_correction == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error bad P det: ", algorithm_detection)

    #correction:
    if(algorithm_correction == "nearest_neighbour_correction"):
        new_accuracy = 1.05
        cost += OC_nearest_neighbour_correction(bad_samples)
    elif(algorithm_correction == "mean_correction"):
        new_accuracy = 1.05
        cost += OC_mean_correction(bad_samples)
    elif(algorithm_correction == "median_correction"):
        new_accuracy = 1.05
        cost += OC_median_correction(bad_samples)


    elif (algorithm_detection == "x" or algorithm_correction == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error bad P corr: ", algorithm_correction)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g32_algorithm(algorithm, frames, framesamples, bands, accuracy, gLast):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "smile_and_keystone"):
        new_frames, new_frame_samples, new_bands = DOS_smile_and_keystone(frames, framesamples, bands)
        if(gLast == "SAM_sw" or gLast == "CEM_sw" or gLast == "ACE_sw" or gLast == "SAM_hw" or gLast == "CEM_hw" or gLast == "ACE_hw" or gLast == "ASMF_hw"):
            new_accuracy = 1.05
        else:
            new_accuracy = accuracy
        cost = OC_smile_and_keystone(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error Snk: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy



def g33_algorithm(algorithm, frames, framesamples, bands, accuracy):
    if(algorithm != "x"):
        print("Error: Do not use this group, g33")
    return 0, frames, framesamples, bands, accuracy


    """
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "radiometric_calibration"):
        new_frames, new_frame_samples, new_bands = DOS_radiometric_calibration(frames, framesamples, bands)
        new_accuracy = 1.05
        cost = OC_radiometric_calibration(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy
"""

def g41_algorithm(algorithm, frames, framesamples, bands, accuracy, reducedbands, dot_product_blocks, iterations):

    new_frame_samples = 0
    new_frames = 0
    new_bands = 8
    new_accuracy = 1
    cost = 0
    

    if (algorithm == "PCA_sw"):
        new_frames, new_frame_samples, new_bands = DOS_dimensional_reduction(frames, framesamples, bands, reducedbands)
        new_accuracy = A_PCA(bands, reducedbands)
        cost = OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "PCA_hw"):
        new_frames, new_frame_samples, new_bands = DOS_dimensional_reduction(frames, framesamples, bands, reducedbands)
        new_accuracy = A_PCA(bands, reducedbands)
        cost = OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations, dot_product_blocks)
    elif (algorithm == "MNF"):
        new_frames, new_frame_samples, new_bands = DOS_dimensional_reduction(frames, framesamples, bands, reducedbands)
        new_accuracy = A_MNF(bands, reducedbands)
        cost = OC_MNF(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "ICA"):
        new_frames, new_frame_samples, new_bands = DOS_dimensional_reduction(frames, framesamples, bands, reducedbands)
        new_accuracy = A_ICA(bands, reducedbands)
        cost = OC_ICA(frames, framesamples, bands, reducedbands, iterations)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error dimRed: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g51_algorithm(algorithm, frames, framesamples, bands, accuracy, frame_increase_factor, framesample_increase_factor, gLast):
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "georeferencing"):
        new_frames, new_frame_samples, new_bands = DOS_georeferencing(frames, framesamples, bands)
        new_accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands)
    elif (algorithm == "geometric_registration"):
        new_frames, new_frame_samples, new_bands = DOS_geometric_registration(frames, framesamples, bands, frame_increase_factor, framesample_increase_factor)
        if (gLast == "GRX_sw" or gLast == "LRX_sw" or gLast == "F_MGD_hw" or gLast == "FrFT_RX_sw" or gLast == "CRD_sw"):
            new_accuracy = 1.05
        else:
            new_accuracy = accuracy
        cost = OC_geometric_registration(frames, framesamples, bands, frame_increase_factor, framesample_increase_factor)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error georef/reg: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def gLast_algorithm(algorithm, frames, framesamples, bands, accuracy, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors):

    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    #target detection:
    if (algorithm == "SAM_sw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.899 
        cost = OC_SAM(frames, framesamples, bands)
    elif (algorithm == "CEM_sw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.9606
        cost = OC_CEM(frames, framesamples, bands)
    elif (algorithm == "ACE_sw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.9417
        cost = OC_ACE_R(frames, framesamples, bands)

    elif (algorithm == "SAM_hw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.899
        cost = OC_SAM_hw(frames, framesamples, bands)
    elif (algorithm == "CEM_hw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.9606
        cost = OC_target_detection_hw(frames, framesamples, bands)
    elif (algorithm == "ACE_hw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.9417
        cost = OC_target_detection_hw(frames, framesamples, bands)
    elif (algorithm == "ASMF_hw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = (0.9606+0.9417)/2
        cost = OC_target_detection_hw(frames, framesamples, bands)
    
    #anomaly detection:
    elif (algorithm == "GRX_sw"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.9420
        cost = OC_GRX(frames, framesamples, bands)
    elif (algorithm == "LRX_sw"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.9604
        cost = OC_LRX(frames, framesamples, bands, outer_window, inner_window)
    elif (algorithm == "F_MGD_hw"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.9947
        cost = OC_F_MGD(frames, framesamples, bands, kernel_element)
    elif (algorithm == "FrFT_RX_sw"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.9657
        cost = OC_FrFT_RX(frames, framesamples, bands, fractional_domains)
    elif (algorithm == "CRD_sw"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.9673
        cost = OC_CRD(frames, framesamples, bands, num_neighbours)

    #Classification: 
    elif (algorithm == "SVM"):
        new_frames, new_frame_samples, new_bands = DOS_classification(frames, framesamples, bands)
        new_accuracy = 0.967
        cost = OC_SVM(frames, framesamples, bands, num_classes, total_num_support_vectors)


    #CCSDS123 compression: 
    elif (algorithm == "CCSDS123_B1_sw"):
        new_frames, new_frame_samples, new_bands = DOS_CCSDS123_B1(frames, framesamples, bands)
        new_accuracy = 1
        cost = OC_CCSDS123_B1_sw(frames, framesamples, bands, P, D)
    elif (algorithm == "CCSDS123_B1_hw"):
        new_frames, new_frame_samples, new_bands = DOS_CCSDS123_B1(frames, framesamples, bands)
        new_accuracy = 1
        cost = OC_CCSDS123_B1_hw(frames, framesamples, bands, P, D)
    elif (algorithm == "CCSDS123_B2_sw"):
        new_frames, new_frame_samples, new_bands = DOS_CCSDS123_B2(frames, framesamples, bands)
        new_accuracy = 0.9 #no idea
        cost = OC_CCSDS123_B2_sw(frames, framesamples, bands, P, D)
    elif (algorithm == "CCSDS123_B2_hw"):
        new_frames, new_frame_samples, new_bands = DOS_CCSDS123_B2(frames, framesamples, bands)
        new_accuracy = 0.9 #no idea
        cost = OC_CCSDS123_B2_hw(frames, framesamples, bands, P, D)


    #skip this step:
    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0    

    else:
        print("Error last: ", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def create_sample_by_pipeline(pipeline, frames, frame_samples, bands, binning_factor, camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, dot_product_blocks, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors):
    cost = 0
    accuracy = 0.84

    gLast = pipeline[9]
    
    cost_group, frames, frame_sample, bands, accuracy_group = g11_algorithm(pipeline[0], frames, frame_samples, bands, accuracy, binning_factor, camera_linse_binning)
    cost += cost_group
    accuracy *= accuracy_group
    
    cost_group, frames, frame_sample, bands, accuracy_group = g12_algorithm(pipeline[1], frames, frame_samples, bands, accuracy, binning_factor, whatToBin)
    cost += cost_group
    accuracy *= accuracy_group

    cost_group, frames, frame_sample, bands, accuracy_group = g21_algorithm(pipeline[2], frames, frame_samples, bands, accuracy)
    cost += cost_group
    accuracy *= accuracy_group

    #geometric calibration:
    cost_group, frames, frame_sample, bands, accuracy_group = g22_algorithm(pipeline[3], frames, frame_samples, bands, accuracy, gLast)
    cost += cost_group
    accuracy *= accuracy_group
    
    cost_group, frames, frame_sample, bands, accuracy_group = g31_algorithm(pipeline[4], pipeline[5], frames, frame_samples, bands, accuracy, num_regions, bad_samples, neigbourlevel, cardinal)
    cost += cost_group
    accuracy *= accuracy_group
  
    #snk:
    cost_group, frames, frame_sample, bands, accuracy_group = g32_algorithm(pipeline[6], frames, frame_samples, bands, accuracy, gLast)
    cost += cost_group
    accuracy *= accuracy_group

    
    cost_group, frames, frame_sample, bands, accuracy_group = g41_algorithm(pipeline[7], frames, frame_samples, bands, accuracy, reducedbands, iterations, dot_product_blocks)
    cost += cost_group
    accuracy *= accuracy_group
    
    #georeg
    cost_group, frames, frame_sample, bands, accuracy_group = g51_algorithm(pipeline[8], frames, frame_samples, bands, accuracy, frame_increase_factor, framesample_increase_factor, gLast)
    cost += cost_group
    accuracy *= accuracy_group

    cost_group, frames, frame_sample, bands, accuracy_group = gLast_algorithm(pipeline[9], frames, frame_samples, bands, accuracy, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors)
    cost += cost_group
    accuracy *= accuracy_group
    

    return [pipeline, frames*frame_sample*bands, accuracy, cost]


def add_processingmodule_name_to_string(old_string, processing_name):
    if(processing_name == "spectral_binning"):
        old_string += " B (spec),"

    elif(processing_name == "spectral_binning"):
        old_string += " B (spec),"

    elif(processing_name == "spatial_binning"):
        old_string += " B (spat),"
    
    elif(processing_name == "radiometric_calibration"):
        old_string += " Dark current,"

    elif(processing_name == "statisical_threshold_detection"):
        old_string += " Bad Pix Det (stat),"

    elif(processing_name == "correlation_detection"):
        old_string += " Bad Pix Det (corr),"

    elif(processing_name == "mean_threshold_detection"):
        old_string += " Bad Pix Det (mean),"

    elif(processing_name == "nearest_neighbour_correction"):
        old_string += " Bad Pix Corr (neighbor),"

    elif(processing_name == "mean_correction"):
        old_string += " Bad Pix Corr (mean),"

    elif(processing_name == "median_correction"):
        old_string += " Bad Pix Corr (median),"

    elif(processing_name == "smile_and_keystone"):
        old_string += " SnK,"

    elif(processing_name == "georeferencing"):
        old_string += " georef,"

    elif(processing_name == "geometric_registration"):
        old_string += " resample,"

    elif(processing_name == "PCA_sw"):
        old_string += " PCA (sw),"

    elif(processing_name == "PCA_hw"):
        old_string += " PCA (hw),"

    elif(processing_name == "MNF"):
        old_string += " MNF,"

    elif(processing_name == "ICA"):
        old_string += " ICA,"

    elif(processing_name == "SAM_sw"):
        old_string += " SAM (sw),"

    elif(processing_name == "SAM_hw"):
        old_string += " SAM (hw),"

    elif(processing_name == "CEM_sw"):
        old_string += " CEM (sw),"

    elif(processing_name == "CEM_hw"):
        old_string += " CEM (hw),"

    elif(processing_name == "ACE_hw"):
        old_string += " ACE (hw),"

    elif(processing_name == "ACE_sw"):
        old_string += " ACE (sw),"

    elif(processing_name == "ASMF_hw"):
        old_string += " ASMF (hw),"

    elif(processing_name == "SVM"):
        old_string += " SVM,"

    elif(processing_name == "GRX_sw"):
        old_string += " GRX (sw),"

    elif(processing_name == "LRX_sw"):
        old_string += " LRX (sw),"

    elif(processing_name == "F_MGD_hw"):
        old_string += " F-MGD (hw),"

    elif(processing_name == "FrFT_RX_sw"):
        old_string += " FrFT-RX (sw),"

    elif(processing_name == "CRD_sw"):
        old_string += " CRD (sw),"

    elif(processing_name == "CCSDS123_B1_sw"):
        old_string += " Compr B1 (sw),"

    elif(processing_name == "CCSDS123_B1_hw"):
        old_string += " Compr B1 (hw),"

    elif(processing_name == "CCSDS123_B2_sw"):
        old_string += " Compr B2 (sw),"

    elif(processing_name == "CCSDS123_B2_hw"):
        old_string += " Compr B2 (hw),"

    elif(processing_name == "x"):
        return old_string

    else:
        print("Unknown name, ", processing_name)   

    return old_string


def RGB(red, green, blue):
    rgb = "#"
    if(red < 16):
        rgb += "0" + hex(red)[-1]
    else:
        rgb += hex(red)[-2] + hex(red)[-1]
    if(green < 16):
        rgb += "0" + hex(green)[-1]
    else:
        rgb += hex(green)[-2] + hex(green)[-1]
    if(blue < 16):
        rgb += "0" + hex(blue)[-1]
    else:
        rgb += hex(blue)[-2] + hex(blue)[-1]
    return rgb

colors_1crimson = [RGB(220,20,60)]

colors_3turkis = [RGB(69,139,116), RGB(102,205,170), RGB(127,244,212)]
colors_3ligthblue = [RGB(83,134,139), RGB(122,197,205), RGB(152,245,255)]
colors_3pink = [RGB(139,10,80), RGB(205,16,118), RGB(255,20,147)]

colors_5brown = [RGB(138,51,36), RGB(156,102,31), RGB(139,131,120), RGB(205,192,176), RGB(238,223,204)]
colors_5gray = [RGB(40,40,40), RGB(91,91,91), RGB(132,132,132), RGB(183,183,183), RGB(215,215,215)]
colors_5purple = [RGB(72,61,139), RGB(104,34,139), RGB(154,50,205), RGB(191,62,255), RGB(238,130,238)]
colors_yellow = [RGB(139,105,20), RGB(205,155,29), RGB(255,215,0), RGB(255,255,0), RGB(244,246,143)]

colors_6red = [RGB(255,0,0), RGB(205,0,0), RGB(155,0,0), RGB(105,0,0), RGB(55,0,0), RGB(10,0,0)]
colors_6green = [RGB(0,255,0), RGB(0,205,0), RGB(0,155,0), RGB(0,105,0), RGB(0,55,0), RGB(0,10,0)]
colors_6blue = [RGB(0,0,255), RGB(0,0,205), RGB(0,0,155), RGB(0,0,105), RGB(0,0,55), RGB(0,0,10)]

colors_costs = ["black", colors_3turkis[0], colors_3turkis[1], colors_3ligthblue[0], colors_3ligthblue[1], colors_3pink[0], colors_3pink[1], colors_3pink[2], colors_5brown[0], colors_5gray[1], \
colors_5purple[0], colors_5purple[1], colors_yellow[0], colors_yellow[1], colors_yellow[2], colors_yellow[3], colors_6red[0], colors_6red[1], colors_6red[2], colors_6red[3], colors_6red[4], \
"grey", colors_6green[0], colors_6green[1], colors_6green[2], colors_6green[3], colors_6green[4], colors_6blue[0], colors_6blue[1], colors_6blue[2], colors_6blue[3], colors_1crimson[0]]

colors_all = [RGB(138,51,36), RGB(156,102,31), RGB(139,131,120), RGB(205,192,176), RGB(238,223,204), RGB(139,10,80), RGB(205,16,118), RGB(255,20,147), RGB(83,134,139), RGB(122,197,205), RGB(152,245,255), RGB(69,139,116), RGB(102,205,170), RGB(127,244,212), RGB(0,0,255), RGB(0,0,205), RGB(0,0,155), RGB(0,0,105), RGB(0,0,55), RGB(0,0,10), RGB(0,255,0), RGB(0,205,0), RGB(0,155,0), RGB(0,105,0), RGB(0,55,0), RGB(0,10,0), RGB(255,0,0), RGB(205,0,0), RGB(155,0,0), RGB(105,0,0), RGB(55,0,0), RGB(10,0,0), RGB(139,105,20), RGB(205,155,29), RGB(255,215,0), RGB(255,255,0), RGB(244,246,143), RGB(72,61,139), RGB(104,34,139), RGB(154,50,205), RGB(191,62,255), RGB(238,130,238), RGB(40,40,40), RGB(91,91,91), RGB(132,132,132), RGB(183,183,183), RGB(215,215,215)]