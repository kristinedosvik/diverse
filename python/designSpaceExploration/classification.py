from OC_utility import *


def DOS_classification(frames, framesamples, bands, num_classes):
    new_frames = frames
    new_frame_samples = framesamples
    new_bands = 1
    return new_frames, new_frame_samples, new_bands


def OC_SVM(frames, framesamples, bands, num_classes, total_num_support_vectors):
    return frames*framesamples*(num_classes**2/2-num_classes/2*(total_num_support_vectors/num_classes*2 * (2 * multiplication() + addition() + exp() + multiplication() + distance(bands) - sqrt())) + (num_classes-1)*addition() + (num_classes-1)*compare())
