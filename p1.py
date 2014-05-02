import numpy as np

a = np.arange(1000)

b = np.mod(a,3) == 0
c = np.mod(a,5) == 0
d = np.mod(a,15) == 0

print np.sum(a[b]) + np.sum(a[c]) - np.sum(a[d])
