import numpy as np

x = [-2.1, -1,  4.3]
y = [3,  1.1,  0.12]
C = np.stack((x, y), axis=0)

print(np.cov(x))
print(np.cov(y))
print(np.cov(C))
