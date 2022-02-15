import numpy as np
import statistics as st
import matplotlib.pyplot as plt

def timesamples_from_file_to_array_interface(filePath):
    #Open file:
    with open(filePath, "r") as f:
        
        #make integer timeduration list:
        file_lines=[line.split() for line in f]     
       
        #file_lines[0] = sample input complexity (x)
        #file_lines[1] = sample time (y)
        x = [float(row[0]) for row in file_lines]
        y = [float(row[1]) for row in file_lines]
    
    x_complex = []
    for i in range (0, len(x)):
        #cubeSize = x[i]**2
        #complexity = x[i]**3
        numOperations = x[i]*(x[i]*(x[i]*1+1+1)+1)+1 
        x_complex.append(numOperations)

    f.close()
    return x, x_complex, y


def mean_and_standard_deviations(x, y):
    i = 0
    arr = []
    means = []
    std_neg = []
    std_pos = []
    xs = []
    while(i < len(x)-1):
        while (i+1 < len(x) and x[i+1]==x[i]):
            arr.append(y[i])
            i+=1;
        xs.append(x[i])
        means.append(np.mean(arr))
        std = st.stdev(arr)
        std_neg.append(np.mean(arr) - std)
        std_pos.append(np.mean(arr) + std)
        arr.clear()
        i+=1

    return xs, means, std_neg, std_pos

def regressionLine(x, y, endValue):
    #p = np.polyfit(x, y, 3)
    p = np.polyfit(x, y, 2)
    #p = np.polyfit(x, y, 1)
    
    x_new = []
    y_new = []
    for i in range(100, endValue, 100):
        x_new.append(i)
        #y_sample = p[0]*i**4 + p[1]*i**3 + p[2]*i**2 + p[3]*i + p[4]
        #y_sample = p[0]*i**3 + p[1]*i**2 + p[2]*i**1 + p[3]
        y_sample = p[0]*i**2 + p[1]*i**1 + p[2]
        #y_sample = p[0]*i**1 + p[1]
        y_new.append(y_sample)

    return x_new, y_new


filePath = "alotOfSamples.txt"
testTimeStamps = "testTimeStamps.txt"
x, x_complex, y = timesamples_from_file_to_array_interface(filePath)
xs, means, std_neg, std_pos = mean_and_standard_deviations(x, y)
xs_c, means_c, std_neg_c, std_pos_c = mean_and_standard_deviations(x_complex, y)

endValue = 900
endValue_c = 600000000
reg_x, reg_y = regressionLine(xs, means, endValue)
reg_x_c, reg_y_c = regressionLine(xs_c, means_c, endValue_c)

#x2, y2 = timesamples_from_file_to_array_interface(filePath)


plt.plot(x, y, 'o', color="blue")
plt.plot(xs, means, color="red")
plt.plot(xs, std_neg, color="green")
plt.plot(xs, std_pos, color="yellow")
# regression line
plt.plot(reg_x, reg_y, color = "black")
plt.show()


plt.plot(x_complex, y, 'o', color="blue")
plt.plot(xs_c, means_c, color="red")
plt.plot(xs_c, std_neg_c, color="green")
plt.plot(xs_c, std_pos_c, color="yellow")
# regression line
plt.plot(reg_x_c, reg_y_c, color = "black")
plt.show()
