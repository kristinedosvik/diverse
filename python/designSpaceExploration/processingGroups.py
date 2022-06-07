from binning import *
from compression import *
from dimensionalReduction import *
from georeferencing_and_geometricRegistration import *
from pixelMitigation import *
from smileAndKeystone import *
from targetDetection import *
from anomalyDetection import *

def g11_algorithm(algorithm, frames, framesamples, bands, accuracy, binningfactor):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "spectral_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spectral_binning(frames, framesamples, bands, binningfactor)
        new_accuracy = 0.8 # no idea
        cost = OC_spectral_binning(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g12_algorithm(algorithm, frames, framesamples, bands, accuracy, binningfactor, whatToBin):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "spatial_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)
        new_accuracy = 0.5 #no idea
        cost = OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm)

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
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g22_algorithm(algorithm, frames, framesamples, bands, accuracy):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "subsamples"):
        new_frames, new_frame_samples, new_bands = DOS_subsamples(frames, framesamples, bands)
        new_accuracy = 1
        cost = OC_subsamples(frames, framesamples, bands)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm)

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

    elif (algorithm_detection == "x" or algorithm_correction == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm_detection)

    #correction:
    if (algorithm_correction == "avaraging_twice_correction"):
        new_accuracy = 1.07
        cost += OC_avaraging_twice_correction(bad_samples, bands)
    elif(algorithm_correction == "nearest_neighbour_correction"):
        new_accuracy = 1.07
        cost += OC_nearest_neighbour_correction(bad_samples, bands)
    elif(algorithm_correction == "mean_correction"):
        new_accuracy = 1.07
        cost += OC_mean_correction(bad_samples, neigbourlevel, cardinal)
    elif(algorithm_correction == "median_correction"):
        new_accuracy = 1.07
        cost += OC_median_correction(bad_samples, neigbourlevel, cardinal)


    elif (algorithm_detection == "x" or algorithm_correction == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm_correction)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g32_algorithm(algorithm, frames, framesamples, bands, accuracy):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "smile_and_keystone"):
        new_frames, new_frame_samples, new_bands = DOS_smile_and_keystone(frames, framesamples, bands)
        new_accuracy = 1.07
        cost = OC_smile_and_keystone(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy



def g33_algorithm(algorithm, frames, framesamples, bands, accuracy):
    
    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    if (algorithm == "radiometric_calibration"):
        new_frames, new_frame_samples, new_bands = DOS_radiometric_calibration(frames, framesamples, bands)
        new_accuracy = 1.07
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


def g41_algorithm(algorithm, frames, framesamples, bands, accuracy, reducedbands, iterations):

    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    new_frames, new_frame_samples, new_bands = DOS_dimensional_reduction(frames, framesamples, bands, reducedbands)

    if (algorithm == "PCA_sw"):
        new_accuracy = 0.9 #no idea
        cost = OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "PCA_hw"):
        new_accuracy = 0.9 #no idea
        cost = OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "MNF"):
        new_accuracy = 0.9 #no idea
        cost = OC_MNF(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "ICA"):
        new_accuracy = 1
        cost = OC_ICA(frames, framesamples, bands, reducedbands, iterations)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def g51_algorithm(algorithm, frames, framesamples, bands, accuracy, frame_increase_factor, framesample_increase_factor):
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
        new_accuracy = 1.07
        cost = OC_geometric_registration(frames, framesamples, bands, frame_increase_factor, framesample_increase_factor)

    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


def gLast_algorithm(algorithm, frames, framesamples, bands, accuracy, outer_window, inner_window, P, D):

    new_frame_samples = 0
    new_frames = 0
    new_bands = 0
    new_accuracy = 1
    cost = 0
    
    #target detection:
    if (algorithm == "SAM"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.1 #no idea
        cost = OC_SAM(frames, framesamples, bands)
    elif (algorithm == "CEM"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.03
        cost = OC_CEM(frames, framesamples, bands)
    elif (algorithm == "ACE_R"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.71
        cost = OC_ACE_R(frames, framesamples, bands)
    elif (algorithm == "target_detection_hw"):
        new_frames, new_frame_samples, new_bands = DOS_target_detection(frames, framesamples, bands)
        new_accuracy = 0.71 #must seperate them
        cost = OC_target_detection_hw(frames, framesamples, bands)

    #anomaly detection:
    elif (algorithm == "GRX_R"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.94
        cost = OC_GRX_R(frames, framesamples, bands)
    elif (algorithm == "LRX"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.96
        cost = OC_LRX(frames, framesamples, bands, outer_window, inner_window)
    elif (algorithm == "DWRX"):
        new_frames, new_frame_samples, new_bands = DOS_anomaly_detection(frames, framesamples, bands)
        new_accuracy = 0.95 # no idea
        cost = OC_DWRX(frames, framesamples, bands, outer_window, inner_window)

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
        new_accuracy = 0.8 #no idea
        cost = OC_CCSDS123_B2_sw(frames, framesamples, bands, P, D)
    elif (algorithm == "CCSDS123_B2_hw"):
        new_frames, new_frame_samples, new_bands = DOS_CCSDS123_B2(frames, framesamples, bands)
        new_accuracy = 0.8 #no idea
        cost = OC_CCSDS123_B2_hw(frames, framesamples, bands, P, D)

    #skip this step:
    elif (algorithm == "x"):
        new_frame_samples = framesamples
        new_frames = frames
        new_bands = bands
        new_accuracy = 1
        cost = 0    

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, new_accuracy


