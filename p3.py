# Project Euler Problem 3
# Created 5-2-2014

import sys
import numpy as np

n = int(sys.argv[1])

f = 2

if n % 2 == 0:
    n = n/2
    lf = 2
    while n % 2 == 0:
        n = n/2
    else:
        lf = 1

f=3
mf = np.sqrt(n)
while n>1 & f <= mf:
    print str(n) + "   |   " + str(f)
    if n % f == 0:
        n = n/f
        lf = f
        while n % f == 0:
            n = n/f
        mf=np.sqrt(n)
    f += 2

if n == 1:
    print lf
else:
    print n
