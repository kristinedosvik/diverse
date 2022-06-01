from OC_utility import *

def DOS_CCSDS123_B1(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples/2.5
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def DOS_CCSDS123_B2(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples/15 #?
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def OC_CCSDS123_B1_sw(frames, framesamples, bands, P, D):
    return frames * framesamples * bands \
    * (absolute_value() + addition() \
    + 2 * subtraction() + minimum() \
    + subtraction() \
    + round_down() + division() \
    + 3 * addition() + 3 * shift() \
    + round_down() + 2 * addition() + 4 * shift() + subtraction() \
    + dot_product(P) + addition() + 2 * subtraction() + 2 * shift() + copy_element() + mod() \
    + 4 * addition() + P * (shift() + subtraction()) \
    + addition() \
    + round_down() + 2 * multiplication() + shift() + sign() \
    + 3 * addition() + round_down() + subtraction() + division() \
    +  shift() + subtraction() \
    + round_down() + 2 * shift() + mod() \
    + addition() + shift() + multiplication() + division() + D * shift() \
    + round_down() + addition() + shift() \
    + round_down() + 2 * addition() + shift())
    
def OC_CCSDS123_B1_hw(frames, framesamples, bands, P, D):
    return frames * framesamples * bands + 12 + np.log2(P) + 1


def OC_CCSDS123_B2_sw(frames, framesamples, bands, P, D):
    return OC_CCSDS123_B1_sw(frames, framesamples, bands, P, D) \
    + frames * framesamples * bands * ( \
    3 * (shift() + addition()) \
    + P * addition() \
    + 4 * addition() + 2 * division() \
    + round_down() + multiplication() + absolute_value() + shift() \
    + 2 * addition() + absolute_value() + shift() + sign() \
    + 7 * addition() + 6 * multiplication() + 6 * shift() + 4 * subtraction() \
    + shift() \
    + shift() + division())

def OC_CCSDS123_B2_hw(frames, framesamples, bands, P, D):
    return frames * framesamples * bands * 7 + 13



