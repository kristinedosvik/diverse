import numpy as np
import statistics as st

def mean_and_standard_deviation(array):
    mean = np.mean(array)
    std = st.stdev(array)
    std_neg = mean - std
    std_pos = mean + std

    return mean, std_neg, std_pos

#arr = [1,2,5,5,5,6,7,7,7,10,11]
#print(mean_and_standard_deviation(arr))
