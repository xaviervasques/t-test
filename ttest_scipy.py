## updated by Xavier Vasques 11/03/2019
## Import the packages
import numpy as np
from scipy import stats

## Define 2 groups with their respective data
#Sample Size
N = 10.0
#Data of group 1
a = np.array([42.1, 80.0, 30.0, 45.8, 57.7, 80.0, 82.4, 66.2, 66.9, 79.0])
#Data of group 2
b = np.array([80.7, 85.1, 88.6, 81.7, 69.8, 79.5, 107.2, 69.3, 80.9, 63.0])

t2, p2 = stats.ttest_ind(a,b)
print("t = " + str(t2))
print("p = " + str(p2))
