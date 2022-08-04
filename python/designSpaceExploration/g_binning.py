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
    return (2*simd() * np.floor(bands/binningfactor)*np.floor(binningfactor/4) + (np.floor(binningfactor/4)+binningfactor%4)*addition()*np.floor(bands/binningfactor) + (bands%binningfactor-1)*addition())*frames*framesamples/frames


def OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin):
    if(whatToBin == "frames"):
        return ((division() + (binningfactor-1) * addition()) * bands * np.floor(frames/binningfactor) + (division() + (frames%binningfactor - 1)*addition())*bands)*framesamples
    else:
        return ((division() + (binningfactor-1) * addition()) * bands * np.floor(framesamples/binningfactor) + (division() + (framesamples%binningfactor - 1)*addition())*bands)*frames


def resolution_estimation(graph, sample):
    
    val = 1

    for i in range(1, len(graph)): #skal ikke denne først sjekke 40 så 60?
        if(sample < graph[i][0] and sample >= graph[i-1][0]):
            a = (graph[i][1] - graph[i-1][1])/(graph[i][0] - graph[i-1][0])
            val = a*sample + graph[i-1][1] - a*graph[i-1][0]
        
    if(sample > graph[-1][0]):
        val = 0
    val

    return val


def snr_of_binning(b):    
    return 120*np.log(b)+110

#import matplotlib.pyplot as plt
def binning_accuracy(binningfactor, spec_or_spat):
    #snr, binningfactor
    x = []
    y = []
    for i in range(, 30):
        x.append(i)
        y.append(snr_of_binning(i))


    #resolution, accuracy
    graph_res_dec = [[0,1],[1,1],[2,0.90],[3,0.80],[4,0.60],[5,0.30],[5,0.01],[6,0],[30,0]]
    x_ = [row[0] for row in graph_res_dec]
    y_ = [row[1] for row in graph_res_dec]
    #plt.plot(x_, y_, color = "grey")
    #plt.savefig("binning_res.png")
    #plt.show()



    x_tot = []
    y_tot = []

    w_snr = 0.0004
    w_res = 1

    #spat:
    graph_binning_acc_spat = [[0,1]]

    for i in range(1,30):
        res = resolution_estimation(graph_res_dec, i)
        y_tot = w_snr*snr_of_binning(i) + w_res*res
        graph_binning_acc_spat.append([i,y_tot])

    x_spat = [row[0] for row in graph_binning_acc_spat]
    y_spat = [row[1] for row in graph_binning_acc_spat]    
    #plt.plot(x_spat, y_spat, color = "grey")
    #plt.savefig("binning_res_snr_spat.png")
    #plt.show()

    #spec:
    graph_binning_acc_spec = [[0,1]]

    for i in range(1,30):
        res = resolution_estimation(graph_res_dec, i)
        y_tot = w_snr*snr_of_binning(i) + w_res*res
        graph_binning_acc_spec.append([i*9,y_tot])

    x_spec = [row[0] for row in graph_binning_acc_spec]
    y_spec = [row[1] for row in graph_binning_acc_spec]    
    #plt.plot(x_spec, y_spec, color = "grey")
    #plt.savefig("binning_res_snr_spec.png")
    #plt.show()

    if (spec_or_spat == "spec"):
        return resolution_estimation(graph_binning_acc_spec, binningfactor)
    else:
        return resolution_estimation(graph_binning_acc, binningfactor)



def A_spectral_binning(bands, binningfactor, camera_linse_binning):
    return binning_accuracy(binningfactor, "spec")


def A_spatial_binning(frames, framesamples, binningfactor, whatToBin):
    return binning_accuracy(binningfactor, "spat")