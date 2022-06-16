from OC_utility import *

def DOS_pixel_mitigation(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def OC_statisical_threshold_detection(frames, framesamples, bands, num_neighbours):
    return ((division() + num_neighbours*subtraction() + num_neighbours*multiplication()) + (2*division() + addition() + subtraction()) + (multiplication() + compare() + addition() + subtraction()))*bands*frames*framesamples + (division() + num_neighbours * addition())*bands
    
def OC_correlation_detection(frames, framesamples, bands, num_neighbours):
    return frames*(framesamples*bands*correlation_matrix(num_neighbours+1, 25))
    #return correlation_matrix(num_neighbours, 25) + num_neighbours*check()*bands + (update_correlation_matrix(5) + checks())*bands*frames*framesamples

def OC_nearest_neighbour_correction(bad_samples):
    return bad_samples * copy_element()

def OC_mean_correction(bad_samples):
        return bad_samples * mean(8)

def OC_median_correction(bad_samples):
    return bad_samples * median(8)
    

