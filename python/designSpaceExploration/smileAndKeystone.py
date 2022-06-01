from OC_utility import *

def OC_smile_and_keystone(frames, framesamples, bands):
    x_and_y = 16 * multiplication() + 10 * addition()
    dx_dy = 2 * subtraction() 
    weights = 4 * multiplication() + 4 * subtraction()
    weighted_sum = bands * (4 * multiplication() + 3 * addition())
    
    #print("frames: ",frames,  "\nframesamples: ", framesamples, "\nbands: ", bands)
    #print("OC snk: ", frames * framesamples * (x_and_y + dx_dy + weights + weighted_sum))

    return frames * framesamples * (x_and_y + dx_dy + weights + weighted_sum)

def DOS_smile_and_keystone(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

