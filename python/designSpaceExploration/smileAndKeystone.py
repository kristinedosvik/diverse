from OC_utility import *

def OC_smile_and_keystone(frames, framesamples, bands):
    x_and_y = 16 * multiplication() + 10 * addition()
    dx_dy = 2 * subtraction() 
    weights = 4 multiplication() + 4 subtraction()
    weighted_sum = 2 multiplication() + 3 addition()
    return frames * framesamples * (x_and_y + dx_dy + weights + weighted_sum)

def DOS_smile_and_keystone(frames, framesamples, bands):
    new_frames = frame
    new_frame_samples = frame_samples
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

