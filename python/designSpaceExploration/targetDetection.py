# 1) data output size: DOS
# 2) operation count: OC
# 3) accuracy: A

from OC_utility import *


def DOS_target_detection(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = 1
    return new_frames, new_frame_samples, new_bands

def OC_SAM(frames, framesamples, bands):
    return dot_product(bands) + frames * framesamples * (2 * dot_product(bands) + 2 * multiplication() + division())

def OC_CEM(frames, framesamples, bands):
    return correlation_matrix(frames * framesamples, bands) + quadratic_matrix_invertion(bands) + matrix_vector_multiplication(bands, bands) + dot_product(bands) + frames * framesamples * (dot_product(bands) + division())

def OC_ACE_R(frames, framesamples, bands):
    return correlation_matrix(frames * framesamples, bands) + quadratic_matrix_invertion(bands) + matrix_vector_multiplication(bands, bands) + dot_product(bands) + frames * framesamples * ( matrix_vector_multiplication(bands, bands) * 2 *  dot_product(bands) + 2 * multiplication() + division())

def OC_target_detection_hw(frames, framesamples, bands):
    return frames * framesamples * (3 * bands + division() + 3) + 2 * bands + division() + 3


