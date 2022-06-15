from OC_utility import *

def DOS_dimensional_reduction(frames, framesamples, bands, reducedbands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = reducedbands
    return new_frames, new_frame_samples, new_bands

def OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations):
    #print("SW:")
    #print("frames: ", frames)
    #print("framesamples: ", framesamples)
    #print("bands: ", bands)
    #print("correlation_matrix: ", correlation_matrix(frames*framesamples, bands))
    #print("J SW pca:")
    #print("jacobi_algorithm_sw: ", jacobi_algorithm_sw(bands, iterations))
    #print("sorting: ", sorting(bands))
    #print("matrix_multiplication: ", matrix_multiplication(reducedbands, bands, bands, frames*framesamples))
    return correlation_matrix(frames*framesamples, bands) + jacobi_algorithm_sw(bands, iterations) + sorting(bands) + matrix_multiplication(reducedbands, bands, bands, frames*framesamples)
    
def OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations, dot_product_blocks):
    #print("HW:")
    #print("frames: ", frames)
    #print("framesamples: ", framesamples)
    #print("bands: ", bands)
    #print("correlation_matrix_hw: ", correlation_matrix_hw(frames*framesamples, bands, dot_product_blocks))
    #print("jacobi_algorithm_hw: ", jacobi_algorithm_hw(bands, iterations, dot_product_blocks))
    #print("sorting_hw: ", sorting_hw(bands))
    #print("matrix_multiplication_hw: ", matrix_multiplication_hw(reducedbands, bands, bands, frames*framesamples, dot_product_blocks))
    print("OC_PCA, ", correlation_matrix_hw(frames*framesamples, bands, dot_product_blocks) + jacobi_algorithm_hw(bands, iterations, dot_product_blocks) + sorting_hw(bands) + matrix_multiplication_hw(reducedbands, bands, bands, frames*framesamples, dot_product_blocks))
    return correlation_matrix_hw(frames*framesamples, bands, dot_product_blocks) + jacobi_algorithm_hw(bands, iterations, dot_product_blocks) + sorting_hw(bands) + matrix_multiplication_hw(reducedbands, bands, bands, frames*framesamples, dot_product_blocks)
   
def OC_MNF(frames, framesamples, bands, reducedbands, iterations):
    return frames*framesamples*bands*subtraction() + SUV(frames*framesamples, bands, iterations) + SUV(bands, bands, iterations) + bands*sqrt() + diagonal_matrix_multiplication(bands) + matrix_multiplication(frames*framesamples, bands, bands, bands) + matrix_multiplication(bands, bands, bands, bands) + matrix_multiplication(reducedbands, bands, bands, frames*framesamples)

def OC_ICA(frames, framesamples, bands, reducedbands, iterations):
    return correlation_matrix(frames*framesamples, bands) \
    + matrix_inversion(bands) \
    + matrix_multiplication(frames*framesamples, bands, bands, bands) \
    + reducedbands * iterations * ( \
    frames*framesamples * (dot_product(bands) + trignomitry() + subtraction() + (2 * bands + 1) * multiplication() ) + 2 * bands * division() + bands * subtraction() \
    + 2 * dot_product(bands) + bands * subtraction()
    + bands * multiplication() + bands * addition() + sqrt() + bands * division()) \
    + matrix_multiplication(frames*framesamples, bands, bands, reducedbands) \
     
def A_PCA(bands, reducedbands):
    #based on 1752x3325x144 image, with 144 bands
    c20 = 20/144
    c15 = 15/144
    c10 = 10/144
    c5 = 5/144
    c2 = 2/144
    
    if (reducedbands/bands > c20):
        return 0.9653
    elif(reducedbands/bands > c15):
        return 0.9652
    elif(reducedbands/bands > c20):
        return 0.9651
    elif(reducedbands/bands > c5):
        return 0.96
    elif(reducedbands/bands > c2):
        return 0.925
    else:
        return 0

def A_MNF(bands, reducedbands):
    #based on 1752x3325x144 image, with 144 bands
    c20 = 20/144
    c15 = 15/144
    c10 = 10/144
    c5 = 5/144
    c2 = 2/144
    
    if (reducedbands/bands > c20):
        return 0.9653
    elif(reducedbands/bands > c15):
        return 0.9652
    elif(reducedbands/bands > c20):
        return 0.965
    elif(reducedbands/bands > c5):
        return 0.94
    elif(reducedbands/bands > c2):
        return 0.924
    else:
        return 0

def A_ICA(bands, reducedbands):
    #based on 1752x3325x144 image, with 144 bands
    c20 = 20/144
    c15 = 15/144
    c10 = 10/144
    c5 = 5/144
    c2 = 2/144
    
    if (reducedbands/bands > c20):
        return 0.951
    elif(reducedbands/bands > c15):
        return 0.95
    elif(reducedbands/bands > c20):
        return 0.9351
    elif(reducedbands/bands > c5):
        return 0.934
    elif(reducedbands/bands > c2):
        return 0.93
    else:
        return 0


