## updated by Xavier Vasques
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

## Calculate the Standard Deviation
#Calculate the variance to get the standard deviation

var_a = a.var(ddof=1.0)
var_b = b.var(ddof=1.0)

#std deviation
s = np.sqrt((var_a + var_b)/2.0)

## Calculate the t-statistics
t = (a.mean() - b.mean())/(s*np.sqrt(2.0/N))

## Compare with the critical t-value
#Degrees of freedom
df = len(a) + len(b) - 2.0

#p-value after comparison with the t
p = stats.t.cdf(t,df=df)

print("t = " + str(t))
print("p = " + str(2.0*p))


