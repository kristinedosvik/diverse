

def addition():
    return 1

def multiplication():
    return 1

def division():
    return 1

def iteration():
    return 1

def insertion():
    return 1

def copy_element():
    return 1

###############

def swap():
    return 3*insertion()

def dot_product(vec_elements):
    return vec_elements*(vec_elements-1)

def add_sample_to_correlation_matrix(bands):
    return (bands * bands/2 + bands/2) *  (multiplication() + division() + addition()) + (bands * bands/2 - bands/2)

def correlation_matrix(frames, framesample, bands):
    frames * framesamples * add_sample_to_correlation_matrix(bands)

def quadratic_matrix_invertion(size):
    return size*size/2+size/2 * insertion() + size*size/2+size/2 * iteration() + (size-1) * size * swap() + gaussian_elimination(size) + size*size/2-size/2 * insertion() + size * 2 * matrix_vector_equation(size)

def matrix_vector_multiplication(row, columns):
    return row*dot_product(columns)

def gaussian_elimination(size):
    return size * (division() + multiplication()) + size*size/2-size/2 * size * (multiplication() + subtraction())

def matrix_vector_equation(size):
    return 2 * gaussian_elimination(size) + 2 * size * (multiplication() + subtraction()) + size * division()



