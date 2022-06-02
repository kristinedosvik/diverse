import matplotlib.pyplot as plt
import math as math
from processingGroups import *

group_colors = ["red", "yellow", "green", "blue", "pink", "grey", "purple", "brown", "black", "lime", "black", "cyan", "magenta", "tan", "maroon"]

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
        print("cost: ", sample[3])
        print()
    
    return mvu

def plot_MVUs(svu_graphs_points, weights, samples, g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast):
    x = []
    y = []
    for i in range(0, len(samples)):
        x.append(samples[i][3])       
        mvu = make_MVU(svu_graphs_points, weights, samples[i], 0)
        y.append(mvu)

    plt.plot(x, y, "o")
    #addSampleLabels(samples, svu_graphs_points, weights, g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast)
    
    plt.show()

def plot_color_by_design(svu_graphs, weights, samples, group_nr, group):

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

    #addSampleLabels(samples, svu_graphs, weights, g0, g1, g2)
    plt.show()


def plot_color_by_design_svu(samples, group_nr, group, axes):
    plot_group = []
    for i in range(0, len(group)):
        plot_group.append([])


    for i in range(0, len(samples)):
        cost = samples[i][2] 
        svu = samples[i][1]
        sample = [cost, svu]

        algorithm_nr = group.index(samples[i][0][group_nr])
        plot_group[algorithm_nr].append(sample)
    
    for i in range(0, len(group)):

        x = [row[0] for row in plot_group[i]]
        y = [row[1] for row in plot_group[i]]
        plt.xlim([0,100000000000])
        axes[group_nr].plot(x, y, "o", color = group_colors[i])

    #addSampleLabels(samples, svu_graphs, weights, g0, g1, g2) 
    

def make_3D_plot(pipelines, frames_vec, frame_samples_vec, bands_vec, binning_factor_vec, dimRed_bands_vec, svu_graphs, weights):

    sample_groups = []
    for i in range(0, len(frames_vec)):
        sample_groups.append([])
    
    #samples in same columns have the same input sizes, while the row have the same pipeline configuration
    for p in range(0, len(pipelines)):
        for v in range(0, len(frames_vec)):
            sample = create_sample_by_pipeline(pipelines[p], frames_vec[v], frame_samples_vec[v], bands_vec[v], binning_factor_vec[v], dimRed_bands_vec[v]) #must change this one!
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
    plt.show()
    print("Finished 3D plot")

def addSampleLabels(samples, svu_graphs, weights, g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast):
    
    mvus = []
    costs = []
    for i in range(0, len(samples)):
        mvu = make_MVU(svu_graphs, weights, samples[i], 0)
        mvus.append(mvu)
        costs.append(samples[i][3])

    i = 0
    for x,y in zip(costs, mvus):
        index_name = create_index_name(samples[i], g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast)

        label = f"{index_name}"

        plt.annotate(label, # this is the text
                     (x,y), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     color="black",
                     ha='center') # horizontal alignment can be left, right or center
        i+=1


def create_index_name(sample, g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast):
    name = ""
    name += str(g11.index(sample[0][0]))
    name += str(g12.index(sample[0][1]))
    name += str(g21.index(sample[0][2]))
    name += str(g22.index(sample[0][3]))
    name += str(g311.index(sample[0][4]))
    name += str(g312.index(sample[0][5]))
    name += str(g32.index(sample[0][6]))
    name += str(g41.index(sample[0][7]))
    name += str(g51.index(sample[0][8]))
    name += str(gLast.index(sample[0][9]))

    return name

def find_pipeline_from_index_name(index_name, g0, g1, g2):
    return g0[int(index_name[0])] + ", " + g1[int(index_name[1])] + ", " + g2[int(index_name[2])] + "."


########################################

def create_sample_by_pipeline(pipeline, frames, frame_samples, bands, binning_factor, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D):
    cost = 0
    accuracy = 0.8
    
    cost_group, frames, frame_sample, bands, accuracy_group = g11_algorithm(pipeline[0], frames, frame_samples, bands, accuracy, binning_factor)
    cost += cost_group
    accuracy *= accuracy_group
    
    cost_group, frames, frame_sample, bands, accuracy_group = g12_algorithm(pipeline[1], frames, frame_samples, bands, accuracy, binning_factor, whatToBin)
    cost += cost_group
    accuracy *= accuracy_group

    cost_group, frames, frame_sample, bands, accuracy_group = g21_algorithm(pipeline[2], frames, frame_samples, bands, accuracy)
    cost += cost_group
    accuracy *= accuracy_group

    cost_group, frames, frame_sample, bands, accuracy_group = g22_algorithm(pipeline[3], frames, frame_samples, bands, accuracy)
    cost += cost_group
    accuracy *= accuracy_group

    cost_group, frames, frame_sample, bands, accuracy_group = g31_algorithm(pipeline[4], pipeline[5], frames, frame_samples, bands, accuracy, num_regions, bad_samples, neigbourlevel, cardinal)
    cost += cost_group
    accuracy *= accuracy_group
  
    cost_group, frames, frame_sample, bands, accuracy_group = g32_algorithm(pipeline[6], frames, frame_samples, bands, accuracy)
    cost += cost_group
    accuracy *= accuracy_group

    cost_group, frames, frame_sample, bands, accuracy_group = g41_algorithm(pipeline[7], frames, frame_samples, bands, accuracy, reducedbands, iterations)
    cost += cost_group
    accuracy *= accuracy_group
    
    cost_group, frames, frame_sample, bands, accuracy_group = g51_algorithm(pipeline[8], frames, frame_samples, bands, accuracy, frame_increase_factor, framesample_increase_factor)
    cost += cost_group
    accuracy *= accuracy_group

    cost_group, frames, frame_sample, bands, accuracy_group = gLast_algorithm(pipeline[9], frames, frame_samples, bands, accuracy, outer_window, inner_window, P, D)
    cost += cost_group
    accuracy *= accuracy_group


    return [pipeline, frames*frame_sample*bands, accuracy, cost] 

