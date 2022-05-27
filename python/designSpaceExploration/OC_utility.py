import math as math
import numpy as np

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

def round_down():
    return 1

def round_up():
    return 1

def find_index():
    return multiplication() + addition()

def vpaddle_4_2():
    return 1

def vpaddle_2_1():
    return 1

def sqrt():
    return 1

def median(size):
    return sorting(size) + division()

def absolute_value():
return 1

def minimum():
    return 1

def mod():
    return -1

def sign():
    return 1

def checks():
    return 1

def trignomitry():
    return 1

##################
## SW functions ##
##################

def optimization(estimate):
    return -1

def binarysearch(size):
    return np.log2(size) * (shift() + checks())

def sorting(size):
    #quicksort:
    return -1

def arnold(size, iterations):
    return 1

def SUV(nr_rows, nr_coloumns, algorithm, iterations):
    matrixes = matrix_multiplication(nr_rows, nr_columns, nr_columns, nr_rows) + matrix_multiplication(nr_columns, nr_rows, nr_rows, nr_columns)
    if (algorithm == "jacobi"):
        return matrixes + jacobi(nr_rows, iterations) + jacobi(nr_columns, iterations)
    else:
        return matrixes + arnold(nr_rows, iterations) + jacobi(nr_columns, iterations)

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

def matrix_multiplication(nr_rows_m1, nr_coloumns_m1, nr_rows_m2, nr_coloumns_m2):
    if (nr_columns_m1 != nr_rows_m2):
        print("Matrix multiplication error: n1xm1 * n2xm2, where m1 != n2")
        return -1
    else:
        return nr_rows_m1*nr_columns_m2*dot_product(nr_coloumns_m1)

def jacobi_algorithm_sw(matrix_size, iterations):
    trignometry = 4*multiplication() + subtraction + 3*division() + 3*addition() + 2*sqrt()
    return iterations * ((matrix_size-1) * (3 matrix_multiplications(matrix_size, matrix_size, matrix_size, matrix_size) + matrix_size/2*trignometry))

def singular_value_decomposition(nr_rows, nr_coloumns, iterations):
    ATA = matrix_multiplication(nr_rows, nr_coloumns, nr_columns, nr_rows)
    AAT = matrix_multiplication(nr_coloumns, nr_rows, nr_rows, nr_columns)
    
def mean(samples):
    return samples * division() + (samples-1) * additions()

def variance(samples):
    return samples * mean(samples) + subtraction + mean(samples)


##################
## HW functions ##
##################

def dot_product_hw(size):
    return multiplication() + np.ceil(math.log2(size))

def matrix_multiplication_hw(nr_rows_m1, nr_coloumns_m1, nr_rows_m2, nr_coloumns_m2):
    if (nr_columns_m1 != nr_rows_m2):
        print("Matrix multiplication error: n1xm1 * n2xm2, where m1 != n2")
        return -1
    else:
        return nr_rows_m1*nr_columns_m2*dot_product_hw(nr_coloumns_m1)

def jacobi_algorithm_sw(matrix_size, iterations):
    trignometry = 4*multiplication() + 3*division() + 3*addition() + 2*sqrt()
    return iterations * ((matrix_size-1) * (3 matrix_multiplications_hw(matrix_size, matrix_size, matrix_size, matrix_size) + trignometry))


def add_sample_to_correlation_matrix_hw(bands):
    return bands * (multiplication() + division() + addition())

def correlation_matrix_hw(frames, framesample, bands):
    return frames * framesamples * add_sample_to_correlation_matrix_hw(bands)
