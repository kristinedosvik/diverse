from OC_utility import *

def DOS_georeferencing(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def DOS_geometric_registration(frames, framesamples, bands, frame_increase_factor, framesample_increase_factor):
    new_frames = frames * frame_increase_factor
    new_frame_samples = framesamples * framesample_increase_factor
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def OC_georeferencing(frames, framesamples, bands): #include binary search maybe ?
    return frames * framesamples * bands * ( \
    + 7 * (4 * subtraction() + 2 * multiplication() + addition()) \
    + 2 * addition() + 2 * trignomitry() + 3 * multiplication() + subtraction() \
    + 2 * multiplication() \
    + 3 * ( 6 * multiplication() + 4 * shift() + 3 * subtraction() + addition()) \
    + 2 * trignomitry() + 2 * shift() + division() + subtraction() + multiplication() \
    + 3 * multiplication() + 3 * addition() \
    + 4 * multiplication() + 2 * addition() + subtraction() \
    + 4 * multiplication() + 2 * addition() + subtraction() + shift() \
    + 5 * multiplication() + 2 * addition() + subtraction() + subtraction() \
    + 3 * multiplication() + addition() + subtraction() + multiplication() + division() + trignomitry() \
    + division() + trignomitry() \
    + 5 * trignomitry() + 4 * multiplication() + 3 * (division() + sqrt() + subtraction() + 2 * multiplication() + trignomitry()) +
    + subtraction() + multiplication() + division() \
    + 3 * addition() + multiplication())

def OC_geometric_registration(frames, framesamples, bands, frame_increase_factor, framesample_increase_factor):
    opt_iteration = 4
    optimization_ = optimization(opt_iteration, 10, 3) #10 er objective funksjonen som er i likningen allerede,
    return frames * framesamples * bands * ( \
    2 * (multiplication() + subtraction()) \
    + 5 * multiplication() + sqrt() + division() + 2 * round_down() \
    + 2 * subtraction() + division() \
    + bands * (5 * subtraction() + 3 * addition() + 4 * multiplication())) \
    + frames * framesamples * (2 * multiplication() + 2 * division() + 2 * addition()) \
    + optimization_ * (2 * subtraction() + 2 * absolute_value() + 2 * multiplication() + 5 * addition() + 12 * multiplication()) 

    
