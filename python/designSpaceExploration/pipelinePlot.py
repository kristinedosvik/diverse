import matplotlib.pyplot as plt
from processingGroups import *
from data_inputs import *
import random


def create_svu_predefined_graph_points_outputted_data_size(frames, framesamples, bands):
    best_case = frames*framesamples*1*16
    bands_10 = frames*framesamples*10*16
    bands_20 = frames*framesamples*20*16
    #assume bands = 120
    divided_4 = frames*framesamples*120/4*16
    divided_2 = frames*framesamples*120/2*16
    worst_case = frames*framesamples*120*16
    raw_cube = frames*framesamples*bands*16
    
    graph = [[best_case,1], [bands_10, 0.95], [bands_20, 0.85], [divided_4, 0.2], [divided_2, 0.1], [worst_case, 0.01], [raw_cube, 0]]
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


p0 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"] # infeasable sample

#B1 (hw)

p1_c1 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"] #infeasable sample
p2_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]
p3_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B1_hw"]
p4_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B1_hw"]
p5_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CCSDS123_B1_hw"]
p6_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_sw", "x", "CCSDS123_B1_hw"]
p7_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "CCSDS123_B1_hw"]
p8_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "ICA", "x", "CCSDS123_B1_hw"]
p9_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "MNF", "x", "CCSDS123_B1_hw"]
p10_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "MNF", "x", "CCSDS123_B1_hw"]

#B2 (hw)

p1_c2 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"] #infeasable sample
p2_c2 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"]
p3_c2 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B2_hw"]
p4_c2 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B2_hw"]
p5_c2 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CCSDS123_B2_hw"]
p6_c2 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_sw", "x", "CCSDS123_B2_hw"]

#B1 (sw)

p1_c3 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"] #infeasable sample
p2_c3 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"]
p3_c3 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B1_sw"]
p4_c3 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B1_sw"]
p5_c3 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B1_sw"]
p6_c3 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CCSDS123_B1_sw"]
p7_c3 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_sw", "x", "CCSDS123_B1_sw"]
p8_c3 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "x", "PCA_sw", "x", "CCSDS123_B1_sw"]

#B2 (sw)

p1_c4 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_sw"] #infeasable sample
p2_c4 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_sw"]
p3_c4 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B2_sw"]
p4_c4 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B2_sw"]
p5_c4 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B2_sw"]
p6_c4 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CCSDS123_B2_sw"]
p7_c4 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_sw", "x", "CCSDS123_B2_sw"]
p8_c4 = ["spectral_binning", "x", "x", "x", "statisical_threshold_detection", "nearest_neighbour_correction", "x", "PCA_sw", "x", "CCSDS123_B2_sw"]
p9_c4 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "MNF", "x", "CCSDS123_B2_sw"]
p10_c4 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "MNF", "x", "CCSDS123_B2_sw"]
p11_c4 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "CCSDS123_B2_sw"]
p12_c4 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "ICA", "x", "CCSDS123_B2_sw"]




compression_vec = [p0, p1_c1, p2_c1, p3_c1, p4_c1, p5_c1, p6_c1, p7_c1, p8_c1, p9_c1, p10_c1, \
					p1_c2, p2_c2, p3_c2, p4_c2, p5_c2, p6_c2, \
					p1_c3, p2_c3, p3_c3, p4_c3, p5_c3, p6_c3, p7_c3, p8_c3, \
					p1_c4, p2_c4, p3_c4, p4_c4, p5_c4, p6_c4, p7_c4, p8_c4, p9_c4, p10_c4, p11_c4, p12_c4]

pipeline_vec = compression_vec


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

pipeline_sizes = 10
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
	random.seed(1)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		plt.plot(samples[i][3]*freq, samples[i][2], "o", color=RGB(random.randrange(2, 200, 5), random.randrange(2, 200, 5), random.randrange(2, 200, 5)))

		#plot sample index/marker:
		plt.annotate(i, (samples[i][3]*freq, samples[i][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e4, 0.86-i*0.005, i_and_name, color=RGB(random.randrange(2, 200, 5), random.randrange(2, 200, 5), random.randrange(2, 200, 5)))

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
	random.seed(1)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		plt.plot(samples[i][3]*freq+samples[i][1]*16*download_rate, samples[i][2], "o", color=RGB(random.randrange(2, 200, 5), random.randrange(2, 200, 5), random.randrange(2, 200, 5)))

		#plot sample index/marker:
		plt.annotate(i, (samples[i][3]*freq+samples[i][1]*16*download_rate, samples[i][2]), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e4, 0.86-i*0.0051, i_and_name, color=RGB(random.randrange(2, 200, 5), random.randrange(2, 200, 5), random.randrange(2, 200, 5)))

	best_case = frames*framesamples*1*16*download_rate
	bands_10 = frames*framesamples*10*16*download_rate
	bands_20 = frames*framesamples*20*16*download_rate
	divided_4 = frames*framesamples*120/4*16*download_rate
	divided_2 = frames*framesamples*120/2*16*download_rate
	worst_case = frames*framesamples*120*16*download_rate
	raw_cube = frames*framesamples*1080*16*download_rate
	plt.plot(best_case, 0.8, "o", color="black")
	plt.plot(bands_10, 0.8, "o", color="black")
	plt.plot(bands_20, 0.8, "o", color="black")
	plt.plot(divided_4, 0.8, "o", color="black")
	plt.plot(divided_2, 0.8, "o", color="black")
	plt.plot(worst_case, 0.8, "o", color="black")
	plt.plot(raw_cube, 0.8, "o", color="black")
	
	plt.text(best_case, 0.8, "B", color = "black")
	plt.text(bands_10, 0.8, "X", color = "black")
	plt.text(bands_20, 0.8, "XX", color = "black")
	plt.text(divided_4, 0.8, "IV", color = "black")
	plt.text(divided_2, 0.8, "II", color = "black")
	plt.text(worst_case, 0.8, "W", color = "black")
	plt.text(raw_cube, 0.8, "R", color = "black")
	

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
	random.seed(1)
	for i in range(0, len(pipeline_vec)):
		#plot samples:
		mvu = svu_acc_weight*make_SVU(svu_graph_accuracy, samples[i][2]) + svu_size_weight*make_SVU(svu_graph_size, samples[i][1]*16)
		cost = samples[i][3]*freq
		plt.plot(cost, mvu, "o", color=RGB(random.randrange(2, 200, 5), random.randrange(2, 200, 5), random.randrange(2, 200, 5)))

		#plot sample index/marker:
		plt.annotate(i, (cost, mvu), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		#plt.annotate(i, (samples[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')

		#plot pipeline names:
		i_and_name = str(i) + ": " + names[i]
		plt.text(1e4, 1-i*0.04, i_and_name, color=RGB(random.randrange(2, 200, 5), random.randrange(2, 200, 5), random.randrange(2, 200, 5)))

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
