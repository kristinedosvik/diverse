import matplotlib.pyplot as plt

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


def make_MVU(svu_graphs, weights, sample, check_sensibility):

    svu0_x = sample[1]
    svu1_x = sample[2]

    svu0_y = make_SVU(svu_graphs[0], svu0_x)
    svu1_y = make_SVU(svu_graphs[1], svu1_x)
    mvu = svu0_y*weights[0] + svu1_y*weights[1]

    if (check_sensibility==1):
        print("sample: ", sample)
        print("svu0_y: ", svu0_y)
        print("svu1_y: ", svu1_y)
        print("mvu: ", mvu)
        print()
    
    return mvu

def plot_MVUs(svu_graphs, weights, samples):
    x = []
    y = []
    for i in range(0, len(samples)):
        x.append(samples[i][3])       
        mvu = make_MVU(svu_graphs, weights, samples[i], 0)
        y.append(mvu)
    plt.plot(x, y, "o")
    plt.show()

def plot_color_by_design(svu_graphs, weights, samples, group_nr, group, group_colors):
    
    plot_group = []
    for i in range(0, len(group)):
        plot_group.append([])


    for i in range(0, len(samples)):
        cost = samples[i][3]  
        mvu = make_MVU(svu_graphs, weights, samples[i], 0)
        sample = [cost, mvu]

        algorithm_nr = group.index(samples[i][0][group_nr])
        plot_group[algorithm_nr].append(sample)
    
    for i in range(0, len(group)):

        x = [row[0] for row in plot_group[i]]
        y = [row[1] for row in plot_group[i]]
        plt.plot(x, y, "o", color = group_colors[i])
    plt.show()




_2D = 1000
raw = 10*_2D
   
svu0_graph = [[40,0],[70,0.5],[100,1]]

svu1_graph = [[_2D,1], [_2D*3, 0.9], [raw/2, 0.2], [raw, 0]]

svu_graphs = [svu0_graph, svu1_graph]
weights = [0.3, 0.7]

g0 = ["binning", "x"]
g1 = ["dimRed_pca", "dimRed_enm", "x"]
g2 = ["tarDet", "anomDet", "x"]

group_colors = ["red", "yellow", "green", "blue", "pink", "grey", "purple", "brown", "black", "lime"]

pipeline1 = [g0[0], g1[0], g2[0]]
pipeline2 = [g0[1], g1[2], g2[1]]
pipeline3 = [g0[0], g1[0], g2[2]]
pipeline4 = [g0[0], g1[1], g2[0]]
pipeline5 = [g0[1], g1[1], g2[0]]
pipeline6 = [g0[0], g1[2], g2[1]]
pipeline7 = [g0[1], g1[1], g2[2]]


samples = [[pipeline2, 30, _2D, 12], [pipeline3, 40, _2D, 55], [pipeline4, 60, _2D*2, 7], [pipeline5, 70, _2D*6, 32], [pipeline6, 100, raw, 19], [pipeline7, 110, _2D*4, 26]]

print(samples)

mvu = make_MVU(svu_graphs, weights, samples[1], 1)

#plot_MVUs(svu_graphs, weights, samples)
plot_color_by_design(svu_graphs, weights, samples, 1, g1, group_colors)



