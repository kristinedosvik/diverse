import numpy as np

#pipelines
noProcessing = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"] # infeasable sample
noProcessing = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] # infeasable sample



############### Compression: ###############

b1_hw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]
b1_hw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]

b1_sw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"]
b1_sw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_sw"]

b2_hw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"]
b2_hw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_hw"]

b2_sw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_sw"]
b2_sw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B2_sw"]

##

pca_hw = ["x", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]
pca_hw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]
pca_hw_spec_b1_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B1_hw"]
pca_hw_spec_b2_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B2_hw"]

##

compression_pipelines = [b1_hw, b1_hw_spec, b1_sw, b1_sw_spec, b2_hw, b2_hw_spec, pca_hw, pca_hw_spec, pca_hw_spec_b1_hw, pca_hw_spec_b2_hw] 

#Compression with dimensional reduction:
"""
pca_hw = ["x", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]
pca_hw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"]
pca_hw_spec_b1_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B1_hw"]

#Vet ikke helt hvordan jeg skal få dette til å fungere enda.
pca_hw_spec_reducedDimensions = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "x"] #legge til de reduced spatial vektorene som utgjør PCA sin transformasjonsmatrise
pca_hw_spec_b1_hw_reducedDimensions = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B1_hw"] #samme som over

#Add correcting algorithms
pca_hw_spec_dete_snk_radio = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "x"]
pca_hw_spec_dete = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "x"]
pca_hw_spec_snk = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "x"]
pca_hw_spec_radio = ["spectral_binning", "x", "x", "radiometric_calibration", "x", "x", "x", "PCA_hw", "x", "x"]

#Check how added end compression will be with the corrected algorithms
pca_hw_spec_dete_snk_radio_b1_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "CCSDS123_B1_hw"]
pca_hw_spec_dete_snk_radio_b1_sw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "CCSDS123_B1_sw"]
pca_hw_spec_dete_snk_radio_b2_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "CCSDS123_B2_hw"]
pca_hw_spec_dete_snk_radio_b2_sw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "CCSDS123_B2_sw"]

#Check that when having other type of dimensional reduction, the dimensional reduction algorithm will dominate the run time:
pca_sw_spec_dete_snk_radio_b1_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_sw", "x", "CCSDS123_B1_hw"]
pca_sw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]

mnf_spec_dete_snk_radio_b1_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "MNF", "x", "CCSDS123_B1_hw"]
mnf_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]

ica_spec_dete_snk_radio_b1_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "ICA", "x", "CCSDS123_B1_hw"]
ica_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]

compression_pipelines = [b1_hw, b1_hw_spec, b1_sw_spec, b1_hw_spec, b1_sw_spec, pca_hw, pca_hw_spec, pca_hw_spec_b1_hw, pca_hw_spec_reducedDimensions, pca_hw_spec_b1_hw_reducedDimensions, pca_hw_spec_dete_snk_radio, pca_hw_spec_dete, pca_hw_spec_snk, pca_hw_spec_radio, pca_hw_spec_dete_snk_radio_b1_hw, pca_hw_spec_dete_snk_radio_b1_sw, pca_hw_spec_dete_snk_radio_b2_hw, pca_hw_spec_dete_snk_radio_b2_sw, pca_sw_spec_dete_snk_radio_b1_hw, pca_sw_spec, mnf_spec_dete_snk_radio_b1_hw, mnf_spec, ica_spec_dete_snk_radio_b1_hw, ica_spec]
"""


############### Classification: ###############

svm = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "SVM"]
svm_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SVM"]
svm_pca_hw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "SVM"]
svm_pca_hw_spec_dete_snk_radio = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "SVM"]

##

svm_pca_sw_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "SVM"]
svm_mnf_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "MNF", "x", "SVM"]
svm_ica_spec = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "SVM"]


classification_pipelines = [svm, svm_spectral, svm_pca_hw_spec, svm_pca_hw_spec_dete_snk_radio, svm_pca_sw_spec, svm_mnf_spec, svm_ica_spec]


############### Target detection/anomaly detection HW: ###############

fmgd_hw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "F_MGD_hw"]
fmgd_hw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "F_MGD_hw"]
spec_dete_geocal_fmgd_hw = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "x", "geometric_registration", "F_MGD_hw"]
spec_pca_hw_dete_geocal_fmgd_hw = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "F_MGD_hw"]

sam_hw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_hw"]
sam_hw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_hw"]
spec_dete_snk_radio_sam_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "SAM_hw"]

cem_hw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_hw"]
cem_hw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_hw"]
spec_dete_snk_radio_cem_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "CEM_hw"]

targetAnomalyHW_pipelines = [fmgd_hw, fmgd_hw_spectral, spec_dete_geocal_fmgd_hw, spec_pca_hw_dete_geocal_fmgd_hw, sam_hw, sam_hw_spectral, spec_dete_snk_radio_sam_hw, cem_hw, cem_hw_spectral, spec_dete_snk_radio_cem_hw]


