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
     

PCA_graph_1 = [[1,0.632], [2,0.90], [3,0.98], [5,0.99], [10,0.995], [16,0.999]]
PCA_graph_2 = [[1,0.903], [2,0.94], [3,0.98], [4,0.989], [5,0.992], [10,0.998], [24,0.999]]

def PCA_accuracy_estimation(graph, sample):
    val = 1

    for i in range(1, len(graph)): #skal ikke denne først sjekke 40 så 60?
        if(sample < graph[i][0] and sample >= graph[i-1][0]):
            a = (graph[i][1] - graph[i-1][1])/(graph[i][0] - graph[i-1][0])
            val = a*sample + graph[i-1][1] - a*graph[i-1][0]
        
    if(sample > graph[-1][0]):
        val = 0.999
    
    return val



def A_PCA(bands, reducedbands):
    a1 = PCA_accuracy_estimation(PCA_graph_1, reducedbands)
    a2 = PCA_accuracy_estimation(PCA_graph_2, reducedbands)
    return (a1+a2)/2


def A_MNF(bands, reducedbands):
    return A_PCA(bands, reducedbands)

def A_ICA(bands, reducedbands):
    return A_PCA(bands, reducedbands)*0.984

