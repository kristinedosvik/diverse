from OC_utility import *

def DOS_dimensional_reduction(frames, framesamples, bands, reducedbands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = reducedbands
    return new_frames, new_frame_samples, new_bands

def OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations):
    return correlation_matrix(frames*framesamples, bands) + jacobi_algorithm_sw(bands, iterations) #+ bands * iteration() + matrix_multiplication(reducedbands, bands, bands, frames * framesamples)
    

def OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations):
    return correlation_matrix_hw(frames*framesamples, bands) + jacobi_algorithm_hw(bands, iterations) + bands * iteration() + matrix_multiplication_hw(reducedbands, bands, bands, frames * framesamples)
   
def OC_MNF(frames, framesamples, bands, reducedbands, iterations):
    return frames * framesamples * bands * subtraction() \
    + correlation_matrix(frames*framesamples, bands) \
    + SUV(bands, bands, "jacobi", iterations) \
    + bands * (sqrt() + division()) \
    + matrix_multiplication(bands, bands, bands, bands) \
    + matrix_multiplication(frames*framesamples, bands, bands, bands) \
    + SUV(frames*framesamples, bands, "arnoldi", iterations) \
    + 2 * matrix_multiplication(bands, bands, bands, bands) \
    + matrix_multiplication(reducedbands, bands, bands, frames*framesamples) 

#def OC_ICA(frames, framesamples, bands, reducedbands):
#    return ..


