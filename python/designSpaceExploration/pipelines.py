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


############### Anomaly detection SW: ###############


GRX = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "GRX_sw"]
GRX_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "GRX_sw"]
GRX_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "GRX_sw"]
GRX_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "x", "geometric_registration", "GRX_sw"]
GRX_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "GRX_sw"]

LRX = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "LRX_sw"]
LRX_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "LRX_sw"]
LRX_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "LRX_sw"]
LRX_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "x", "geometric_registration", "LRX_sw"]
LRX_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "LRX_sw"]

CRD = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "CRD_sw"]
CRD_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "CRD_sw"]
CRD_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "CRD_sw"]
CRD_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "x", "geometric_registration", "CRD_sw"]
CRD_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "FrFT_RX_sw"]

frft_rx = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "FrFT_RX_sw"]
frft_rx_spectral = ["spectral_binning", "x", "x", "x", "x", "x", "x", "x", "x", "FrFT_RX_sw"]
frft_rx_spectral_pca_hw = ["spectral_binning", "x", "x", "x", "x", "x", "x", "PCA_hw", "x", "FrFT_RX_sw"]
frft_rx_spectral_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "x", "geometric_registration", "FrFT_RX_sw"]
frft_rx_spectral_pca_hw_dete_georeg = ["spectral_binning", "x", "x", "x", "mean_threshold_detection", "nearest_neighbour_correction", "x", "PCA_hw", "geometric_registration", "FrFT_RX_sw"]

anomaly_sw_pipelines = [GRX, GRX_spectral, GRX_spectral_pca_hw, GRX_spectral_dete_georeg, GRX_spectral_pca_hw_dete_georeg, LRX, LRX_spectral, LRX_spectral_pca_hw, LRX_spectral_dete_georeg, LRX_spectral_pca_hw_dete_georeg, CRD, CRD_spectral, CRD_spectral_pca_hw, CRD_spectral_dete_georeg, CRD_spectral_pca_hw_dete_georeg, frft_rx, frft_rx_spectral, frft_rx_spectral_pca_hw, frft_rx_spectral_dete_georeg, frft_rx_spectral_pca_hw_dete_georeg]


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

