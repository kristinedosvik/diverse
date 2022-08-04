

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

freq = freq_hypso1 #1/4.7e9 #freq_hypso1

frames = 956#1#100#956#512#100#80#64#100#956#1000#956#614#350#956
framesamples = 684#1600#245#100#684#512#300#100#64#100#684#245#684#512#350#684
bands = 1080#160#450#120#189#120#224#126#175#169#189#200#120#1080#450#1080#120#1216#224#1080
bands_1_reduction = 120
bands_2_reduction = 20
binningfactor = 9
camera_linse_binning = -1
whatToBin = "frames"
num_regions = 8 #num neighbors for bad pixel detection
bad_samples = 600
neigbourlevel = 2
cardinal = 1
reducedbands = 3#24#10
iterations = bands
frame_increase_factor = 1
framesample_increase_factor = 1
outer_window = 13*13
inner_window = 9*9
P = 12
D = 4
dot_product_blocks = 1 #framesamples
kernel_element = 9
fractional_domains = 10
num_neighbours = outer_window-inner_window # 15*15-3*3
num_classes = 4#9 
total_num_support_vectors = 1096#4757
absolute_error_value = 64
x_ = 0

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


