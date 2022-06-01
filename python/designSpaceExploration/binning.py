import numpy as np
from OC_utility import *

def DOS_spectral_binning(frames, framesamples, bands, binningfactor):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = np.ceil(bands/binningfactor)
    return new_frames, new_frame_samples, new_bands

def DOS_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin):
    if(whatToBin == "frames"):
        new_frames = np.ceil(frames/binningfactor)
        new_frame_samples = framesamples
    else:
        new_frames = frames
        new_frame_samples = np.ceil(framesamples/binningfactor)

    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def OC_spectral_binning(frames, framesamples, bands, binningfactor):
    return frames * (framesamples * find_index() + 
            framesamples * ((np.floor(bands/binningfactor) * (vpaddle_4_2() + vpaddle_2_1()) + binningfactor%4 * addition()) + bands%binningfactor * addition()))

def OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin):
    if(whatToBin == "frames"):
        return framesamples * (np.floor(frames/binningfactor) * binningfactor * bands * addition() + (frames % binningfactor) * bands * addition())
    else:
        return fames * (np.floor(framesamples/binningfactor) * binningfactor * bands * addition() + (framesamples % binningfactor) * bands * addition())

