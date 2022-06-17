import math as math
import numpy as np


def addition():
    return 1

def subtraction():
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

def sqrt():
    return 1

def median(size):
    return sorting(size) + division()

def absolute_value():
    return 1

def mod():
    return 1

def sign():
    return 1

def checks():
    return 1

def check():
    return 1

def trignomitry():
    return 1

def shift():
    return 1

def simd():
    return 1

def compare():
    return 1

def exp():
    return 1

def log():
    return 1

def clip():
    return 1

def divide():
    return 1

##################
## SW functions ##
##################

def distance(num_elements):
    return num_elements*multiplication() + (num_elements-1)*subtraction() + sqrt()


def optimization(iteration, objective_function, dimension_parameter_space):
    return 5000 # no idea

def sorting(size):
    return size*np.log2(size) * (divide() + compare())

    
def update_inversion_matrix(bands):
    return bands**2 *multiplication() + 4*matrix_multiplication(bands, bands, bands, bands) + 2*matrix_vector_multiplication(bands, bands) + 2*dot_product(bands)+2*bands**2*division() + (2*bands+1)*subtraction() + addition()

def dot_product(vec_elements):
    return vec_elements*multiplication() + (vec_elements-1)*addition()

def correlation_matrix(samples, bands):
    return matrix_multiplication(samples, bands, bands, samples) + samples**2 * division()

def update_correlation_matrix(bands):
    return bands**2 * (multiplication()+addition())

def diagonal_matrix_multiplication(bands):
    return bands*bands*multiplication()

def matrix_inversion(size):
    return gaussian_row_echelon_form(size) + (size**2/2 + size/2) *copy_element() + 2*size*system_of_equations(size)

def matrix_vector_multiplication(row, coloumns):
    return matrix_multiplication(row, coloumns, coloumns, 1)

def gaussian_row_echelon_form(size):
    return size * division() + (size**2/2 + size/2) * subtraction()

def system_of_equations(size):
    return 2* (size * division() + (size**2/2 + size/2 + size) * subtraction())
    
def matrix_multiplication(nr_rows_m1, nr_coloumns_m1, nr_rows_m2, nr_coloumns_m2):
    #print(nr_rows_m1)
    #print(nr_coloumns_m1)
    #print(nr_rows_m2)
    #print(nr_coloumns_m2)
    #print(nr_rows_m1*nr_coloumns_m2)
    #print(dot_product(nr_rows_m2))
    return nr_rows_m1*nr_coloumns_m2*dot_product(nr_rows_m2)

def jacobi_algorithm_sw(matrix_size, extra_iterations):
    #print("J SW:")
    #print(matrix_multiplication(matrix_size, matrix_size, matrix_size, matrix_size))
    return matrix_size/2*(matrix_size-1)*(3*matrix_multiplication(matrix_size, matrix_size, matrix_size, matrix_size) + matrix_size/2*13) + extra_iterations*(3*matrix_multiplication(matrix_size, matrix_size, matrix_size, matrix_size) + matrix_size/2*13)

def SUV(nr_rows, nr_coloumns, extra_iterations):
    return matrix_multiplication(nr_rows, nr_coloumns, nr_coloumns, nr_rows) + matrix_multiplication(nr_coloumns, nr_rows, nr_rows, nr_coloumns) + jacobi_algorithm_sw(nr_coloumns, extra_iterations) + jacobi_algorithm_sw(nr_rows, extra_iterations) + nr_coloumns*sqrt()
    
def mean(samples):
    return samples * addition() + division()

def update_mean():
    return subtraction() + addition() + 2*division()

def variance(samples):
    return samples * (addition()+subtraction()+multiplication()) + division()


##################
## HW functions ##
##################

def dot_product_hw(vec_elements):
    return multiplication() + np.ceil(np.log2(vec_elements))*addition()

def sorting_hw(elements):
    return elements


def matrix_multiplication_hw(nr_rows_m1, nr_coloumns_m1, nr_rows_m2, nr_coloumns_m2, dot_product_blocks):
    return dot_product_hw(nr_rows_m2) + nr_rows_m1 * nr_coloumns_m2 / dot_product_blocks 

def jacobi_algorithm_hw(matrix_size, extra_iterations, dot_product_blocks):
    return matrix_size/2*(matrix_size-1)*(3*matrix_multiplication_hw(matrix_size, matrix_size, matrix_size, matrix_size, dot_product_blocks) + 12) + extra_iterations*(3*matrix_multiplication_hw(matrix_size, matrix_size, matrix_size, matrix_size, dot_product_blocks) + 12)

def correlation_matrix_hw(samples, bands, dot_product_blocks):
    return matrix_multiplication_hw(samples, bands, bands, samples, dot_product_blocks) + samples**2 * division()

