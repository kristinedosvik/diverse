import numpy as np

def timesamples_from_file_to_array_interface(filePath):
    #Open file:
    with open(filePath, "r") as f:
        
        #Skip first two lines:
        f.readline()
        f.readline()

        #make integer timeduration list:
        file_lines=[line.split() for line in f]     
       
        #file_lines[0] = sample number
        #file_lines[1] = sample
        samples = [int(row[1]) for row in file_lines]
        
    f.close()
    return samples

filePath = "timeSamples.txt" 
print(file_to_array_interface(filePath))


