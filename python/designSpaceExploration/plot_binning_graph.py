import matplotlib.pyplot as plt
import numpy as np


graph_res_dec = [[0,1],[1,1],[2,0.95],[3,0.85],[4,0.65],[5,0.40],[6,0.01],[100,0]]

def resolution_estimation(graph, sample):
    
    val = 1

    for i in range(1, len(graph)): #skal ikke denne først sjekke 40 så 60?
        if(sample < graph[i][0] and sample >= graph[i-1][0]):
            a = (graph[i][1] - graph[i-1][1])/(graph[i][0] - graph[i-1][0])
            val = a*sample + graph[i-1][1] - a*graph[i-1][0]
        
    if(sample > graph[-1][0]):
        val = 0
    val

    return val




def spatial_binning_resolution(num_samples, binningfactor):
    graph_spat = [[1,num_samples]]
    for i in range(1,int(np.ceil(np.log2(num_samples))+1)):
        graph_spat.append([2**(i),num_samples/2**i])

    
    #x_spat = [row[0] for row in graph_spat]
    #y_spat = [row[1] for row in graph_spat]

    #plt.plot(x_spat,y_spat)
    #plt.show()

#spatial_binning_resolution(956)


def spectral_binning_resolution(num_samples, binningfactor):
    graph_spec = [[0, num_samples], [9, num_samples]]

    for i in range(1,int(np.ceil(np.log2(num_samples/9))+1)):
        graph_spec.append([9*2**i,num_samples/2**i])


    #x_spec = [row[0] for row in graph_spec]
    #y_spec = [row[1] for row in graph_spec]

    #plt.plot(x_spec,y_spec)
    #plt.show()

#spectral_binning_resolution(1080)

def snr_factor_spatial(b):    
    return 120*np.log(b)+110

print("spec")
print(spectral_binning_resolution(1084, 5))
print(spectral_binning_resolution(1084, 9))
print(spectral_binning_resolution(1084, 17))
print(spectral_binning_resolution(1084, 18))
print(spectral_binning_resolution(1084, 20))
print("spat")
print(spatial_binning_resolution(1084, 5))
print(spatial_binning_resolution(1084, 9))
print(spatial_binning_resolution(1084, 17))
print(spatial_binning_resolution(1084, 18))
print(spatial_binning_resolution(1084, 20))
print(spatial_binning_resolution(1084, 200))
print(spatial_binning_resolution(1084, 400))


x = []
y = []
for i in range(0, 30):
    x.append(i)
    y.append(snr_factor_spatial(i))
plt.plot(x,y, color="grey")
#plt.show()
plt.savefig("binning_snr.png")


graph_res_dec = [[0,1],[1,1],[2,0.90],[3,0.80],[4,0.60],[5,0.30],[5,0.01],[6,0],[30,0]]
x_ = [row[0] for row in graph_res_dec]
y_ = [row[1] for row in graph_res_dec]

plt.plot(x_,y_, color="grey")
#plt.show()
plt.savefig("binning_res.png")

x_tot = []
y_tot = []

w_snr = 0.0004
w_res = 1

for i in range(0,30):
    x_tot.append(i)
    res = resolution_estimation(graph_res_dec, i)
    y_tot.append(w_snr*snr_factor_spatial(i) + w_res*res)

#plt.grid()
plt.plot(x_tot,y_tot, color="grey")
plt.savefig("binning_0.0004snr_res.png")
#plt.show()