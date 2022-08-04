from OC_utility import *

def OC_smile_and_keystone(frames, framesamples, bands):
    return ((10*addition() + 16*multiplication()) + (4*subtraction() + 4*multiplication()) + (2*subtraction()) + (3*addition() + 4*multiplication())*bands)*frames*framesamples

def DOS_smile_and_keystone(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

