from statistics_of_array import *
import numpy as np

def make_mean_and_standard_deviation_samples(x, arr):
    
    mean, std_neg, std_pos = mean_and_standard_deviation(arr)
    
    mean_sample = [x, mean]
    std_neg_sample = [x, std_neg]
    std_pos_sample = [x, std_pos]
    
    return mean_sample, std_neg_sample, std_pos_sample

#arr = [1,2,3,3,3,4,5,6,6,6,6,7,8,]
#mean_sample, std_neg_sample, std_pos_sample = make_mean_and_standard_deviation_samples(3, arr)
#print(mean_sample)
#print(std_neg_sample)
#print(std_pos_sample)
