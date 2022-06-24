import matplotlib.pyplot as plt
import random

from binning import *
from compression import *
from dimensionalReduction import *
from georeferencing_and_geometricRegistration import *
from pixelMitigation import *
from smileAndKeystone import *
from targetDetection import *
from classification import *
from anomalyDetection import *
from radiometricCalibration import *
from data_inputs import *

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



##### Bands = bands #####

spectral_binning = OC_spectral_binning(frames, framesamples, bands, binningfactor)
spatial_binning = OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)

radiometric_calibration = OC_radiometricCalibration(frames, framesamples, bands)

statisical_threshold_detection = OC_statisical_threshold_detection(frames, framesamples, bands, num_regions)
correlation_detection = OC_correlation_detection(frames, framesamples, bands, num_regions)
mean_threshold_detection = OC_mean_threshold_detection(frames, framesamples, bands, num_neighbours)

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

print("Bands = ", bands)
print("spectral_binning: ", spectral_binning*freq)
print("statisical_threshold_detection: ", statisical_threshold_detection*freq)
print("smile_and_keystone: ", smile_and_keystone*freq)
print("georeferencing: ", georeferencing*freq)
print("geometric_registration: ", geometric_registration*freq)
print("PCA sw: ", PCA_sw*freq)
print("PCA hw: ", PCA_hw*freq)
print("ICA: ", ICA*freq)
print("MNF: ", MNF*freq)
print("SAM: ", SAM*freq)
print("CEM: ", CEM*freq)
print("ACE_R: ", ACE_R*freq)
print("SVM: ", SVM*freq)
print("GRX_R: ", GRX_R*freq)
print("LRX: ", LRX*freq)
print("FrFT_RX: ", FrFT_RX*freq)
print("CRD: ", CRD*freq)
print("F_MGD: ", F_MGD*freq)


#### Bands = bands 1. reduction ####

spectral_binning_1 = OC_spectral_binning(frames, framesamples, bands_1_reduction, binningfactor)
spatial_binning_1 = OC_spatial_binning(frames, framesamples, bands_1_reduction, binningfactor, whatToBin)

radiometric_calibration_1 = OC_radiometricCalibration(frames, framesamples, bands_1_reduction)

statisical_threshold_detection_1 = OC_statisical_threshold_detection(frames, framesamples, bands_1_reduction, num_regions)
correlation_detection_1 = OC_correlation_detection(frames, framesamples, bands_1_reduction, num_regions)
mean_threshold_detection_1 = OC_mean_threshold_detection(frames, framesamples, bands_1_reduction, num_neighbours)

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



#### Bands = bands 2. reduction ####

spectral_binning_2 = OC_spectral_binning(frames, framesamples, bands_2_reduction, binningfactor)
spatial_binning_2 = OC_spatial_binning(frames, framesamples, bands_2_reduction, binningfactor, whatToBin)

radiometric_calibration_2 = OC_radiometricCalibration(frames, framesamples, bands_2_reduction)

statisical_threshold_detection_2 = OC_statisical_threshold_detection(frames, framesamples, bands_2_reduction, num_regions)
correlation_detection_2 = OC_correlation_detection(frames, framesamples, bands_2_reduction, num_regions)
mean_threshold_detection_2 = OC_mean_threshold_detection(frames, framesamples, bands_2_reduction, num_neighbours)

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


color_cost_2 = ["black", RGB(255,128,128), RGB(255,0,0), RGB(200,0,0), RGB(148,3,3), \
#RGB(255,146,205), RGB(255,0,137), RGB(229,0,122), RGB(198,0,105), RGB(179,0,96), \
RGB(225,144,225), RGB(209,0,209), RGB(141,0,141), RGB(80,0,80), \
RGB(158,158,255), RGB(0,0,255), RGB(0,0,125), RGB(0,0,50), \
RGB(127,247,255), RGB(0,212,228), RGB(1,182,195), RGB(3,152,162), \
RGB(138,255,138), RGB(0,255,0), RGB(0,174,0), RGB(0,100,0), \
RGB(255,255,0), RGB(191,191,0), RGB(148,148,0), \
RGB(255,229,166), RGB(255,179,0), RGB(154,109,3), RGB(105,74,0), \
RGB(182,182,182), RGB(82,82,82), \
RGB(156,102,31), "brown"]



