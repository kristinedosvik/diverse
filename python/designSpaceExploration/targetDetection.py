# 1) data output size: DOS
# 2) operation count: OC
# 3) accuracy: A

def DOS_target_detection(frames, framesamples, bands):
    new_frames = frame
    new_frame_samples = frame_samples
    new_bands = 1
    return new_frames, new_frame_samples, new_bands

def OC_SAM(frames, framesamples, bands):
    return dot_product(bands) + frames * framesamples * (2 * dot_product(bands) + 2 * multiplication() + division())

def OC_CEM(frames, framesamples, bands):
    return make_correlation_matrix(frames, framesamples, bands) + quadratic_matrix_invertion(bands) + matrix_vector_multiplication(bands, bands) + dot_product(bands) + frames * framesamples * (dot_product(bands) + division())

def OC_ACE_R(frames, framesamples, bands):
    return

def dot_product(vec_elements):
    return vec_elements*(vec_elements-1)

def add_sample_to_correlation_matrix(bands):
    return (bands * bands/2 + bands/2) *  (multiplication() + division() + addition()) + (bands * bands/2 - bands/2)

def make_correlation_matrix(frames, framesample, bands):
    frames * framesamples * add_sample_to_correlation_matrix(bands)
    
def copy_element()
    return 1

def addition()
    return 1

def multiplication()
    return 1

def division()
    return 1

def iteration()
    return 1

def insertion()
    return 1

def matrix_vector_multiplication(row, columns):
    return row*dot_product(columns)

def gaussian_elimination(size):
    return size * (division() + multiplication()) + size*size/2-size/2 * size * (multiplication() + subtraction())

def matrix_vector_equation(size):
    return 2 * gaussian_elimination(size) + 2 * size * (multiplication() + subtraction()) + size * division()

def swap()
    return 3*insertion()

def quadratic_matrix_invertion(size):
    return size*size/2+size/2 * insertion() + size*size/2+size/2 * iteration() + (size-1) * size * swap() + gaussian_elimination(size) + size*size/2-size/2 * insertion() + size * 2 * matrix_vector_equation(size)
