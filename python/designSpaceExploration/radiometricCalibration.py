from OC_utility import *


def DOS_radiometricCalibration(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = bands
    return new_frames, new_frame_samples, new_bands


#Formel:
#calibrated pixel = [rå_pixel - dark_pixel]*rad_coeff/exp
def OC_radiometricCalibration(frames, framesamples, bands):
	return frames*framesamples*bands*(subtraction() + multiplication() + division())
