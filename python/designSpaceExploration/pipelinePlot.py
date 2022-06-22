import matplotlib.pyplot as plt
from processingGroups import *
from data_inputs import *


def create_svu_predefined_graph_points_outputted_data_size(frames, framesamples, bands):
    best_case = frames*framesamples*1*16
    bands_10 = frames*framesamples*10*16
    bands_20 = frames*framesamples*20*16
    #assume bands = 120
    divided_4 = frames*framesamples*120/4*16
    divided_2 = frames*framesamples*120/2*16
    worst_case = frames*framesamples*120*16
    
    graph = [[best_case,1], [bands_10, 0.95], [bands_20, 0.85], [divided_4, 0.2], [divided_2, 0.1], [worst_case, 0]]
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




#return [spec_vec[i], spat_vec[i], "x", "x", bad_p_det_vec[i], bad_p_cor_vec[i], snk_vec[i], dimRed_vec[i], geo_ref_vec[i], "GRX_sw"]
pipeline_sizes = 10
#p0 = ["spectral_binning", "spatial_binning", "x", "x", "OC_statisical_threshold_detection", "OC_median_correction", "smile_and_keystone", "MNF", "geometric_registration", "CCSDS123_B2_sw"]
p0 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
p1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

pNMF = ["x", "x", "x", "x", "x", "x", "x", "MNF", "x", "x"]

#compression pipelines:
p2 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "F_MGD_hw"]
p3 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "F_MGD_hw"]
p4 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_hw"]
p5 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_hw"]


p6 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]
p7 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]

p8 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_hw"]
p9 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_hw"]
p10 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "ACE_hw"]
p11 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "ACE_hw"]
p12 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "ASMF_hw"]
p13 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "ASMF_hw"]



p14 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"]
p15 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"]

p16 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_sw"]
p17 = ["spectral_binning", "x", "x", "radiometric_calibration", "x", "x", "x", "x", "x", "SAM_sw"]
p18 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_sw"]

p19 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"]
p20 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"]

p21 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]
p22 = ["spectral_binning", "x", "x", "radiometric_calibration", "x", "x", "x", "PCA_hw", "x", "x"]
p23 = ["x", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]

"""
p21 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SVM"]
p22 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "SVM"]

p23 = ["spectral_binning", "x", "x", "radiometric_calibration", "x", "x", "smile_and_keystone", "x", "x", "SVM"]
p24 = ["spectral_binning", "x", "x", "radiometric_calibration", "x", "x", "x", "x", "x", "SVM"]
p25 = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "x", "x", "SVM"]

p26 = ["spectral_binning", "x", "x", "radiometric_calibration", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "SVM"]
p27 = ["spectral_binning", "x", "x", "radiometric_calibration", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "SVM"]

p28 = ["spectral_binning", "x", "x", "radiometric_calibration", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "geometric_registration", "SVM"]
p29 = ["spectral_binning", "x", "x", "radiometric_calibration", "statisical_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "geometric_registration", "SVM"]
"""





#Legg inn for resten av de interessante pipelinene.


pipeline_vec_low_runtime = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23]
pipeline_vec = pipeline_vec_low_runtime