"""
spec_dete_snk_radio = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "x"]
spec_dete_snk_radio_ace_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "ACE_hw"]

spec_pca_hw_geocal = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "geometric_registration", "x"]
spec_pca_hw_geocal_fmgd_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "geometric_registration", "F_MGD_hw"]

targetAnomalyHW_pipelines = [sam_hw, sam_hw_spectral, fmgd_hw, fmgd_hw_spectral, ace_hw, ace_hw_spectral, spec_dete_snk_radio, spec_dete_snk_radio_ace_hw, spec_pca_hw_geocal, spec_pca_hw_geocal_fmgd_hw]
"""


############### Target detection SW: ###############

# SAM:

sam_sw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_sw"]
sam_sw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "SAM_sw"]
sam_sw_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "SAM_sw"]
sam_sw_spec_dete_snk_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "SAM_sw"]

CEM_sw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_sw"]
CEM_sw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_sw"]
CEM_sw_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CEM_sw"]
CEM_sw_spec_dete_snk_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "CEM_sw"]

ACE_sw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "ACE_sw"]
ACE_sw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "ACE_sw"]
ACE_sw_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "ACE_sw"]
ACE_sw_spec_dete_snk_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "ACE_sw"]

target_sw_pipelines = [sam_sw, sam_sw_spectral, sam_sw_spectral_pca_hw, sam_sw_spec_dete_snk_radio_pca_hw, CEM_sw, CEM_sw_spectral, CEM_sw_spectral_pca_hw, CEM_sw_spec_dete_snk_radio_pca_hw, ACE_sw, ACE_sw_spectral, ACE_sw_spectral_pca_hw, ACE_sw_spec_dete_snk_radio_pca_hw]


"""
sam_sw_spec_dete_snk_radio = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "SAM_sw"]
sam_sw_spec_dete_snk_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "SAM_sw"]

sam_sw_spec_dete_snk_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_sw", "x", "SAM_sw"]
pca_sw = ["x", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]

sam_sw_spectral_radcal = ["spectral_binning", "x", "x", "radiometric_calibration", "x", "x", "x", "x", "x", "SAM_sw"]
sam_sw_spectral_det = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "x", "x", "SAM_sw"]
sam_sw_spectral_snk = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "x", "x", "SAM_sw"]


sam_sw_pipelines = [sam_sw, sam_sw_spectral, sam_sw_spec_dete_snk_radio, sam_sw_spec_dete_snk_radio_pca_hw, sam_sw_spec_dete_snk_radio_pca_hw, pca_sw, sam_sw_spectral_radcal, sam_sw_spectral_det, sam_sw_spectral_snk]

# CEM, ACE:

cem_sw = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_sw"]
cem_sw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CEM_sw"]
cem_sw_spectral_dete_snk_radio = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "CEM_sw"]

cem_sw_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CEM_sw"]
cem_sw_spectral_dete_snk_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "CEM_sw"]

cem_sw_spectral_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "x", "x", "x", "PCA_hw", "x", "CEM_sw"]
cem_sw_spectral_dete_pca_hw = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CEM_sw"]
cem_sw_spectral_snk_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "smile_and_keystone", "PCA_hw", "x", "CEM_sw"]

spectral_pca_sw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]
#cem_sw_spectral_pca_sw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CEM_sw"]

ace_sw_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "ACE_sw"]
ace_sw_spectral_dete_snk_radio = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "x", "x", "ACE_sw"]
ace_sw_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "ACE_sw"]
ace_sw_spectral_dete_snk_radio_pca_hw = ["spectral_binning", "x", "x", "radiometric_calibration", "mean_threshold_detection", "nearest_neighbour_correction", "smile_and_keystone", "PCA_hw", "x", "ACE_sw"]

cem_ace_sw_pipelines = [cem_sw, cem_sw_spectral, cem_sw_spectral_dete_snk_radio, cem_sw_spectral_pca_hw, cem_sw_spectral_dete_snk_radio_pca_hw, cem_sw_spectral_radio_pca_hw, cem_sw_spectral_dete_pca_hw, cem_sw_spectral_snk_pca_hw, spectral_pca_sw, ace_sw_spectral, ace_sw_spectral_dete_snk_radio, ace_sw_spectral_pca_hw, ace_sw_spectral_dete_snk_radio_pca_hw]


target_sw_pipelines = []
for i in range(0, len(sam_sw_pipelines)):
	target_sw_pipelines.append(sam_sw_pipelines[i])
for i in range(0, len(cem_ace_sw_pipelines)):
	target_sw_pipelines.append(cem_ace_sw_pipelines[i])
"""


############### Anomaly detection SW: ###############


GRX = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "GRX_sw"]
GRX_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "GRX_sw"]
GRX_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "GRX_sw"]
GRX_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "GRX_sw"]
GRX_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "GRX_sw"]

LRX = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "LRX_sw"]
LRX_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "LRX_sw"]
LRX_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "LRX_sw"]
LRX_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "LRX_sw"]
LRX_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "LRX_sw"]

CRD = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CRD_sw"]
CRD_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CRD_sw"]
CRD_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CRD_sw"]
CRD_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "CRD_sw"]
CRD_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "FrFT_RX_sw"]

