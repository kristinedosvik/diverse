import matplotlib.pyplot as plt

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


dr1 =1/1000000
dr2 = 1/125000
download_rate = dr1
freq = 1/667000000
frames = 956
framesamples = 684
bands = 1080
binningfactor = 9
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

x_ = 0
spectral_binning = OC_spectral_binning(frames, framesamples, bands, binningfactor)
spatial_binning = OC_spatial_binning(frames, framesamples, bands, binningfactor, whatToBin)

radiometric_calibration = OC_radiometricCalibration(frames, framesamples, bands)

statisical_threshold_detection = OC_statisical_threshold_detection(frames, framesamples, bands, num_regions)
correlation_detection = OC_correlation_detection(frames, framesamples, bands, num_regions)

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


colors_1crimson = [RGB(220,20,60)]

colors_3turkis = [RGB(69,139,116), RGB(102,205,170), RGB(127,244,212)]
colors_3ligthblue = [RGB(83,134,139), RGB(122,197,205), RGB(152,245,255)]
colors_3pink = [RGB(139,10,80), RGB(205,16,118), RGB(255,20,147)]

colors_5brown = [RGB(138,51,36), RGB(156,102,31), RGB(139,131,120), RGB(205,192,176), RGB(238,223,204)]
colors_5gray = [RGB(40,40,40), RGB(91,91,91), RGB(132,132,132), RGB(183,183,183), RGB(215,215,215)]
colors_5purple = [RGB(72,61,139), RGB(104,34,139), RGB(154,50,205), RGB(191,62,255), RGB(238,130,238)]
colors_yellow = [RGB(139,105,20), RGB(205,155,29), RGB(255,215,0), RGB(255,255,0), RGB(244,246,143)]

colors_6red = [RGB(255,0,0), RGB(205,0,0), RGB(155,0,0), RGB(105,0,0), RGB(55,0,0), RGB(10,0,0)]
colors_6green = [RGB(0,255,0), RGB(0,205,0), RGB(0,155,0), RGB(0,105,0), RGB(0,55,0), RGB(0,10,0)]
colors_6blue = [RGB(0,0,255), RGB(0,0,205), RGB(0,0,155), RGB(0,0,105), RGB(0,0,55), RGB(0,0,10)]

#x = [x, spectral_binning, spatial_binning, statisical_threshold_detection, correlation_detection, nearest_neighbour_correction, mean_correction, median_correction, smile_and_keystone, radiometric_calibration,\
#georeferencing, geometric_registration, PCA_sw, PCA_hw, ICA, MNF, SAM, CEM, ACE_R, target_detection_hw, GRX_R, LRX, CCSDS123_B1_sw, CCSDS123_B1_hw, CCSDS123_B2_sw, CCSDS123_B2_hw]

colors_costs = ["black", colors_3turkis[0], colors_3turkis[1], colors_3ligthblue[0], colors_3ligthblue[1], colors_3pink[0], colors_3pink[1], colors_3pink[2], colors_5brown[0], colors_5gray[1], \
colors_5purple[0], colors_5purple[1], colors_yellow[0], colors_yellow[1], colors_yellow[2], colors_yellow[3], colors_6red[0], colors_6red[1], colors_6red[2], colors_6red[3], colors_6red[4], \
"grey", colors_6green[0], colors_6green[1], colors_6green[2], colors_6green[3], colors_6green[4], colors_6blue[0], colors_6blue[1], colors_6blue[2], colors_6blue[3], colors_1crimson[0], colors_yellow[4], colors_3turkis[2]]

algorithms_names = ["x", "spectral binning", "spatial binning", "statisical threshold detection", "correlation detection", "nearest neighbour correction", "mean correction", "median correction", "smile and keystone", "georeferencing", "geometric registration", "PCA sw", "PCA hw", "MNF", "SAM", "SAM hw", "CEM", "ACE", "target_detection hw", "SVM", "GRX R","LRX", "FrFT RX", "CRD", "F MGD", "CCSDS123 B1 sw", "CCSDS123 B1 hw","CCSDS123 B2 sw", "CCSDS123 B2 hw", "ICA", "radiometric_calibration"]
algorithms = [x_, spectral_binning, spatial_binning, statisical_threshold_detection, correlation_detection, nearest_neighbour_correction, mean_correction, median_correction, smile_and_keystone, georeferencing, geometric_registration, PCA_sw, PCA_hw, MNF, SAM, SAM_hw, CEM, ACE_R, target_detection_hw, GRX_R, LRX, FrFT_RX, CRD, F_MGD, CCSDS123_B1_sw, CCSDS123_B1_hw,CCSDS123_B2_sw, CCSDS123_B2_hw, ICA, radiometric_calibration,  SVM]

############### PLOTS ##############

#### Overwiew, with and without grids ####

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
plt.show()
#plt.savefig("plot_cost_withGrid.png")
"""

#### zoomed in ####
plt.figure(1, figsize=(17,4), tight_layout=True)
#Fig 1)
for i in range(0, len(algorithms)):
	plt.plot(algorithms[i]*freq, 0, "o", color = colors_costs[i])
	plt.annotate(i, (algorithms[i]*freq, 0), textcoords="offset points", xytext=(0,10), color="black", ha='center')
	i_and_name = str(i) + ": " + algorithms_names[i]
	plt.text(1e12, 14-i, i_and_name, color = colors_costs[i])

plt.grid()
#plt.xlim(9.6e-4, 1e-3)
plt.ylim(-15,15)
plt.xscale("log")
plt.show()
#plt.savefig("plot_cost.png")
"""
