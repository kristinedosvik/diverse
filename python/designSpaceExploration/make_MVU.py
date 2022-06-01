import matplotlib.pyplot as plt
import math as math
from binning import *
from compression import *
from dimensionalREduction import *
from georeferencing_and_geometricRegistration import *
from pixelMitigation import *
from smileAndKeystone import *
from targetDetection import *


def make_SVU(svu_graph, svu_sample):
    
    #default value:
    svu_value = 0

    #Check if svu sample is infeasible:
    if ((svu_sample < svu_graph[0][0] and svu_graph[0][1]==0) or (svu_sample > svu_graph[len(svu_graph)-1][0] and svu_graph[len(svu_graph)-1][1]==0)):
        print("infeasable sample ", svu_sample)
        return -1

    #check if svu sample is perfectly satifiable:
    elif (svu_sample <= svu_graph[0][0] and svu_graph[0][1]==1):
        svu_value = 1
    elif (svu_sample >= svu_graph[len(svu_graph)-1][0] and svu_graph[len(svu_graph)-1][1]==1):
        svu_value = 1

    else:
        #make svu values:
        for i in range(1, len(svu_graph)): #skal ikke denne først sjekke 40 så 60?
            if(svu_sample < svu_graph[i][0] and svu_sample >= svu_graph[i-1][0]):
                a = (svu_graph[i][1] - svu_graph[i-1][1])/(svu_graph[i][0] - svu_graph[i-1][0])
                svu_value = a*svu_sample + svu_graph[i-1][1] - a*svu_graph[i-1][0]
                
    return svu_value


def make_MVU(svu_graphs, weights, sample, check_sensibility):

    outputted_data_size = sample[1]
    accuracy = sample[2]

    svu_outputted_data_size = make_SVU(svu_graphs[0], outputted_data_size)
    svu_accuracy = make_SVU(svu_graphs[1], accuracy)
    mvu = svu_outputted_data_size*weights[0] + svu_accuracy*weights[1]

    if (check_sensibility==1):
        print("sample: ", sample)
        print("svu_outputted_data_size: ", svu_outputted_data_size)
        print("svu_accuracy: ", svu_accuracy)
        print("mvu: ", mvu)
        print()
    
    return mvu

def plot_MVUs(svu_graphs, weights, samples, g0, g1, g2):
    x = []
    y = []
    for i in range(0, len(samples)):
        x.append(samples[i][3])       
        mvu = make_MVU(svu_graphs, weights, samples[i], 0)
        y.append(mvu)

    plt.plot(x, y, "o")
    addSampleLabels(samples, svu_graphs, weights, g0, g1, g2)
    
    plt.show()

def plot_color_by_design(svu_graphs, weights, samples, group_nr, group, group_colors, g0, g1, g2):
    
    plot_group = []
    for i in range(0, len(group)):
        plot_group.append([])


    for i in range(0, len(samples)):
        cost = samples[i][3]  
        mvu = make_MVU(svu_graphs, weights, samples[i], 0)
        sample = [cost, mvu]

        algorithm_nr = group.index(samples[i][0][group_nr])
        plot_group[algorithm_nr].append(sample)
    
    for i in range(0, len(group)):

        x = [row[0] for row in plot_group[i]]
        y = [row[1] for row in plot_group[i]]
        plt.plot(x, y, "o", color = group_colors[i])

    addSampleLabels(samples, svu_graphs, weights, g0, g1, g2)
    plt.show()

def make_3D_plot(pipelines, frames_vec, frame_samples_vec, bands_vec, binning_factor_vec, dimRed_bands_vec, svu_graphs, weights, group_colors, g0, g1, g2):

    sample_groups = []
    for i in range(0, len(frames_vec)):
        sample_groups.append([])
    
    #samples in same columns have the same input sizes, while the row have the same pipeline configuration
    for p in range(0, len(pipelines)):
        for v in range(0, len(frames_vec)):
            sample = create_sample_by_pipeline(pipelines[p], frames_vec[v], frame_samples_vec[v], bands_vec[v], binning_factor_vec[v], dimRed_bands_vec[v])
            sample_groups[v].append(sample)

    #make plot:

    #varying inputs, same pipeline
    x = []
    y = []
    for p in range(0, len(pipelines)):
        for v in range(0, len(frames_vec)):
            mvu = make_MVU(svu_graphs, weights, sample_groups[v][p], 0)
            y.append(mvu)
            cost = sample_groups[v][p][3]
            x.append(cost)
        plt.plot(x, y, color="black")
        x.clear()
        y.clear()


    #same inputs, varying pipelines
    x = []
    y = []
    for v in range(0, len(frames_vec)):
        for p in range(0, len(pipelines)):
            mvu = make_MVU(svu_graphs, weights, sample_groups[v][p], 0)
            y.append(mvu)
            cost = sample_groups[v][p][3]
            x.append(cost)
        plt.plot(x, y, "o", color=group_colors[v])
        x.clear()
        y.clear()

    #samples = [row[0] for row in sample_groups]
    samples = sample_groups[0]
    addSampleLabels(samples, svu_graphs, weights, g0, g1, g2)
    plt.show()
    print("Finished 3D plot")

