from OC_utility import *

def DOS_dimensional_reduction(frames, framesamples, bands, reducedbands, iterations):
    new_frames = frame
    new_frame_samples = frame_samples
    new_bands = reducedbands
    return new_frames, new_frame_samples, new_bands

def OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations):
    return correlation_matrix(frames, framesamples, bands) + jacobi_algorithm_sw(bands, iterations) + bands * iteration() + matrix_multiplication(reducedbands, bands, bands, frames * framesamples)
    

def OC_PCA_hw(frames, framesamples, bands, reducedbands):
    return correlation_matrix_hw(frames, framesamples, bands) + jacobi_algorithm_hw(bands, iterations) + bands * iteration() + matrix_multiplication_hw(reducedbands, bands, bands, frames * framesamples)
   
def OC_MNF(frames, framesamples, bands, reducedbands):
    nois_samples = frames * framesamples * bands * subtraction()
    



