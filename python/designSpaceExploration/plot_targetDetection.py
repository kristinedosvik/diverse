import matplotlib.pyplot as plt

from binning import *
from targetDetection import *
from dimensionalReduction import *
from processingGroups import *



def RGB(red, green, blue):
	rgb = "#"
	if(red < 16):
		rgb += "0" + hex(red)[-1]
	else:
		rgb += hex(red)[-2] + hex(red)[-1]
	if(green < 16):
		rgb += "0" + hex(green)[-1]
	else:
		rgb += hex(green)[-2] + hex(green)[-1]
	if(blue < 16):
		rgb += "0" + hex(blue)[-1]
	else:
		rgb += hex(blue)[-2] + hex(blue)[-1]
	return rgb

group_colors = ["red", "yellow", "green", "blue", "pink", "grey", "purple", "brown", "black", "lime", "black", "cyan", "magenta", "tan", "maroon"]

dr1 =1/1000000
dr2 = 1/125000
download_rate = dr1
freq = 1/667000000
frames = 956
framesamples = 684
bands = 1080
binningfactor = 9
camera_linse_binning = -1
whatToBin = "frames"
num_regions = 80
bad_samples = 600
neigbourlevel = 2
cardinal = 1
reducedbands = 10
iterations = 2
frame_increase_factor = 2
framesample_increase_factor = 2
outer_window = 60
inner_window = 20
P = 12
D = 4

frames_vec = [956, 956, 956, 956, 956]
frame_samples_vec = [684, 684, 684, 684, 684]
bands_vec = [1080, 1080, 1080, 1080, 1080]
spec_binning_factor_vec = [9, 9, 9, 9, 9]
spat_binning_factor_vec = [9, 9, 9, 9, 9]
dimRed_bands_vec = [12, 12, 12, 12, 12]
spec_vec = ["x", "spectral_binning", "spectral_binning", "spectral_binning", "spectral_binning"]
spat_vec = ["x", "x", "x", "x", "spatial_binning"]
dimRed_vec = ["x", "x", "PCA_hw", "PCA_sw", "PCA_sw"]
snk_vec = ["x", "x", "smile_and_keystone", "smile_and_keystone", "smile_and_keystone"]
geo_ref_vec = ["x", "x", "x", "x", "geometric_registration"] #georeferencing - trengs ikke onboard uten geometric correction


bad_p_det_vec = ["x", "x", "x", "statisical_threshold_detection", "correlation_detection"]
bad_p_cor_vec = ["x", "x", "nearest_neighbour_correction", "mean_correction", "median_correction"]



def pipeline_sam_hw(i):
    return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "SAM_hw"]

def pipeline_sam_sw(i):
    return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "SAM_sw"]

def pipeline_cem_hw(i):
    return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "CEM_hw"]

def pipeline_cem_sw(i):
    return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "CEM_sw"]

def pipeline_ace_hw(i):
    return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "ACE_hw"]

def pipeline_ace_sw(i):
    return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "ACE_sw"]

def pipeline_asmf_hw(i):
    return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "ASMF_hw"]

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
    
    name += "target detection"
    return name