def addSampleLabels(samples, svu_graphs, weights, g0, g1, g2):
    
    mvus = []
    costs = []
    for i in range(0, len(samples)):
        mvu = make_MVU(svu_graphs, weights, samples[i], 0)
        mvus.append(mvu)
        costs.append(samples[i][3])

    i = 0
    for x,y in zip(costs, mvus):
        index_name = create_index_name(samples[i], g0, g1, g2)

        label = f"{index_name}"

        plt.annotate(label, # this is the text
                     (x,y), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     color="black",
                     ha='center') # horizontal alignment can be left, right or center
        i+=1


def create_index_name(sample, g0, g1, g2):
    name = ""
    name += str(g0.index(sample[0][0]))
    name += str(g1.index(sample[0][1]))
    name += str(g2.index(sample[0][2]))
    return name

def find_pipeline_from_index_name(index_name, g0, g1, g2):
    return g0[int(index_name[0])] + ", " + g1[int(index_name[1])] + ", " + g2[int(index_name[2])] + "."


###################################################


def g11_algorithm(algorithm, frames, frame_samples, bands, accuracy, binning_factor):
    if (algorithm == "spectral_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spectral_binning(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_spectral_binning(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g12_algorithm(algorithm, frames, frame_samples, bands, accuracy, binning_factor):
    if (algorithm == "spatial_binning"):
        new_frames, new_frame_samples, new_bands = DOS_spatial_binning(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_spatial_binning(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g21_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "thumbnails"):
        new_frames, new_frame_samples, new_bands = DOS_thumbnails(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_thumbnails(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g22_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "subsamples"):
        new_frames, new_frame_samples, new_bands = DOS_subsamples(frames, framesamples, bands, binningfactor)
        accuracy = 1
        cost = OC_subsamples(frames, framesamples, bands, binningfactor)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g31_algorithm(algorithm_detection, algorithm_correction, frames, frame_samples, bands, accuracy, bad_samples, neigbourlevel, cardinal):
        new_frames, new_frame_samples, new_bands = DOS_pixel_mitigation(frames, framesamples, bands, binningfactor, num_regions)
    
    #detection:
    if (algorithm_detection == "statisical_threshold_detection"):
        accuracy = 1
        cost = OC_statisical_threshold_detection(frames, framesamples, bands, num_regions)
    elif(algorithm_detection == "correlation_detection"):
        accuracy = 1
        cost = OC_correlation_detection(frames, framesamples, bands, num_regions)

    #correction:
    if (algorithm_detection == "avaraging_twice_correction"):
        accuracy = 1
        cost = OC_avaraging_twice_correction(bad_samples, bands)
    elif(algorithm_detection == "nearest_neighbour_correction"):
        accuracy = 1
        cost = OC_nearest_neighbour_correction(bad_samples, bands)
    elif(algorithm_detection == "mean_correction"):
        accuracy = 1
        cost = OC_mean_correction(bad_samples, neigbourlevel, cardinal)
    elif(algorithm_detection == "median_correction"):
        accuracy = 1
        cost = OC_median_correction(bad_samples, neigbourlevel, cardinal)


    elif (algorithm_detection == "x" or algorithm_correction == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)
    
    #correction:


    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g32_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "smile_and_keystone"):
        new_frames, new_frame_samples, new_bands = DOS_smile_and_keystone(frames, framesamples, bands)
        accuracy = 1
        cost = OC_smile_and_keystone(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g33_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "radiometric_calibration"):
        new_frames, new_frame_samples, new_bands = DOS_radiometric_calibration(frames, framesamples, bands)
        accuracy = 1
        cost = OC_radiometric_calibration(frames, framesamples, bands)


    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g41_algorithm(algorithm, frames, frame_samples, bands, accuracy, reducedbands, iterations):
        
    new_frames, new_frame_samples, new_bands = DOS_dimensional_reduction(frames, framesamples, bands)
    
    if (algorithm == "PCA_sw"):
        accuracy = 1
        cost = OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "PCA_hw"):
        accuracy = 1
        cost = OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "MNF"):
        accuracy = 1
        cost = OC_MNF(frames, framesamples, bands, reducedbands, iterations)
    elif (algorithm == "ICA"):
        accuracy = 1
        cost = OC_ICA(frames, framesamples, bands, reducedbands, iterations)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def g51_algorithm(algorithm, frames, frame_samples, bands, accuracy, resolution_increase):
    if (algorithm == "georeferencing"):
        new_frames, new_frame_samples, new_bands = DOS_georeferencing(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands)
    if (algorithm == "geometric_registration"):
        new_frames, new_frame_samples, new_bands = DOS_geometric_registration(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands) + OC_geometric_registration(frames, framesamples, bands, resolution_increse)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy


def gLast_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    
    #target detection:
    if (algorithm == "georeferencing"):
        new_frames, new_frame_samples, new_bands = DOS_georeferencing(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands)
    if (algorithm == "geometric_registration"):
        new_frames, new_frame_samples, new_bands = DOS_geometric_registration(frames, framesamples, bands)
        accuracy = 1
        cost = OC_georeferencing(frames, framesamples, bands) + OC_geometric_registration(frames, framesamples, bands, resolution_increse)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy

########################################

def create_sample_by_pipeline(pipeline, frames, frame_samples, bands, binning_factor, dimRed_bands):
    cost = 0
    accuracy = 1
    
    cost_group, frames, frame_sample, bands, accuracy = g0_algorithm(pipeline[0], frames, frame_samples, bands, accuracy, binning_factor)
    cost += cost_group
    
    cost_group, frames, frame_sample, bands, accuracy = g1_algorithm(pipeline[1], frames, frame_samples, bands, accuracy, dimRed_bands)
    cost += cost_group
    
    cost_group, frames, frame_sample, bands, accuracy = g2_algorithm(pipeline[2], frames, frame_samples, bands, accuracy)
    cost += cost_group

    return [pipeline, frames*frame_sample*bands, accuracy, cost] 

#print(create_sample_by_pipeline(["binning", "dimRed_pca", "tarDet"], 100, 80, 200, 4, 12))

########################################

def create_pipelines(g0, g1, g2):
    pipelines = []
    for i0 in range(0, len(g0)):
        for i1 in range(0, len(g1)):
            for i2 in range(0, len(g2)):
                pipelines.append([g0[i0], g1[i1], g2[i2]])
    return pipelines

########################################

def create_svu_outputted_data_size_graph(frames, frame_samples, bands):
    _2D = frames*frame_samples
    raw = frames*frame_samples*bands
    graph = [[_2D,1], [_2D*3, 0.9], [raw/2, 0.2], [raw, 0]]
    return graph

########################################




def main():

    frames = 10
    frame_samples = 16
    bands = 20
    binning_factor = 2
    dimRed_bands = 7

    g0 = ["binning", "x"]
    g1 = ["dimRed_pca", "dimRed_enm", "x"]
    g2 = ["tarDet", "anomDet", "x"]

    svu_outputted_data_size_graph = create_svu_outputted_data_size_graph(frames, frame_samples, bands)
    svu_accuracy_graph = [[0.4,0],[0.7,0.5],[1,1]]

    svu_graphs = [svu_outputted_data_size_graph, svu_accuracy_graph]
    weights = [0.3, 0.7]


    group_colors = ["red", "yellow", "green", "blue", "pink", "grey", "purple", "brown", "black", "lime"]

    #Pipeline:
    pipelines = create_pipelines(g0, g1, g2)
    print("Pipelines:\n", pipelines)

    #Samples:
    samples = []
    for i in range(0, len(pipelines)):
        samples.append(create_sample_by_pipeline(pipelines[i], frames, frame_samples, bands, binning_factor, dimRed_bands))
    print("Samples:\n", samples)

    #Check sensibility of MVU and SVU scores:
    check_sensibility = 1
    for i in range(0, len(samples)):
        make_MVU(svu_graphs, weights, samples[i], check_sensibility)
    
    #plots 2D:
    plot_MVUs(svu_graphs, weights, samples, g0, g1, g2)
    plot_color_by_design(svu_graphs, weights, samples, 0, g0, group_colors, g0, g1, g2)
    plot_color_by_design(svu_graphs, weights, samples, 1, g1, group_colors, g0, g1, g2)
    plot_color_by_design(svu_graphs, weights, samples, 2, g2, group_colors, g0, g1, g2)

    frames_vec = [10, 10, 10, 10, 10] 
    frame_samples_vec = [16, 16, 16, 16, 16] 
    bands_vec = [20, 30, 40, 50, 60]
    binning_factor_vec = [2, 2, 2, 2, 2]
    dimRed_bands_vec = [7, 7, 7, 7, 7]
    
    frames_vec = [10, 20, 30, 40, 50] 
    frame_samples_vec = [16, 16, 16, 16, 16] 
    bands_vec = [20, 20, 20, 20, 20]
    binning_factor_vec = [2, 2, 2, 2, 2]
    dimRed_bands_vec = [7, 7, 7, 7, 7]

    frames_vec = [10, 10, 10, 10, 10] 
    frame_samples_vec = [10, 20, 30, 40, 50] 
    bands_vec = [20, 20, 20, 20, 20]
    binning_factor_vec = [2, 2, 2, 2, 2]
    dimRed_bands_vec = [7, 7, 7, 7, 7]

    #plots 3D:
    make_3D_plot(pipelines, frames_vec, frame_samples_vec, bands_vec, binning_factor_vec, dimRed_bands_vec, svu_graphs, weights, group_colors, g0, g1, g2)

    #Check sample names:
    sample_index_name = "021"
    print(sample_index_name, " = ", find_pipeline_from_index_name(sample_index_name, g0, g1, g2))

#####################################################

main()

    