frft_rx = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "FrFT_RX_sw"]
frft_rx_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "FrFT_RX_sw"]
frft_rx_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "FrFT_RX_sw"]
frft_rx_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "FrFT_RX_sw"]
frft_rx_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "FrFT_RX_sw"]

anomaly_sw_pipelines = [GRX, GRX_spectral, GRX_spectral_pca_hw, GRX_spectral_dete_georeg, GRX_spectral_pca_hw_dete_georeg, LRX, LRX_spectral, LRX_spectral_pca_hw, LRX_spectral_dete_georeg, LRX_spectral_pca_hw_dete_georeg, CRD, CRD_spectral, CRD_spectral_pca_hw, CRD_spectral_dete_georeg, CRD_spectral_pca_hw_dete_georeg, frft_rx, frft_rx_spectral, frft_rx_spectral_pca_hw, frft_rx_spectral_dete_georeg, frft_rx_spectral_pca_hw_dete_georeg]

"""
frft_rx = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "FrFT_RX_sw"]
frft_rx_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "FrFT_RX_sw"]

frft_rx_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "FrFT_RX_sw"]
frft_rx_spectral_pca_hw_georeg = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "geometric_registration", "FrFT_RX_sw"]

lrx_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "LRX_sw"]
lrx_spectral_pca_hw_georeg = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "geometric_registration", "LRX_sw"]

crd_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CRD_sw"]
crd_spectral_pca_hw_georeg = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "geometric_registration", "CRD_sw"]

pca_sw_ = ["x", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "x"]
mnf = ["x", "x", "x", "x", "x", "x", "x", "MNF", "x", "x"]
ica = ["x", "x", "x", "x", "x", "x", "x", "ICA", "x", "x"]
frft_rx_spectral_pca_sw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "FrFT_RX_sw"]
frft_rx_spectral_MNF = ["spectral_binning", "x", "x", "x", "x", "x", "x", "MNF", "x", "FrFT_RX_sw"]
frft_rx_spectral_ICA = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "FrFT_RX_sw"]

anomaly_sw_pipelines = [frft_rx, frft_rx_spectral, frft_rx_spectral_pca_hw, frft_rx_spectral_pca_hw_georeg, lrx_spectral_pca_hw, lrx_spectral_pca_hw_georeg, crd_spectral_pca_hw, crd_spectral_pca_hw_georeg, pca_sw_, mnf, ica, frft_rx_spectral_pca_sw, frft_rx_spectral_MNF, frft_rx_spectral_ICA]
"""

############### Pipeline vector: ###############

pipeline_vec = compression_pipelines
pipeline_vec = classification_pipelines
pipeline_vec = targetAnomalyHW_pipelines
pipeline_vec = target_sw_pipelines
pipeline_vec = anomaly_sw_pipelines

pipeline_vec = []
for i in range(0, len(compression_pipelines)):
	pipeline_vec.append(compression_pipelines[i])
for i in range(0, len(classification_pipelines)):
	pipeline_vec.append(classification_pipelines[i])
for i in range(0, len(targetAnomalyHW_pipelines)):
	pipeline_vec.append(targetAnomalyHW_pipelines[i])
for i in range(0, len(target_sw_pipelines)):
	pipeline_vec.append(target_sw_pipelines[i])
for i in range(0, len(anomaly_sw_pipelines)):
	pipeline_vec.append(anomaly_sw_pipelines[i])




"""
p1_c1 = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"] #infeasable sample
p2_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CCSDS123_B1_hw"]
p3_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CCSDS123_B1_hw"]
p4_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B1_hw"]
p5_c1 = ["spectral_binning", "x", "x", "smile_and_keystone", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "x", "CCSDS123_B1_hw"]
p6_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "radiometric_calibration", "PCA_hw", "x", "CCSDS123_B1_hw"]
p7_c1 = ["spectral_binning", "x", "x", "smile_and_keystone", "mean_threshold_detection", "nearest_neighbour_correction", "radiometric_calibration", "PCA_hw", "x", "CCSDS123_B1_hw"]

p8_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_sw", "x", "CCSDS123_B1_hw"]
p9_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_sw", "x", "CCSDS123_B1_hw"]
p10_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "ICA", "x", "CCSDS123_B1_hw"]
p11_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "ICA", "x", "CCSDS123_B1_hw"]
p12_c1 = ["spectral_binning", "x", "x", "x", "x", "x", "x", "MNF", "x", "CCSDS123_B1_hw"]
p13_c1 = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "MNF", "x", "CCSDS123_B1_hw"]



compression_vec = [p0, p1_c1, p2_c1, p3_c1, p4_c1, p5_c1, p6_c1, p7_c1] #, p8_c1, p9_c1, p10_c1, p11_c1, p12_c1, p13_c1 \
					#p1_c2, p2_c2, p3_c2, p4_c2, p5_c2, p6_c2, \
					#p1_c3, p2_c3, p3_c3, p4_c3, p5_c3, p6_c3, p7_c3, p8_c3, \
					#p1_c4, p2_c4, p3_c4, p4_c4, p5_c4, p6_c4, p7_c4, p8_c4, p9_c4, p10_c4, p11_c4, p12_c4 \
					#]


"""