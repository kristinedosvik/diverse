from OC_utility import *

def DOS_CCSDS123_B1(frames, framesamples, bands):
    new_frames = frames
    new_frame_samples = framesamples/2 #2.5
    new_bands = bands
    return new_frames, new_frame_samples, new_bands

def DOS_CCSDS123_B2(frames, framesamples, bands, absolute_error_value):
    
    a = (165 - 0)/(1024 - 0)
    CR = a*absolute_error_value
    
    new_frames = frames
    new_frame_samples = framesamples/CR
    new_bands = bands

    return new_frames, new_frame_samples, new_bands


ccsds123_graph = [[0,1], [128,0.9], [256, 0.1], [1024, 0]]
def ccsds123_b2_accuracy_estimation(graph, sample):
    val = 1

    for i in range(1, len(graph)): #skal ikke denne først sjekke 40 så 60?
        if(sample < graph[i][0] and sample >= graph[i-1][0]):
            a = (graph[i][1] - graph[i-1][1])/(graph[i][0] - graph[i-1][0])
            val = a*sample + graph[i-1][1] - a*graph[i-1][0]
        
    if(sample > graph[-1][0]):
        val = 0
    
    return val

def A_CCSDS123_B2(absolute_error_value):
    return ccsds123_b2_accuracy_estimation(ccsds123_graph, absolute_error_value)



def OC_CCSDS123_B1_sw(frames, framesamples, bands, P, bit_resolution):
    return frames * framesamples * bands \
    * (absolute_value() + addition() + 2 * subtraction() + check() \
    + subtraction() \
    + 3*addition() + 3*multiplication() + clip() + division() + round_down()\
    + 3*addition() + 4*subtraction() + 2*multiplication() + division() + round_down() + mod()\
    + dot_product(P+3) \
    + (multiplication() + subtraction()) * (P+3) \
    + 3*addition() \
    + clip() + addition() \
    + 3*multiplication() + addition() + shift() + sign() + division() + round_down() + subtraction()\
    + clip() + 3*addition() + round_down() + subtraction() + division()\
    + division() + round_down() + shift() + mod()\
    + (2*division() + addition() + multiplication() + round_down())*bit_resolution*checks()\
    + division() + addition() + round_down()\
    + division() + 2*addition() + round_down() \
    )
    
def OC_CCSDS123_B1_hw(frames, framesamples, bands, P, D):
    return frames * framesamples * bands + 12 + np.log2(P) + 1


def OC_CCSDS123_B2_sw(frames, framesamples, bands, P, D):
    return OC_CCSDS123_B1_sw(frames, framesamples, bands, P, D) \
    + frames * framesamples * bands * ( \
    (sign() + 2*multiplication() + absolute_value() + 2*addition() + division() + round_down()) + \
    (absolute_value() + 4*addition() + 2*subtraction() + multiplication() + 2*round_down() + checks()) + \
    (absolute_value() + multiplication() + division() + round_down() + checks()) + \
    (addition() + division() + round_down()) + \
    (8*multiplication() + 3*subtraction() + 3*addition() + sign() + division() + round_down()) + \
    (2*addition() + 2*multiplication() + clip()))

def OC_CCSDS123_B2_hw(frames, framesamples, bands, P, D):
    return frames * framesamples * bands * 7 + 13