def make_3D_plot_targetDetection(pipelines, frames_vec, frame_samples_vec, bands_vec, spec_binning_factor_vec, spat_binning_factor_vec, dimRed_bands_vec, spec_vec, spat_vec):

	#make num 3D groups:
    pipeline_name_vec = []
    samples_sam_hw = []
    samples_sam_sw = []
    samples_cem_hw = []
    samples_cem_sw = []
    samples_ace_hw = []
    samples_ace_sw = []
    samples_asmf_hw = []

    for i in range(0, len(frames_vec)):
        sam_hw = create_sample_by_pipeline(pipeline_sam_hw(i), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        sam_sw = create_sample_by_pipeline(pipeline_sam_sw(i), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        cem_hw = create_sample_by_pipeline(pipeline_cem_hw(i), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        cem_sw = create_sample_by_pipeline(pipeline_cem_sw(i), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        ace_hw = create_sample_by_pipeline(pipeline_ace_hw(i), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        ace_sw = create_sample_by_pipeline(pipeline_ace_sw(i), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        asmf_hw = create_sample_by_pipeline(pipeline_asmf_hw(i), frames_vec[i], frame_samples_vec[i], bands_vec[i], spec_binning_factor_vec[i], camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D)
        pipeline_name_vec.append(pipeline_name(sam_hw))
        samples_sam_hw.append(sam_hw)
        samples_sam_sw.append(sam_sw)
        samples_cem_hw.append(cem_hw)
        samples_cem_sw.append(cem_sw)
        samples_ace_hw.append(ace_hw)
        samples_ace_sw.append(ace_sw)
        samples_asmf_hw.append(asmf_hw)

        #return [pipeline, frames*frame_sample*bands, accuracy, cost]
    #make plot:

    #varying inputs, same pipeline
    #1)
    x = []
    y = []
    targetDetection_names = ["sam_hw", "sam_sw", "cem_hw", "cem_sw", "ace_hw", "ace_sw", "asmf_hw"]
    for i in range(0, len(frames_vec)):
        score = samples_sam_hw[i][2]
        cost = samples_sam_hw[i][3]
        y.append(score)
        x.append(cost)
        plt.text(0, 0.8-i/100, pipeline_name_vec[i], color = group_colors[i])
    plt.plot(x, y, color="black")
    x.clear()
    y.clear()

    #2)
    for i in range(0, len(frames_vec)):
        score = samples_sam_sw[i][2]
        cost = samples_sam_sw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="black")
    x.clear()
    y.clear()

    #3)
    for i in range(0, len(frames_vec)):
        score = samples_cem_hw[i][2]
        cost = samples_cem_hw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="black")
    x.clear()
    y.clear()

    #4)
    for i in range(0, len(frames_vec)):
        score = samples_cem_sw[i][2]
        cost = samples_cem_sw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="black")
    x.clear()
    y.clear()

    #5)
    for i in range(0, len(frames_vec)):
        score = samples_ace_hw[i][2]
        cost = samples_ace_hw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="black")
    x.clear()
    y.clear()

    #6)
    for i in range(0, len(frames_vec)):
        score = samples_ace_sw[i][2]
        cost = samples_ace_sw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="black")
    x.clear()
    y.clear()

    #7)
    for i in range(0, len(frames_vec)):
        score = samples_asmf_hw[i][2]
        cost = samples_asmf_hw[i][3]
        y.append(score)
        x.append(cost)
    plt.plot(x, y, color="black")
    x.clear()
    y.clear()


    #same inputs, varying pipelines

    for i in range(0, len(frames_vec)):
        y.append(samples_sam_hw[i][2])
        y.append(samples_sam_sw[i][2])
        y.append(samples_cem_hw[i][2])
        y.append(samples_cem_sw[i][2])
        y.append(samples_ace_hw[i][2])
        y.append(samples_ace_sw[i][2])
        y.append(samples_asmf_hw[i][2])
        
        x.append(samples_sam_hw[i][3])
        x.append(samples_sam_sw[i][3])
        x.append(samples_cem_hw[i][3])
        x.append(samples_cem_sw[i][3])
        x.append(samples_ace_hw[i][3])
        x.append(samples_ace_sw[i][3])
        x.append(samples_asmf_hw[i][3])

        plt.plot(x, y, "o", color=group_colors[i])
        x.clear()
        y.clear()

    plt.annotate(targetDetection_names[0], (samples_sam_hw[0][3], samples_sam_hw[0][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
    plt.annotate(targetDetection_names[1], (samples_sam_sw[0][3], samples_sam_sw[0][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
    plt.annotate(targetDetection_names[2], (samples_cem_hw[0][3], samples_cem_hw[0][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
    plt.annotate(targetDetection_names[3], (samples_cem_sw[0][3], samples_cem_sw[0][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
    plt.annotate(targetDetection_names[4], (samples_ace_hw[0][3], samples_ace_hw[0][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
    plt.annotate(targetDetection_names[5], (samples_ace_sw[0][3], samples_ace_sw[0][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
    plt.annotate(targetDetection_names[6], (samples_asmf_hw[0][3], samples_asmf_hw[0][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')

    plt.show()

    print("finito")
    

print(make_3D_plot_targetDetection(frames_vec, frame_samples_vec, bands_vec, spec_binning_factor_vec, spat_binning_factor_vec, dimRed_bands_vec, spec_vec, spat_vec, dimRed_vec))
