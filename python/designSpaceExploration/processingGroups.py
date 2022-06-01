from binning import *
from compression import *
from dimensionalREduction import *
from georeferencing_and_geometricRegistration import *
from pixelMitigation import *
from smileAndKeystone import *
from targetDetection import *


def g11_algorithm(algorithm, frames, frame_samples, bands, accuracy, binning_factor):
    if (algorithm == "spectral_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spectral_binning(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_spectral_binning(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g12_algorithm(algorithm, frames, frame_samples, bands, accuracy, binning_factor):
    if (algorithm == "spatial_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spatial_binning(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_spatial_binning(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g21_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "thumbnails"):
        new_frames, new_frame_samples, new_bands = DOS_thumbnails(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_thumbnails(frames, framesamples, bands, binningfactor)


    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g22_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "subsamples"):
        new_frames, new_frame_samples, new_bands = DOS_subsamples(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_subsamples(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g31_algorithm(algorithm_detection, algorithm_correction, frames, frame_samples, bands, accuracy, bad_samples, neigbourlevel, cardinal):
        new_frames, new_frame_samples, new_bands = DOS_pixel_mitigation(frames, framesamples, bands, binningfactor, num_regions)

    #detection:
    if (algorithm_detection == "statisical_threshold_detection"):
        accuracy = 1
        cost = OC_statisical_threshold_detection(frames, framesamples, bands, num_regions)
    elif(algorithm_detection == "correlation_detection"):
        accuracy = 1
        cost = OC_correlation_detection(frames, framesamples, bands, num_regions)

    #correction:
    if (algorithm_detection == "avaraging_twice_correction"):
        accuracy = 1
        cost = OC_avaraging_twice_correction(bad_samples, bands)
    elif(algorithm_detection == "nearest_neighbour_correction"):
        accuracy = 1
        cost = OC_nearest_neighbour_correction(bad_samples, bands)
    elif(algorithm_detection == "mean_correction"):
        accuracy = 1
        cost = OC_mean_correction(bad_samples, neigbourlevel, cardinal)
    elif(algorithm_detection == "median_correction"):
        accuracy = 1
        cost = OC_median_correction(bad_samples, neigbourlevel, cardinal)


    elif (algorithm_detection == "x" or algorithm_correction == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    #correction:


    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g32_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "smile_and_keystone"):
        new_frames, new_frame_samples, new_bands = DOS_smile_and_keystone(frames, framesamples, bands)
        accuracy = 1
        cost = OC_smile_and_keystone(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy



def g33_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "radiometric_calibration"):
        new_frames, new_frame_samples, new_bands = DOS_radiometric_calibration(frames, framesamples, bands)
        accuracy = 1
        cost = OC_radiometric_calibration(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g41_algorithm(algorithm, frames, frame_samples, bands, accuracy, reducedbands, iterations):

    new_frames, new_frame_samples, new_bands = DOS_dimensional_reduction(frames, framesamples, bands)

    if (algorithm == "PCA_sw"):
        accuracy = 1
        cost = OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "PCA_hw"):
        accuracy = 1
        cost = OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "MNF"):
        accuracy = 1
        cost = OC_MNF(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "ICA"):
        accuracy = 1
        cost = OC_ICA(frames, framesamples, bands, reducedbands, iterations)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g51_algorithm(algorithm, frames, frame_samples, bands, accuracy, resolution_increase):
    if (algorithm == "georeferencing"):
        new_frames, new_frame_samples, new_bands = DOS_georeferencing(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands)
    if (algorithm == "geometric_registration"):
        new_frames, new_frame_samples, new_bands = DOS_geometric_registration(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands) + OC_geometric_registration(frames, framesamples, bands, resolution_increse)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def gLast_algorithm(algorithm, frames, frame_samples, bands, accuracy):

    #target detection:
    if (algorithm == "georeferencing"):
        new_frames, new_frame_samples, new_bands = DOS_georeferencing(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands)
    if (algorithm == "geometric_registration"):
        new_frames, new_frame_samples, new_bands = DOS_geometric_registration(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands) + OC_geometric_registration(frames, framesamples, bands, resolution_increse)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


