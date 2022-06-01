from OC_utility import *


def DOS_anomaly_detection(frames, framesamples, bands):
    new_frames = frame
    new_frame_samples = frame_samples
    new_bands = 1
    return new_frames, new_frame_samples, new_bands


def OC_GRX_R(frames, framesamples, bands):
    return bands * mean(frames*framesamples) + correlation_matrix(frames * framesamples, bands) + quadratic_matrix_inversion(bands) + frames * framesamples * (subtraction() + matrix_vector_multiplication(frames*framesamples, bands) + dot_product(bands))

def OC_LRX(frames, framesamples, bands, outer_window, inner_window):
    #firt window samples:
    return correlation_matrix(quadratix_window_size-inner_window) + quadratix_matrix_invertion(bands) + bands * mean(outer_window-inner_window) + (outer_window - inner_window) * subtraction() \ #first window operations
    frames * framesamples * (2 * sherman_morris_update(size) + 4 * division() + 4 * subtraction() + 2 * multiplication() + matrix_vector_multiplication(bands, bands) + dot_product(bands)) #sliding windows
    
def OC_DWRX(frames, framesamples, bands, outer_window, inner_window):
    return OC_LRX(frames, framesamples, bands, outer_window, inner_window) + bands * mean(inner_window) + frames * framesamples * (4 * division() + 2 * subtraction() + 2 * addition()) 

def OC_FrFT_RX(frames, framesamples, bands):
    return 1

def OC_CRD(frames, framesamples, bands):
    return 1
