from OC_utility import *

def DOS_dimensional_reduction(frames, framesamples, bands, reducedbands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = reducedbands
    return new_frames, new_frame_samples, new_bands

def OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations):
    return correlation_matrix(frames*framesamples, bands) + qr_eigen_vec_val(bands, iterations) \
    + sorting(bands) + matrix_multiplication(reducedbands, bands, bands, frames*framesamples)
    
def OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations, dot_product_blocks):
    return correlation_matrix_hw(frames*framesamples, bands, dot_product_blocks) + jacobi_algorithm_hw(bands, iterations, dot_product_blocks) + sorting_hw(bands) + matrix_multiplication_hw(reducedbands, bands, bands, frames*framesamples, dot_product_blocks)
   
def OC_MNF(frames, framesamples, bands, reducedbands, iterations):
    nois_matrix = frames*framesamples*bands*subtraction()
    correlation_matrix_noise = correlation_matrix(frames*framesamples, bands)
    eigen_vecs = qr_eigen_vec_val(bands, iterations)
    correlation_matrix_adjusted = 2*matrix_multiplication(bands,bands,bands,bands)

    return OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations) + nois_matrix + correlation_matrix_noise + eigen_vecs + correlation_matrix_adjusted

    #return frames*framesamples*bands*subtraction() + SUV(frames*framesamples, bands, iterations) + SUV(bands, bands, iterations) + bands*sqrt() + diagonal_matrix_multiplication(bands) + matrix_multiplication(frames*framesamples, bands, bands, bands) + matrix_multiplication(bands, bands, bands, bands) + matrix_multiplication(reducedbands, bands, bands, frames*framesamples)

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
    c20 = 20
    c15 = 15
    c10 = 10
    c5 = 5
    c2 = 2
    
    if (reducedbands > c20):
        return 0.9653
    elif(reducedbands > c15):
        return 0.9652
    elif(reducedbands > c20):
        return 0.9651
    elif(reducedbands > c5):
        return 0.96
    elif(reducedbands > c2):
        return 0.925
    else:
        return 0

def A_MNF(bands, reducedbands):
    #based on 1752x3325x144 image, with 144 bands
    c20 = 20
    c15 = 15
    c10 = 10
    c5 = 5
    c2 = 2
    
    if (reducedbands > c20):
        return 0.9653
    elif(reducedbands > c15):
        return 0.9652
    elif(reducedbands > c20):
        return 0.965
    elif(reducedbands > c5):
        return 0.94
    elif(reducedbands > c2):
        return 0.924
    else:
        return 2

def A_ICA(bands, reducedbands):
    #based on 1752x3325x144 image, with 144 bands
    c20 = 20
    c15 = 15
    c10 = 10
    c5 = 5
    c2 = 2

    if (reducedbands > c20):
        return 0.951
    elif(reducedbands > c15):
        return 0.95
    elif(reducedbands > c20):
        return 0.9351
    elif(reducedbands > c5):
        return 0.934
    elif(reducedbands > c2):
        return 0.93
    else:
        return 4


