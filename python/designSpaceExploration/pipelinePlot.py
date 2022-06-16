import matplotlib.pyplot as plt
from processingGroups import *


def create_svu_predefined_graph_points_outputted_data_size(frames, framesamples, bands):
    _2D = frames*framesamples
    raw = frames*framesamples*bands
    graph = [[_2D,1], [_2D*3, 0.9], [raw/2, 0.1], [raw+3*_2D, 0]]
    return graph

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
dot_product_blocks = framesamples
kernel_element = 9
fractional_domains = 10
num_neighbours = 8
num_classes = 4 
total_num_support_vectors = 1096


#return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "GRX_sw"]
pipeline_sizes = 10
#p0 = ["spectral_binning", "spatial_binning", "x", "x", "OC_statisical_threshold_detection", "OC_median_correction", "smile_and_keystone", "MNF", "geometric_registration", "CCSDS123_B2_sw"]
p0 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

pNMF = ["x", "x", "x", "x", "x", "x", "x", "MNF", "x", "x"]

#compression pipelines:
p1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"]
p2 = ["spectral_binning", "spatial_binning", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"]

p3 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]
p4 = ["spectral_binning", "spatial_binning", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]

p5 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_sw"]
p6 = ["spectral_binning", "spatial_binning", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_sw"]

p7 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"]
p8 = ["spectral_binning", "spatial_binning", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"]

#Dim Red as compression
p9 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "x"]
p10 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]
p11 = ["spectral_binning", "spatial_binning", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]
p12 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]
p13 = ["spectral_binning", "spatial_binning", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]
p14 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "MNF", "x", "x"]

#Target Detection:
p15 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_sw"]
p16 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "SAM_sw"]
p17 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "SAM_sw"]
p18 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "SAM_sw"]

p19 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "SAM_sw"]
p20 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "geometric_registration", "SAM_sw"]
p21 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "SAM_sw"]

p15 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_hw"]
p16 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "SAM_hw"]
p17 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "SAM_hw"]
p18 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "SAM_hw"]

p19 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "SAM_hw"]
p20 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "geometric_registration", "SAM_hw"]
p21 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "SAM_hw"]

p15 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_hw"]
p16 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CEM_hw"]
p17 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CEM_hw"]
p18 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "CEM_hw"]

p19 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "CEM_hw"]
p20 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "geometric_registration", "CEM_hw"]
p21 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "CEM_hw"]

p22 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_sw"]
p23 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CEM_sw"]
p24 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CEM_sw"]
p25 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "CEM_sw"]

p26 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "CEM_sw"]
p27 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "geometric_registration", "CEM_sw"]
p28 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "CEM_sw"]

p29 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "ACE_hw"]
p30 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "ACE_hw"]
p31 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "ACE_hw"]
p32 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "ACE_hw"]

p33 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "ACE_hw"]
p34 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "geometric_registration", "ACE_hw"]
p35 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "ACE_hw"]

p36 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "ACE_sw"]
p37 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "ACE_sw"]
p38 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "ACE_sw"]
p39 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "ACE_sw"]

p40 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "ACE_sw"]
p41 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "geometric_registration", "ACE_sw"]
p42 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "ACE_sw"]

p43 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "ASMF_hw"]
p44 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "ASMF_hw"]
p45 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "ASMF_hw"]
p46 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "ASMF_hw"]

p47 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "ASMF_hw"]
p48 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "geometric_registration", "ASMF_hw"]
p49 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "ASMF_hw"]


#p0 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_sw", "x", "CCSDS123_B1_hw"]
#p1 = ["spectral_binning", "spatial_binning", "x", "x", "bad_p_det_vec", "bad_p_cor_vec", "smile_and_keystone", "MNF", "geometric_registration", "CCSDS123_B2_sw"]
#p2 = ["x", "spatial_binning", "x", "x", "x", "x", "x", "ICA", "x", "CCSDS123_B1_sw"]

pipeline_vec_all = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p3, p33, p34, p35, p36, p37, p38, p39, p40, p41, p4, p43, p44, p45, p46, p47, p48, p49]
pipeline_vec_compr = [pNMF, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]
pipeline_vec_tardet = [pNMF, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p3, p33, p34, p35, p36, p37, p38, p39, p40, p41, p4, p43, p44, p45, p46, p47, p48, p49]
pipeline_vec = pipeline_vec_tardet




