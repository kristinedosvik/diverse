import matplotlib.pyplot as plt

from g_binning import *
from g_compression import *
from g_dimensionalReduction import *
from g_georeferencing_and_geometricRegistration import *
from g_badPixel import *
from g_smileAndKeystone import *
from g_targetDetection import *
from g_classification import *
from g_anomalyDetection import *
from g_radiometricCalibration import *
from input_parameters import *

def create_algorithmic_operationcounts_array(bands):
	spectral_binning = OC_spectral_binning(frames, framesamples, bands, binningfactor)
	spatial_binning = OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)

	radiometric_calibration = OC_radiometricCalibration(frames, framesamples, bands)

	statisical_threshold_detection = OC_statisical_threshold_detection(frames, framesamples, bands, num_regions)
	correlation_detection = OC_correlation_detection(frames, framesamples, bands, num_regions)
	mean_threshold_detection = OC_mean_threshold_detection(frames, framesamples, bands)

	nearest_neighbour_correction = OC_nearest_neighbour_correction(bad_samples)
	mean_correction = OC_mean_correction(bad_samples)
	median_correction = OC_median_correction(bad_samples)

	smile_and_keystone =  OC_smile_and_keystone(frames, framesamples, bands)

	georeferencing = OC_georeferencing(frames, framesamples, bands)
	geometric_registration = OC_geometric_registration(frames, framesamples, bands, frame_increase_factor, framesample_increase_factor)

	PCA_sw = OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations)
	PCA_hw = OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations, dot_product_blocks)

	ICA = OC_ICA(frames, framesamples, bands, reducedbands, iterations)
	MNF = OC_MNF(frames, framesamples, bands, reducedbands, iterations)

	SAM = OC_SAM(frames, framesamples, bands)
	SAM_hw = OC_SAM_hw(frames, framesamples, bands)
	CEM = OC_CEM(frames, framesamples, bands)
	ACE_R = OC_ACE_R(frames, framesamples, bands)
	target_detection_hw = OC_target_detection_hw(frames, framesamples, bands)

	SVM = OC_SVM(frames, framesamples, bands, num_classes, total_num_support_vectors)

	GRX_R = OC_GRX(frames, framesamples, bands)
	LRX = OC_LRX(frames, framesamples, bands, outer_window, inner_window)
	FrFT_RX = OC_FrFT_RX(frames, framesamples, bands, fractional_domains)
	CRD = OC_CRD(frames, framesamples, bands, num_neighbours)
	F_MGD = OC_F_MGD(frames, framesamples, bands, kernel_element)

	CCSDS123_B1_sw = OC_CCSDS123_B1_sw(frames, framesamples, bands, P, D)
	CCSDS123_B1_hw = OC_CCSDS123_B1_hw(frames, framesamples, bands, P, D)
	CCSDS123_B2_sw = OC_CCSDS123_B2_sw(frames, framesamples, bands, P, D)
	CCSDS123_B2_hw = OC_CCSDS123_B2_hw(frames, framesamples, bands, P, D)

	return [x_, spectral_binning, spatial_binning, statisical_threshold_detection, correlation_detection, mean_threshold_detection, nearest_neighbour_correction, mean_correction, median_correction, smile_and_keystone, radiometric_calibration, georeferencing, geometric_registration, PCA_sw, PCA_hw, MNF, ICA, SAM, SAM_hw, CEM, ACE_R, target_detection_hw, SVM, GRX_R, LRX, FrFT_RX, CRD, F_MGD, CCSDS123_B1_sw, CCSDS123_B1_hw, CCSDS123_B2_sw, CCSDS123_B2_hw]



def print_algoritmic_operationcounts(algoritmic_operationcounts, algorithmic_names):
	for i in range (0, len(algorithmic_names)):
		print(algorithmic_names[i], ": ", algoritmic_operationcounts[i]*freq)


