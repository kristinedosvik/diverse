import matplotlib.pyplot as plt
import math as math

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

def plot_MVUs(svu_graphs, weights, samples):
    x = []
    y = []
    for i in range(0, len(samples)):
        x.append(samples[i][3])       
        mvu = make_MVU(svu_graphs, weights, samples[i], 0)
        y.append(mvu)
    plt.plot(x, y, "o")
    plt.show()

def plot_color_by_design(svu_graphs, weights, samples, group_nr, group, group_colors):
    
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
    plt.show()

###################################################


def binning_output_data_size(frames, frame_samples, bands, binning_factor):
    return frames, frame_samples, math.floor(bands/binning_factor)

def binning_accuracy(accuracy, bands, binning_factor):
    if (binning_factor > 10):
        return accuracy*0.90
    else:
        return accuracy*0.97

def binning_cost(frames, frame_samples, bands):
    return frame_samples*(frames/4*bands+bands*4)

##############

def dimRed_pca_output_data_size(frames, frame_samples, dimRed_bands):
    return frames, frame_samples, dimRed_bands

def dimRed_pca_accuracy(accuracy, bands, dimRed_bands):
    if (dimRed_bands > 12):
        return accurcy*0.95
    else:
        return accuracy*0.80

def dimRed_pca_cost(frames, frame_samples, bands, dimRed_bands):
    return frame_samples*(frames/4*7)+dimRed_bands*bands*frames

##############

def dimRed_enm_output_data_size(frames, frame_samples, dimRed_bands):
    return frames, frame_samples, dimRed_bands

def dimRed_enm_accuracy(accuracy, bands, dimRed_bands):
    if (dimRed_bands > 12):
        return accuracy*0.98
    else:
        return accuracy*0.85

def dimRed_enm_cost(frames, frame_samples, bands, dimRed_bands):
    return 2*(frame_samples*(frames/4*7)+dimRed_bands*bands*frames)

##############

def tarDet_output_data_size(frames, frame_samples):
    return frames, frame_samples, 1

def tarDet_accuracy(accuracy):
    return accuracy*0.96

def tarDet_cost(frames, frame_samples, bands):
    return frame_samples*frames*3*(frames/bands)

##############

def anomDet_output_data_size(frames, frame_samples):
    return frames, frame_samples, 1

def anomDet_accuracy(accuracy):
    return accuracy*0.92

def anomDet_cost(frames, frame_samples, bands):
    return frame_samples*frames*5*(frames/bands)/4

##############


#####################################################


def g0_algorithm(algorithm, frames, frame_samples, bands, accuracy, binning_factor):
    if (algorithm == "binning"):
        new_frames, new_frame_samples, new_bands = binning_output_data_size(frames, frame_samples, bands, binning_factor)
        accuracy = binning_accuracy(accuracy, bands, binning_factor)
        cost = binning_cost(frames, frame_samples, bands)

    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy
        

def g1_algorithm(algorithm, frames, frame_samples, bands, accuracy, dimRed_bands):
    if (algorithm == "dimRed_pca"):
        new_frames, new_frame_samples, new_bands = dimRed_pca_output_data_size(frames, frame_samples, dimRed_bands)
        accuracy = dimRed_pca_accuracy(accuracy, bands, dimRed_bands)
        cost = dimRed_pca_cost(frames, frame_samples, bands, dimRed_bands)

    elif (algorithm == "dimRed_enm"):
        new_frames, new_frame_samples, new_bands = dimRed_enm_output_data_size(frames, frame_samples, dimRed_bands)
        accuracy = dimRed_enm_accuracy(accuracy, bands, dimRed_bands)
        cost = dimRed_enm_cost(frames, frame_samples, bands, dimRed_bands)
    
    elif (algorithm == "x"):
        new_frame_samples = frame_samples
        new_frames = frames
        new_bands = bands
        new_accuracy = accuracy
        cost = 0

    else:
        print("Error", algorithm)

    return cost, new_frames, new_frame_samples, new_bands, accuracy

def g2_algorithm(algorithm, frames, frame_samples, bands, accuracy):
    if (algorithm == "tarDet"):
        new_frames, new_frame_samples, new_bands = tarDet_output_data_size(frames, frame_samples)
        accuracy = tarDet_accuracy(accuracy)
        cost = tarDet_cost(frames, frame_samples, bands)

    elif (algorithm == "anomDet"):
        new_frames, new_frame_samples, new_bands = anomDet_output_data_size(frames, frame_samples)
        accuracy = anomDet_accuracy(accuracy)
        cost = anomDet_cost(frames, frame_samples, bands)
    
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
    plot_MVUs(svu_graphs, weights, samples)
    plot_color_by_design(svu_graphs, weights, samples, 0, g0, group_colors)
    plot_color_by_design(svu_graphs, weights, samples, 1, g1, group_colors)
    plot_color_by_design(svu_graphs, weights, samples, 2, g2, group_colors)

    #plots 3D:


#####################################################

main()

    





