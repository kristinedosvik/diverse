from OC_utility import *

def DOS_pixel_mitigation(frames, framesamples, bands):
    new_frames = frame
    new_frame_samples = frame_samples
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def OC_statisical_threshold_detection(frames, framesamples, bands, num_regions):
    return bands * num_regions * (variance (frames*framesamples/regions ) + multiplication() + frames * framesamples / regions * iteration())
    
def OC_correlation_detection(frames, framesamples, bands, num_neighbours):
    return frames * framesamples * bands * (correlation_matrix(num_neighbours) + num_neighbours * iteration())

def OC_avaraging_twice_correction(bands):
    return bands * (4 * (mean(3) + divisio() + subtraction()) + mean(4))

def OC_nearest_neighbour_correction(bands):
    return bands * copy_element()

def OC_mean_correction(neigbourlevel, cardinal):
    if (neighbourlevel == 1):
        if (cardinal == 1):
            return mean(4)
        return mean(8)
    elif (neighbourlevel == 2):
        if (cardinal == 1):
            return mean(8)
        return mean(16)
    if (cardinal == 1):
        return mean(12)
    return mean(24)

def OC_median_correction(neigbourlevel, cardinal):
    if (neighbourlevel == 1):
        if (cardinal == 1):
            return median(4)
        return median(8)
    elif (neighbourlevel == 2):
        if (cardinal == 1):
            return median(8)
        return median(16)
    if (cardinal == 1):
        return median(12)
    return median(24)