def print_and_plot_algorithmic_runtimes():

	algorithms_names_in_order = ["x", "Spectral binning", "Spatial binning", "Statisical threshold detection", "Correlation detection", "Mean threshold detection", "Nearest neighbour correction", "Mean correction", "Median correction", "Smile and keystone", "radiometric calibration", "Georeferencing", "Geometric registration", "PCA (sw)", "PCA (hw)", "MNF", "ICA", "SAM (sw)", "SAM (hw)", "CEM (sw)", "ACE (sw)", "Target detection (hw)", "SVM", "GRX","LRX", "FrFT RX", "CRD", "F-MGD (hw)", "CCSDS123 B1 (sw)", "CCSDS123 B1 (hw)","CCSDS123 B2 (sw)", "CCSDS123 B2 (hw)"]

	############### Generate array of operation counts ##############

	algoritmic_operationcounts_no_band_reduction = create_algorithmic_operationcounts_array(bands)
	algoritmic_operationcounts_1_band_reduction = create_algorithmic_operationcounts_array(bands_1_reduction)
	algoritmic_operationcounts_2_band_reduction = create_algorithmic_operationcounts_array(bands_2_reduction)


	############### PRINTS ##############
	
	print("\nNo band reduction: bands = ", bands)
	print_algoritmic_operationcounts(algoritmic_operationcounts_no_band_reduction, algorithms_names_in_order)
	
	print("\n1. band reduction: bands = ", bands_1_reduction)
	print_algoritmic_operationcounts(algoritmic_operationcounts_no_band_reduction, algorithms_names_in_order)
	
	print("\n2. band reduction: bands = ", bands_2_reduction)
	print_algoritmic_operationcounts(algoritmic_operationcounts_no_band_reduction, algorithms_names_in_order)


	############### PLOTS ##############
	plt.figure(1, figsize=(13,7), tight_layout=True)

	#### bands = bands ####
	for i in range(0, len(algoritmic_operationcounts_no_band_reduction)):
		plt.plot(algoritmic_operationcounts_no_band_reduction[i]*freq, 10, "o", color = color_cost_2[i])
		plt.annotate(i, (algoritmic_operationcounts_no_band_reduction[i]*freq, 10), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		i_and_name = str(i) + ": " + algorithms_names_in_order[i]
		plt.text(2e7, 14-i, i_and_name, color = color_cost_2[i])

	#### bands = bands_1 ####
	for i in range(0, len(algoritmic_operationcounts_1_band_reduction)):
		if(algorithms_names_in_order[i] == "Spectral binning" or algorithms_names_in_order[i] == "Spatial binning"):
			continue
		plt.plot(algoritmic_operationcounts_1_band_reduction[i]*freq, 0, "o", color = color_cost_2[i])
		plt.annotate(i, (algoritmic_operationcounts_1_band_reduction[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		i_and_name = str(i) + ": " + algorithms_names_in_order[i]
		

	#### bands = bands_2 ####
	for i in range(0, len(algoritmic_operationcounts_2_band_reduction)):
		if(i <= 16 and (i != 11 and i != 12)):
			continue
		plt.plot(algoritmic_operationcounts_2_band_reduction[i]*freq, -10, "o", color = color_cost_2[i])
		plt.annotate(i, (algoritmic_operationcounts_2_band_reduction[i]*freq, -10), textcoords="offset points", xytext=(0,10), color="black", ha='center')
		i_and_name = str(i) + ": " + algorithms_names_in_order[i]


	plt.grid()
	plt.ylim(-15,15)
	plt.xscale("log")
	#plt.savefig("plots_OC_runtimes.png")
	plt.show()

print_and_plot_algorithmic_runtimes()


############### Delete ###############
"""
##### Bands = bands #####

spectral_binning = OC_spectral_binning(frames, framesamples, bands, binningfactor)
spatial_binning = OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)

radiometric_calibration = OC_radiometricCalibration(frames, framesamples, bands)

statisical_threshold_detection = OC_statisical_threshold_detection(frames, framesamples, bands, num_regions)
correlation_detection = OC_correlation_detection(frames, framesamples, bands, num_regions)
mean_threshold_detection = OC_mean_threshold_detection(frames, framesamples, bands)

nearest_neighbour_correction = OC_nearest_neighbour_correction(bad_samples)
mean_correction = OC_mean_correction(bad_samples)
median_correction = OC_median_correction(bad_samples)

smile_and_keystone =  OC_smile_and_keystone(frames, framesamples, bands)

georeferencing = OC_georeferencing(frames, framesamples, bands)
geometric_registration = OC_geometric_registration(frames, framesamples, bands, frame_increase_factor, framesample_increase_factor)

PCA_sw = OC_PCA_sw(frames, framesamples, bands, reducedbands, iterations)
PCA_hw = OC_PCA_hw(frames, framesamples, bands, reducedbands, iterations, dot_product_blocks)

ICA = OC_ICA(frames, framesamples, bands, reducedbands, iterations)
MNF = OC_MNF(frames, framesamples, bands, reducedbands, iterations)

SAM = OC_SAM(frames, framesamples, bands)
SAM_hw = OC_SAM_hw(frames, framesamples, bands)
CEM = OC_CEM(frames, framesamples, bands)
ACE_R = OC_ACE_R(frames, framesamples, bands)
target_detection_hw = OC_target_detection_hw(frames, framesamples, bands)

SVM = OC_SVM(frames, framesamples, bands, num_classes, total_num_support_vectors)

GRX_R = OC_GRX(frames, framesamples, bands)
LRX = OC_LRX(frames, framesamples, bands, outer_window, inner_window)
FrFT_RX = OC_FrFT_RX(frames, framesamples, bands, fractional_domains)
CRD = OC_CRD(frames, framesamples, bands, num_neighbours)
F_MGD = OC_F_MGD(frames, framesamples, bands, kernel_element)

CCSDS123_B1_sw = OC_CCSDS123_B1_sw(frames, framesamples, bands, P, D)
CCSDS123_B1_hw = OC_CCSDS123_B1_hw(frames, framesamples, bands, P, D)
CCSDS123_B2_sw = OC_CCSDS123_B2_sw(frames, framesamples, bands, P, D)
CCSDS123_B2_hw = OC_CCSDS123_B2_hw(frames, framesamples, bands, P, D)


#### Bands = bands_1_reduction ###

spectral_binning_1 = OC_spectral_binning(frames, framesamples, bands_1_reduction, binningfactor)
spatial_binning_1 = OC_spatial_binning(frames, framesamples, bands_1_reduction, binningfactor, whatToBin)

radiometric_calibration_1 = OC_radiometricCalibration(frames, framesamples, bands_1_reduction)

statisical_threshold_detection_1 = OC_statisical_threshold_detection(frames, framesamples, bands_1_reduction, num_regions)
correlation_detection_1 = OC_correlation_detection(frames, framesamples, bands_1_reduction, num_regions)
mean_threshold_detection_1 = OC_mean_threshold_detection(frames, framesamples, bands_1_reduction)

nearest_neighbour_correction_1 = OC_nearest_neighbour_correction(bad_samples)
mean_correction_1 = OC_mean_correction(bad_samples)
median_correction_1 = OC_median_correction(bad_samples)

smile_and_keystone_1 =  OC_smile_and_keystone(frames, framesamples, bands_1_reduction)

georeferencing_1 = OC_georeferencing(frames, framesamples, bands_1_reduction)
geometric_registration_1 = OC_geometric_registration(frames, framesamples, bands_1_reduction, frame_increase_factor, framesample_increase_factor)

PCA_sw_1 = OC_PCA_sw(frames, framesamples, bands_1_reduction, reducedbands, iterations)
PCA_hw_1 = OC_PCA_hw(frames, framesamples, bands_1_reduction, reducedbands, iterations, dot_product_blocks)

ICA_1 = OC_ICA(frames, framesamples, bands_1_reduction, reducedbands, iterations)
MNF_1 = OC_MNF(frames, framesamples, bands_1_reduction, reducedbands, iterations)

SAM_1 = OC_SAM(frames, framesamples, bands_1_reduction)
SAM_hw_1 = OC_SAM_hw(frames, framesamples, bands_1_reduction)
CEM_1 = OC_CEM(frames, framesamples, bands_1_reduction)
ACE_R_1 = OC_ACE_R(frames, framesamples, bands_1_reduction)
target_detection_hw_1 = OC_target_detection_hw(frames, framesamples, bands_1_reduction)

SVM_1 = OC_SVM(frames, framesamples, bands_1_reduction, num_classes, total_num_support_vectors)

GRX_R_1 = OC_GRX(frames, framesamples, bands_1_reduction)
LRX_1 = OC_LRX(frames, framesamples, bands_1_reduction, outer_window, inner_window)
FrFT_RX_1 = OC_FrFT_RX(frames, framesamples, bands_1_reduction, fractional_domains)
CRD_1 = OC_CRD(frames, framesamples, bands_1_reduction, num_neighbours)
F_MGD_1 = OC_F_MGD(frames, framesamples, bands_1_reduction, kernel_element)

CCSDS123_B1_sw_1 = OC_CCSDS123_B1_sw(frames, framesamples, bands_1_reduction, P, D)
CCSDS123_B1_hw_1 = OC_CCSDS123_B1_hw(frames, framesamples, bands_1_reduction, P, D)
CCSDS123_B2_sw_1 = OC_CCSDS123_B2_sw(frames, framesamples, bands_1_reduction, P, D)
CCSDS123_B2_hw_1 = OC_CCSDS123_B2_hw(frames, framesamples, bands_1_reduction, P, D)


#### Bands = bands_2_reduction ####
spectral_binning_2 = OC_spectral_binning(frames, framesamples, bands_2_reduction, binningfactor)
spatial_binning_2 = OC_spatial_binning(frames, framesamples, bands_2_reduction, binningfactor, whatToBin)

radiometric_calibration_2 = OC_radiometricCalibration(frames, framesamples, bands_2_reduction)

statisical_threshold_detection_2 = OC_statisical_threshold_detection(frames, framesamples, bands_2_reduction, num_regions)
correlation_detection_2 = OC_correlation_detection(frames, framesamples, bands_2_reduction, num_regions)
mean_threshold_detection_2 = OC_mean_threshold_detection(frames, framesamples, bands_2_reduction)

nearest_neighbour_correction_2 = OC_nearest_neighbour_correction(bad_samples)
mean_correction_2 = OC_mean_correction(bad_samples)
median_correction_2 = OC_median_correction(bad_samples)

smile_and_keystone_2 =  OC_smile_and_keystone(frames, framesamples, bands_2_reduction)

georeferencing_2 = OC_georeferencing(frames, framesamples, bands_2_reduction)
geometric_registration_2 = OC_geometric_registration(frames, framesamples, bands_2_reduction, frame_increase_factor, framesample_increase_factor)

PCA_sw_2 = OC_PCA_sw(frames, framesamples, bands_2_reduction, reducedbands, iterations)
PCA_hw_2 = OC_PCA_hw(frames, framesamples, bands_2_reduction, reducedbands, iterations, dot_product_blocks)

ICA_2 = OC_ICA(frames, framesamples, bands_2_reduction, reducedbands, iterations)
MNF_2 = OC_MNF(frames, framesamples, bands_2_reduction, reducedbands, iterations)

SAM_2 = OC_SAM(frames, framesamples, bands_2_reduction)
SAM_hw_2 = OC_SAM_hw(frames, framesamples, bands_2_reduction)
CEM_2 = OC_CEM(frames, framesamples, bands_2_reduction)
ACE_R_2 = OC_ACE_R(frames, framesamples, bands_2_reduction)
target_detection_hw_2 = OC_target_detection_hw(frames, framesamples, bands_2_reduction)

SVM_2 = OC_SVM(frames, framesamples, bands_2_reduction, num_classes, total_num_support_vectors)

GRX_R_2 = OC_GRX(frames, framesamples, bands_2_reduction)
LRX_2 = OC_LRX(frames, framesamples, bands_2_reduction, outer_window, inner_window)
FrFT_RX_2 = OC_FrFT_RX(frames, framesamples, bands_2_reduction, fractional_domains)
CRD_2 = OC_CRD(frames, framesamples, bands_2_reduction, num_neighbours)
F_MGD_2 = OC_F_MGD(frames, framesamples, bands_2_reduction, kernel_element)

CCSDS123_B1_sw_2 = OC_CCSDS123_B1_sw(frames, framesamples, bands_2_reduction, P, D)
CCSDS123_B1_hw_2 = OC_CCSDS123_B1_hw(frames, framesamples, bands_2_reduction, P, D)
CCSDS123_B2_sw_2 = OC_CCSDS123_B2_sw(frames, framesamples, bands_2_reduction, P, D)
CCSDS123_B2_hw_2 = OC_CCSDS123_B2_hw(frames, framesamples, bands_2_reduction, P, D)



algorithms = [x_, spectral_binning, spatial_binning, statisical_threshold_detection, correlation_detection, mean_threshold_detection, nearest_neighbour_correction, mean_correction, median_correction, smile_and_keystone, radiometric_calibration, georeferencing, geometric_registration, PCA_sw, PCA_hw, MNF, ICA, SAM, SAM_hw, CEM, ACE_R, target_detection_hw, SVM, GRX_R, LRX, FrFT_RX, CRD, F_MGD, CCSDS123_B1_sw, CCSDS123_B1_hw, CCSDS123_B2_sw, CCSDS123_B2_hw]
algorithms_1 = [x_, spectral_binning_1, spatial_binning_1, statisical_threshold_detection_1, correlation_detection_1, mean_threshold_detection_1, nearest_neighbour_correction_1, mean_correction_1, median_correction_1, smile_and_keystone_1, radiometric_calibration_1, georeferencing_1, geometric_registration_1, PCA_sw_1, PCA_hw_1, MNF_1, ICA_1, SAM_1, SAM_hw_1, CEM_1, ACE_R_1, target_detection_hw_1, SVM_1, GRX_R_1, LRX_1, FrFT_RX_1, CRD_1, F_MGD_1, CCSDS123_B1_sw_1, CCSDS123_B1_hw_1, CCSDS123_B2_sw_1, CCSDS123_B2_hw_1]
algorithms_2 = [x_, spectral_binning_2, spatial_binning_2, statisical_threshold_detection_2, correlation_detection_2, mean_threshold_detection_2, nearest_neighbour_correction_2, mean_correction_2, median_correction_2, smile_and_keystone_2, radiometric_calibration_2, georeferencing_2, geometric_registration_2, PCA_sw_2, PCA_hw_2, MNF_2, ICA_2, SAM_2, SAM_hw_2, CEM_2, ACE_R_2, target_detection_hw_2, SVM_2, GRX_R_2, LRX_2, FrFT_RX_2, CRD_2, F_MGD_2, CCSDS123_B1_sw_2, CCSDS123_B1_hw_2, CCSDS123_B2_sw_2, CCSDS123_B2_hw_2]

"""
