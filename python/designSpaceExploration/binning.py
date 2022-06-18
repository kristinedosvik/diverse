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
    return (2*simd() * np.floor(bands/binningfactor)*np.floor(binningfactor/4) + (np.floor(binningfactor/4)+binningfactor%4)*addition()*np.floor(bands/binningfactor) + (bands%binningfactor-1)*addition())*frames*framesamples


def OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin):
    if(whatToBin == "frames"):
        return ((division() + (binningfactor-1) * addition()) * bands * np.floor(frames/binningfactor) + (division() + (frames%binningfactor - 1)*addition())*bands)*framesamples
    else:
        return ((division() + (binningfactor-1) * addition()) * bands * np.floor(framesamples/binningfactor) + (division() + (framesamples%binningfactor - 1)*addition())*bands)*frames


def A_spectral_binning(bands, binningfactor, camera_linse_binning):
    return resolution_factor_spectral(bands, binningfactor, camera_linse_binning) * (1 + snr_factor_spectral(binningfactor)/10000)


def A_spatial_binning(frames, framesamples, binningfactor, whatToBin):
    return resolution_factor_spatial(frames, framesamples, binningfactor, whatToBin) * (1 + snr_factor_spatial(binningfactor)/100000)


def resolution_factor_spectral(bands, b, camera_linse_binning):
    if (camera_linse_binning != -1):
        #default:
        camera_linse_binning = 9
    
    a = (0-1)/(bands/camera_linse_binning - camera_linse_binning)
    x1 = 9
    y1 = 1
    y_ = a * (b- x1) + y1
    if(y_ > 1):
        return 1
    else:
        return y_

def snr_factor_spectral(b):    
    a = (150-45)/(18-1)
    x1 = 1
    y1 = 45
    y_ = a * (b- x1) + y1
    return y_


def resolution_factor_spatial(frames, framesamples, b, whatToBin):
    if(whatToBin == "frames"):
        a = (0-1)/(frames-0)
    else:
        a = (0-1)/(framesamples-0)
    x1 = 0
    y1 = 1
    y_ = a * (b- x1) + y1
    return y_

def snr_factor_spatial(b):    
    return 120*np.log(b)+110