#Make pipeline names in correct order:
def make_pipeline_names_in_pipeline_order(pipeline_vec, pipeline_sizes):
	names_pipelines_vec = []
	name = ""
	for j in range(0, len(pipeline_vec)):
		for i in range(0, pipeline_sizes):
			name = add_processingmodule_name_to_string(name, pipeline_vec[j][i])
		
		names_pipelines_vec.append(name[:len(name)-1])
		name = ""
	return names_pipelines_vec


print(make_pipeline_names_in_pipeline_order(pipeline_vec, pipeline_sizes))


def make_pipeline_plot(pipeline_vec):
	#Make samples from pipelines:
	samples = []
	for i in range(0, len(pipeline_vec)):
		sample = create_sample_by_pipeline(pipeline_vec[i], frames, framesamples, bands, binningfactor, camera_linse_binning, whatToBin, num_regions, bad_samples, neigbourlevel, cardinal, reducedbands, dot_product_blocks, iterations, frame_increase_factor, framesample_increase_factor, outer_window, inner_window, P, D, kernel_element, fractional_domains, num_neighbours, num_classes, total_num_support_vectors)
		#[pipeline, frames*frame_sample*bands, accuracy, cost]
		#print(sample)
		samples.append(sample)

	#Make name to each pipeline:
	names = make_pipeline_names_in_pipeline_order(pipeline_vec, pipeline_sizes)

	#Prepare MVU score:
	svu_graph_size = create_svu_predefined_graph_points_outputted_data_size(frames, framesamples, bands)
	svu_graph_accuracy = [[0.4,0], [0.7,0.5], [1,1]]

	svu_acc_weight = 0.5
	svu_size_weight = 0.5


	##### Plotting cost Vs. accuracy #####
	plt.figure(1, figsize=(17,4), tight_layout=True)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		plt.plot(samples[i][3]*freq, samples[i][2], "o", color=colors_all[i])

		#plot sample index/marker:
		plt.annotate(i, (samples[i][3]*freq, samples[i][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e10, 1-i*0.008, i_and_name, color = colors_all[i])

	plt.grid()
	plt.title('Cost Vs. Accuracy')
	plt.xlabel('Cost')
	plt.ylabel('Accuracy')
	#plt.xlim(9.6e-4, 1e-3)
	#plt.ylim(0.5, 1)
	plt.xscale("log")
	#plt.show()


	##### Plotting processing + downloading time Vs. accuracy #####
	plt.figure(2, figsize=(17,4), tight_layout=True)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		plt.plot(samples[i][3]*freq+samples[i][1]*download_rate, samples[i][2], "o", color=colors_all[i])

		#plot sample index/marker:
		plt.annotate(i, (samples[i][3]*freq+samples[i][1]*download_rate, samples[i][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e10, 1-i*0.008, i_and_name, color = colors_all[i])

	plt.grid()
	plt.title('Processing + Downloading Time Vs. Accuracy')
	plt.xlabel('Processing + Downloading Time')
	plt.ylabel('Accuracy')
	#plt.xlim(9.6e-4, 1e-3)
	#plt.ylim(0.5, 1)
	plt.xscale("log")
	#plt.show()

	svu_graph_size = create_svu_predefined_graph_points_outputted_data_size(frames, framesamples, bands)
	svu_graph_accuracy = [[0.4,0],[0.7,0.5],[1,1]]

	##### Plotting cost Vs. MUV(accuracy, data output) #####
	plt.figure(3, figsize=(17,4), tight_layout=True)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		mvu = svu_acc_weight*make_SVU(svu_graph_accuracy, samples[i][2]) + svu_size_weight*make_SVU(svu_graph_size, samples[i][1])
		cost = samples[i][3]*freq
		plt.plot(cost, mvu, "o", color=colors_all[i])

		#plot sample index/marker:
		plt.annotate(i, (cost, mvu), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e10, 1-i*0.008, i_and_name, color = colors_all[i])

	plt.grid()
	title_name = 'Cost Vs. MVU (Acc: ' + str(svu_acc_weight) + ' & Size: ' + str(svu_size_weight) + ')'
	plt.title(title_name)
	plt.xlabel('Cost')
	plt.ylabel('MVU')
	#plt.xlim(9.6e-4, 1e-3)
	#plt.ylim(0.5, 1)
	plt.xscale("log")
	plt.show()


make_pipeline_plot(pipeline_vec)