pipeline_vec_all = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23] #, p24, p25, p26, p27, p28, p29]#, p30, p31, p3, p33, p34, p35, p36, p37, p38, p39, p40, p41, p4, p43, p44, p45, p46, p47, p48, p49, pNMF]
#pipeline_vec = pipeline_vec_all




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
	svu_graph_accuracy = [[0.4,0], [0.7,0.4], [0.8, 0.8], [1,1]]

	svu_acc_weight = 0.5
	svu_size_weight = 0.5


	##### Plotting cost Vs. accuracy #####
	plt.figure(1, figsize=(17,15), tight_layout=True)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		plt.plot(samples[i][3]*freq, samples[i][2], "o", color=colors_all[i])

		#plot sample index/marker:
		plt.annotate(i, (samples[i][3]*freq, samples[i][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e4, 0.86-i*0.005, i_and_name, color = colors_all[i])

	plt.grid()
	plt.title('Cost Vs. Accuracy')
	plt.xlabel('Cost')
	plt.ylabel('Accuracy')
	#plt.xlim(1e-1, 1e6)
	#plt.ylim(0.5, 1)
	plt.xscale("log")
	#plt.show()
	#plt.savefig("plot_low_coss_accuracy.png")


	##### Plotting processing + downloading time Vs. accuracy #####
	plt.figure(2, figsize=(17,15), tight_layout=True)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		plt.plot(samples[i][3]*freq+samples[i][1]*16*download_rate, samples[i][2], "o", color=colors_all[i])

		#plot sample index/marker:
		plt.annotate(i, (samples[i][3]*freq+samples[i][1]*16*download_rate, samples[i][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e4, 0.86-i*0.0051, i_and_name, color = colors_all[i])

	best_case = frames*framesamples*1*16*download_rate
	bands_10 = frames*framesamples*10*16*download_rate
	bands_20 = frames*framesamples*20*16*download_rate
	divided_4 = frames*framesamples*120/4*16*download_rate
	divided_2 = frames*framesamples*120/2*16*download_rate
	worst_case = frames*framesamples*120*16*download_rate
	plt.plot(best_case, 0.8, "o", color="black")
	plt.plot(bands_10, 0.8, "o", color="black")
	plt.plot(bands_20, 0.8, "o", color="black")
	plt.plot(divided_4, 0.8, "o", color="black")
	plt.plot(divided_2, 0.8, "o", color="black")
	plt.plot(worst_case, 0.8, "o", color="black")
	
	plt.text(best_case, 0.8, "B", color = "black")
	plt.text(bands_10, 0.8, "X", color = "black")
	plt.text(bands_20, 0.8, "XX", color = "black")
	plt.text(divided_4, 0.8, "IV", color = "black")
	plt.text(divided_2, 0.8, "II", color = "black")
	plt.text(worst_case, 0.8, "W", color = "black")
	print("divided_4", divided_4)
	print("divided_2", divided_2)
	print("worst_case", worst_case)

	plt.grid()
	plt.title('Processing + Downloading Time Vs. Accuracy')
	plt.xlabel('Processing + Downloading Time')
	plt.ylabel('Accuracy')
	##plt.xlim(1e-1, 1e6)
	#plt.ylim(0.5, 1)
	plt.xscale("log")
	#plt.show()
	#plt.savefig("plot_low_cost_total_processing.png")


	##### Plotting cost Vs. MUV(accuracy, data output) #####
	plt.figure(3, figsize=(17,15), tight_layout=True)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		mvu = svu_acc_weight*make_SVU(svu_graph_accuracy, samples[i][2]) + svu_size_weight*make_SVU(svu_graph_size, samples[i][1]*16)
		cost = samples[i][3]*freq
		plt.plot(cost, mvu, "o", color=colors_all[i])

		#plot sample index/marker:
		plt.annotate(i, (cost, mvu), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e4, 1-i*0.04, i_and_name, color = colors_all[i])

	plt.grid()
	title_name = 'Cost Vs. MVU (Acc: ' + str(svu_acc_weight) + ' + Size: ' + str(svu_size_weight) + ')'
	plt.title(title_name)
	plt.xlabel('Cost')
	plt.ylabel('MVU')
	#plt.xlim(1e-1, 1e6)
	#plt.ylim(0.5, 1)
	plt.xscale("log")
	#plt.show()
	#plt.savefig("plot_low_cost_mvu.png")



	#"""
	##### Plotting SVU graf #####
	svu_graph_size_x = [row[0] for row in svu_graph_size]
	svu_graph_size_y = [row[1] for row in svu_graph_size]
	plt.figure(4, figsize=(17,4), tight_layout=True)
	plt.plot(svu_graph_size_x, svu_graph_size_y, color="grey")
	plt.xscale("linear")
	
	svu_graph_accuracy_x = [row[0] for row in svu_graph_accuracy]
	svu_graph_accuracy_y = [row[1] for row in svu_graph_accuracy]
	plt.figure(5, figsize=(17,4), tight_layout=True)
	plt.plot(svu_graph_accuracy_x, svu_graph_accuracy_y, color="blue")
	plt.xscale("linear")
	#"""

	plt.show()


print(framesamples*frames*120)
print(framesamples*frames*120/2)
make_pipeline_plot(pipeline_vec)
