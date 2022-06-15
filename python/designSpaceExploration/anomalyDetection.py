from OC_utility import *


def DOS_anomaly_detection(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = 1
    return new_frames, new_frame_samples, new_bands


def OC_GRX(frames, framesamples, bands):
    return (bands * mean(frames*framesamples) + correlation_matrix(frames * framesamples, bands) + matrix_inversion(bands) + frames * framesamples * (subtraction() + matrix_vector_multiplication(frames*framesamples, bands) + dot_product(bands))) + frames*framesamples*(bands*subtraction() + matrix_vector_multiplication(bands, bands) + dot_product(bands))

def OC_LRX(frames, framesamples, bands, outer_window, inner_window):
    return (correlation_matrix(outer_window-inner_window, bands) + matrix_inversion(bands) + bands*mean(outer_window-inner_window) + bands*subtraction() + matrix_vector_multiplication(bands, bands) + dot_product(bands)) + frames*framesamples*(bands * update_mean() + update_inversion_matrix(bands) + bands*subtraction() + matrix_vector_multiplication(bands, bands) + dot_product(bands))

def OC_FrFT_RX(frames, framesamples, bands, fractional_domains):
    return frames*framesamples*bands*fractional_domains*( \
        (division() + bands*addition()) + \
        (10*multiplication() + 3*trignomitry() + division() + subtraction() + addition() + exp()) + \
        (3*division() + exp() + 3*multiplication() + trignomitry() + absolute_value() + sqrt() + sign())) \
        + (fractional_domains*(addition() + log() + multiplication()) + multiplication()) \
        + (frames*framesamples*bands*multiplication()) \
        + fractional_domains*checks() \
        + OC_GRX(frames, framesamples, bands)


def OC_CRD(frames, framesamples, bands, num_neighbours):
    return (matrix_multiplication(num_neighbours, bands, bands, num_neighbours) + bands*addition() + matrix_inversion(bands) + 2* matrix_vector_multiplication(num_neighbours, bands)) + \
    frames*framesamples* (matrix_vector_multiplication(num_neighbours, bands) + bands * (subtraction() + distance(bands)) + \
    update_inversion_matrix(bands) + 2*matrix_vector_multiplication(num_neighbours, bands))

def OC_F_MGD(frames, framesamples, bands, kernel_element):
    return 20 * (kernel_element-1) + subtraction() + 8 + mean(bands) + frames*framesamples
    