#print(create_sample_by_pipeline(["binning", "dimRed_pca", "tarDet"], 100, 80, 200, 4, 12))

########################################

def create_pipelines(g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast):
    pipelines = []
    for i11 in range(0, len(g11)):
        for i12 in range(0, len(g12)):
            for i21 in range(0, len(g21)):
                for i22 in range(0, len(g22)):
                    for i311 in range(0, len(g311)):
                        for i312 in range(0, len(g312)):
                            for i32 in range(0, len(g32)):
                                for i41 in range(0, len(g41)):
                                    for i51 in range(0, len(g51)):
                                        for iLast in range(0, len(gLast)):
                                            pipelines.append([g11[i11], g12[i12], g21[i21], g22[i22], g311[i311], g312[i312], g32[i32], g41[i41], g51[i51], gLast[iLast]])
    return pipelines

########################################

def create_svu_predefined_graph_points_outputted_data_size(frames, frame_samples, bands):
    _2D = frames*frame_samples
    raw = frames*frame_samples*bands
    graph = [[_2D,1], [_2D*3, 0.9], [raw/2, 0.2], [raw*10, 0]]
    return graph

########################################



g11 = ["x", "spectral_binning"]
g12 = ["x", "spatial_binning"]

g21 = ["x"]#, "thumbnails"]
g22 = ["x"]#, "subsamples"]

g311 = ["x", "statisical_threshold_detection", "correlation_detection"]
g312 = ["x", "avaraging_twice_correction", "nearest_neighbour_correction", "mean_correction", "median_correction"]

g32 = ["x", "smile_and_keystone"]

g41 = ["x", "PCA_sw", "PCA_hw", "MNF"]
g51 = ["x", "georeferencing", "geometric_registration"]
gLast = ["x", "SAM", "CEM", "ACE_R", "target_detection_hw","GRX_R","LRX", "DWRX", "CCSDS123_B1_sw", "CCSDS123_B1_hw","CCSDS123_B2_sw", "CCSDS123_B2_hw"]


download_rate = 1
frames = 200
frame_samples = 680
bands = 1080
binning_factor = 9
whatToBin = "frames" 
num_regions = 80 
bad_samples = 600 
neigbourlevel = 2
cardinal = 1 
reducedbands = 20 
iterations = 2 
frame_increase_factor = 2 
framesample_increase_factor = 2
outer_window = 60 
inner_window = 20 
P = 12 
D = 4

def mainSVU():


    #Pipeline:
    pipelines = create_pipelines(g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast)

    #Samples:
    samples_ = []
    for i in range(0, len(pipelines)):
        s = create_sample_by_pipeline(pipelines[i], frames, frame_samples, bands, binning_factor, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        s_ = [s[0], s[2], s[3] + s[1]*download_rate]
        samples_.append(s_)
        #print("sample: ", s_)
        #print("svu_accuracy: ", s_[1])
        #print("cost: ", s_[2])
        #print()

    
    x_cost = [row[2] for row in samples_]
    y_accuracy = [row[1] for row in samples_]
   
    #plots 2D:
    plt.plot(x_cost, y_accuracy, "o")
    plt.show()

    #color by design
    fig,axes = plt.subplots(10, 1)
    plot_color_by_design_svu(samples_, 0, g11, axes)
    plot_color_by_design_svu(samples_, 1, g12, axes)
    plot_color_by_design_svu(samples_, 2, g21, axes)
    plot_color_by_design_svu(samples_, 3, g22, axes)
    plot_color_by_design_svu(samples_, 4, g311, axes)
    plot_color_by_design_svu(samples_, 5, g312, axes)
    plot_color_by_design_svu(samples_, 6, g32, axes)
    plot_color_by_design_svu(samples_, 7, g41, axes)
    plot_color_by_design_svu(samples_, 8, g51, axes)
    plot_color_by_design_svu(samples_, 9, gLast, axes)
    plt.show()


def mainMVU():


    #svu settings:    
    svu_predefined_graph_points_outputted_data_size = create_svu_predefined_graph_points_outputted_data_size(frames, frame_samples, bands)
    svu_predefined_graph_points_accuracy = [[0.4,0],[0.7,0.5],[1,1]]

    svu_graphs_points = [svu_predefined_graph_points_outputted_data_size, svu_predefined_graph_points_accuracy]
    weights = [0.3, 0.7]


    #Pipeline:
    pipelines = create_pipelines(g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast)

    #Samples:
    samples = []
    for i in range(0, len(pipelines)):
        s = create_sample_by_pipeline(pipelines[i], frames, frame_samples, bands, binning_factor, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        samples.append(s)

    #Check sensibility of MVU and SVU scores:
    #check_sensibility = 1
    #for i in range(0, len(samples)):
        #make_MVU(svu_graphs_points, weights, samples[i], check_sensibility)
    
    #plots 2D:
    plot_MVUs(svu_graphs_points, weights, samples, g11, g12, g21, g22, g311, g312, g32, g41, g51, gLast)

    
    plot_color_by_design(svu_graphs_points, weights, samples, 0, g11)
    plot_color_by_design(svu_graphs_points, weights, samples, 9, gLast)
    plot_color_by_design(svu_graphs_points, weights, samples, 7, g41)

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
    #sample_index_name = "021"
    #print(sample_index_name, " = ", find_pipeline_from_index_name(sample_index_name, g0, g1, g2))

#mainMVU()
mainSVU()

