dr1 =1/1000000
dr2 = 1/125000
freq_linux_kd = 1/2711000000
freq_pca_hw = 1/710000000
freq_hypso1 = 1/667000000
freq_sun_ws = 1/450000000
freq_anomaly = 1/2800000000
freq_fast_mpd = 1/200000000
freq_grx = 1/2.8e9
freq_nmf = 1/3.6e9
download_rate = dr1
freq = freq_hypso1

frames = 956#1#100#956#512#100#80#64#100#956#1000#956#614#350#956
framesamples = 684#1600#245#100#684#512#300#100#64#100#684#245#684#512#350#684
bands = 1080#160#450#120#189#120#224#126#175#169#189#200#120#1080#450#1080#120#1216#224#1080
bands_1_reduction = 120
bands_2_reduction = 20
binningfactor = 9
camera_linse_binning = -1
whatToBin = "frames"
num_regions = 80
bad_samples = 600
neigbourlevel = 2
cardinal = 1
reducedbands = 3#24#10
iterations = bands
frame_increase_factor = 2
framesample_increase_factor = 2
outer_window = 13*13
inner_window = 9*9
P = 12
D = 4
dot_product_blocks = 1 #framesamples
kernel_element = 9
fractional_domains = 10
num_neighbours = outer_window-inner_window # 15*15-3*3
num_classes = 9#4 
total_num_support_vectors = 4757#1096
x_ = 0