algorithms_names = ["x", "Spectral binning", "Spatial binning", "Statisical threshold detection", "Correlation detection", "Mean threshold detection", "Nearest neighbour correction", "Mean correction", "Median correction", "Smile and keystone", "radiometric_calibration", "Georeferencing", "Geometric registration", "PCA (sw)", "PCA (hw)", "MNF", "ICA", "SAM (sw)", "SAM (hw)", "CEM (sw)", "ACE (sw)", "Target detection (hw)", "SVM", "GRX","LRX", "FrFT RX", "CRD", "F MGD (hw)", "CCSDS123 B1 (sw)", "CCSDS123 B1 (hw)","CCSDS123 B2 (sw)", "CCSDS123 B2 (hw)"]
algorithms = [x_, spectral_binning, spatial_binning, statisical_threshold_detection, correlation_detection, mean_threshold_detection, nearest_neighbour_correction, mean_correction, median_correction, smile_and_keystone, radiometric_calibration, georeferencing, geometric_registration, PCA_sw, PCA_hw, MNF, ICA, SAM, SAM_hw, CEM, ACE_R, target_detection_hw, SVM, GRX_R, LRX, FrFT_RX, CRD, F_MGD, CCSDS123_B1_sw, CCSDS123_B1_hw, CCSDS123_B2_sw, CCSDS123_B2_hw]
algorithms_1 = [x_, spectral_binning_1, spatial_binning_1, statisical_threshold_detection_1, correlation_detection_1, mean_threshold_detection_1, nearest_neighbour_correction_1, mean_correction_1, median_correction_1, smile_and_keystone_1, radiometric_calibration_1, georeferencing_1, geometric_registration_1, PCA_sw_1, PCA_hw_1, MNF_1, ICA_1, SAM_1, SAM_hw_1, CEM_1, ACE_R_1, target_detection_hw_1, SVM_1, GRX_R_1, LRX_1, FrFT_RX_1, CRD_1, F_MGD_1, CCSDS123_B1_sw_1, CCSDS123_B1_hw_1, CCSDS123_B2_sw_1, CCSDS123_B2_hw_1]
algorithms_2 = [x_, spectral_binning_2, spatial_binning_2, statisical_threshold_detection_2, correlation_detection_2, mean_threshold_detection_2, nearest_neighbour_correction_2, mean_correction_2, median_correction_2, smile_and_keystone_2, radiometric_calibration_2, georeferencing_2, geometric_registration_2, PCA_sw_2, PCA_hw_2, MNF_2, ICA_2, SAM_2, SAM_hw_2, CEM_2, ACE_R_2, target_detection_hw_2, SVM_2, GRX_R_2, LRX_2, FrFT_RX_2, CRD_2, F_MGD_2, CCSDS123_B1_sw_2, CCSDS123_B1_hw_2, CCSDS123_B2_sw_2, CCSDS123_B2_hw_2]
############### PLOTS ##############

#### Overwiew, with and without grids ####
"""
plt.figure(1, figsize=(11,4), tight_layout=True)
#Fig 1)
for i in range(0, len(algorithms)):
	plt.plot(algorithms[i]*freq, 0, "o", color = colors_costs[i])
	plt.annotate(i, (algorithms[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')
	i_and_name = str(i) + ": " + algorithms_names[i]
	plt.text(1e12, 14-i, i_and_name, color = colors_costs[i])

plt.grid()
plt.ylim(-15,15)
plt.xscale("log")
#plt.show()
plt.savefig("plot_cost_withGrid.png")
"""

#### zoomed in ####
plt.figure(1, figsize=(13,7), tight_layout=True)

#### bands = bands ####
for i in range(0, len(algorithms)):
	plt.plot(algorithms[i]*freq, 10, "o", color = color_cost_2[i])
	#plt.plot(i, 10, "o", color = color_cost_2[i])
	plt.annotate(i, (algorithms[i]*freq, 10), textcoords="offset points", xytext=(0,10), color="black", ha='center')
	#plt.annotate(i, (i, 10), textcoords="offset points", xytext=(0,10), color="black", ha='center')
	i_and_name = str(i) + ": " + algorithms_names[i]
	plt.text(2e7, 14-i, i_and_name, color = color_cost_2[i])

#### bands = bands_1 ####
for i in range(0, len(algorithms_1)):
	if(algorithms_1[i] == spectral_binning_1 or algorithms_1[i] == spatial_binning_1):
		continue
	plt.plot(algorithms_1[i]*freq, 0, "o", color = color_cost_2[i])
	plt.annotate(i, (algorithms_1[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')
	i_and_name = str(i) + ": " + algorithms_names[i]
	#plt.text(2e7, 14-i, i_and_name, color = color_cost_2[i])

#### bands = bands_2 ####
for i in range(0, len(algorithms_2)):
	if(i <= 16):
		continue
	plt.plot(algorithms_2[i]*freq, -10, "o", color = color_cost_2[i])
	plt.annotate(i, (algorithms_2[i]*freq, -10), textcoords="offset points", xytext=(0,10), color="black", ha='center')
	i_and_name = str(i) + ": " + algorithms_names[i]

	#plt.text(2e7, 14-i, i_and_name, color = color_cost_2[i])


#plt.grid()
#plt.xlim(0, 10)
plt.ylim(-15,15)
plt.xscale("log")
plt.show()
#plt.savefig("plot.png")

