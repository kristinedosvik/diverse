import matplotlib.pyplot as plt

from binning import *
from compression import *
from dimensionalReduction import *
from processingGroups import *
from data_inputs import *



group_colors = ["red", "yellow", "green", "blue", "pink", "grey", "purple", "brown", "darkgrey", "lime", "black", "cyan", "magenta", "tan", "maroon"]





def pipeline_ccsds123_b1_hw(i, spec_vec, spat_vec, dimRed_vec):
    return [spec_vec[i], spat_vec[i], "x", "x", "x", "x", "x", dimRed_vec[i], "x", "CCSDS123_B1_hw"]

def pipeline_ccsds123_b1_sw(i, spec_vec, spat_vec, dimRed_vec):
    return [spec_vec[i], spat_vec[i], "x", "x", "x", "x", "x", dimRed_vec[i], "x", "CCSDS123_B1_sw"]

def pipeline_ccsds123_b2_hw(i, spec_vec, spat_vec, dimRed_vec):
    return [spec_vec[i], spat_vec[i], "x", "x", "x", "x", "x", dimRed_vec[i], "x", "CCSDS123_B2_hw"]

def pipeline_ccsds123_b2_sw(i, spec_vec, spat_vec, dimRed_vec):
    return [spec_vec[i], spat_vec[i], "x", "x", "x", "x", "x", dimRed_vec[i], "x", "CCSDS123_B2_sw"]

def pipeline_name(sample):
    name = ""
    temp = sample[0][0]
    if(temp != "x"):
        name += temp + " "
    temp = sample[0][1]
    if(temp != "x"):
        name += temp + " "
    temp = sample[0][4]
    if(temp != "x"):
        name += temp + " "
    temp = sample[0][5]
    if(temp != "x"):
        name += temp + " "
    temp = sample[0][6]
    if(temp != "x"):
        name += temp + " "
    temp = sample[0][7]
    if(temp != "x"):
        name += temp + " "
    temp = sample[0][8]
    if(temp != "x"):
        name += temp + " "
    
    name += "CCSDS123"
    return name


def make_3D_plot_compression(frames_vec, frame_samples_vec, bands_vec, spec_binning_factor_vec, spat_binning_factor_vec, dimRed_bands_vec, spec_vec, spat_vec, dimRed_vec):

	#make num 3D groups:
    pipeline_name_vec = []
    samples_ccsds123_b1_hw = []
    samples_ccsds123_b1_sw = []
    samples_ccsds123_b2_hw = []
    samples_ccsds123_b2_sw = []
    for i in range(0, len(frames_vec)):
        b1_hw = create_sample_by_pipeline(pipeline_ccsds123_b1_hw(i, spec_vec, spat_vec, dimRed_vec), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, dimRed_bands_vec[i], dot_product_blocks, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors)
        b1_sw = create_sample_by_pipeline(pipeline_ccsds123_b1_sw(i, spec_vec, spat_vec, dimRed_vec), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, dimRed_bands_vec[i], dot_product_blocks, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors)
        b2_hw = create_sample_by_pipeline(pipeline_ccsds123_b2_hw(i, spec_vec, spat_vec, dimRed_vec), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, dimRed_bands_vec[i], dot_product_blocks, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors)
        b2_sw = create_sample_by_pipeline(pipeline_ccsds123_b2_sw(i, spec_vec, spat_vec, dimRed_vec), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, dimRed_bands_vec[i], dot_product_blocks, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors)
        
        pipeline_name_vec.append(pipeline_name(b1_hw))

        samples_ccsds123_b1_hw.append(b1_hw)
        samples_ccsds123_b1_sw.append(b1_sw)
        samples_ccsds123_b2_hw.append(b2_hw)
        samples_ccsds123_b2_sw.append(b2_sw)

        print("b1_hw, ", b1_hw[3])
        print("b1_sw, ", b1_sw[3])
        print("b2_hw, ", b2_hw[3])
        print("b2_sw, ",b2_sw[3])
        
        #return [pipeline, frames*frame_sample*bands, accuracy, cost]
    #make plot:

    #varying inputs, same pipeline
    #1)
    x = []
    y = []
    compression_names = ["b1_hw", "b1_sw", "b2_hw", "b2_sw"]
    for i in range(0, len(frames_vec)):
        score = samples_ccsds123_b1_hw[i][2]
        cost = samples_ccsds123_b1_hw[i][3]
        y.append(score)
        x.append(cost)
        plt.text(0, 0.8-i/100, pipeline_name_vec[i], color = group_colors[i])
    plt.plot(x, y, color="grey")
    x.clear()
    y.clear()

    #2)
    for i in range(0, len(frames_vec)):
        score = samples_ccsds123_b1_sw[i][2]
        cost = samples_ccsds123_b1_sw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="grey")
    x.clear()
    y.clear()

    #3)
    for i in range(0, len(frames_vec)):
        score = samples_ccsds123_b2_hw[i][2]
        cost = samples_ccsds123_b2_hw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="grey")
    x.clear()
    y.clear()

    #4)
    for i in range(0, len(frames_vec)):
        score = samples_ccsds123_b2_sw[i][2]
        cost = samples_ccsds123_b2_sw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="grey")
    x.clear()
    y.clear()


    #same inputs, varying pipelines

    for i in range(0, len(frames_vec)):
        y.append(samples_ccsds123_b1_hw[i][2])
        y.append(samples_ccsds123_b1_sw[i][2])
        y.append(samples_ccsds123_b2_hw[i][2])
        y.append(samples_ccsds123_b2_sw[i][2])

        x.append(samples_ccsds123_b1_hw[i][3])
        x.append(samples_ccsds123_b1_sw[i][3])
        x.append(samples_ccsds123_b2_hw[i][3])
        x.append(samples_ccsds123_b2_sw[i][3])            
    
        plt.plot(x, y, "o", color=group_colors[i])
        x.clear()
        y.clear()

    plt.annotate(compression_names[0], (samples_ccsds123_b1_hw[0][3], samples_ccsds123_b1_hw[0][2]), textcoords="offset points", xytext=(0,10), color="grey", ha='center')
    plt.annotate(compression_names[1], (samples_ccsds123_b1_sw[0][3], samples_ccsds123_b1_sw[0][2]), textcoords="offset points", xytext=(0,10), color="grey", ha='center')
    plt.annotate(compression_names[2], (samples_ccsds123_b2_hw[0][3], samples_ccsds123_b2_hw[0][2]), textcoords="offset points", xytext=(0,10), color="grey", ha='center')
    plt.annotate(compression_names[3], (samples_ccsds123_b2_sw[0][3], samples_ccsds123_b2_sw[0][2]), textcoords="offset points", xytext=(0,10), color="grey", ha='center')
    plt.show()

    print("finito")
    


print(make_3D_plot_compression(frames_vec, frame_samples_vec, bands_vec, spec_binning_factor_vec, spat_binning_factor_vec, dimRed_bands_vec, spec_vec, spat_vec, dimRed_vec))

