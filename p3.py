# Project Euler Problem 3
# Created 5-2-2014
# Returns the largest prime factor

import sys
import numpy as np


def factor(n):
    f = 2
    lf = 1
    if n % 2 == 0:
        lf = 2
        while n % 2 == 0:
            n = n/2
    else:
        lf = 1

    f = 3
    mf = np.sqrt(n)
    while n>1 & f <= mf:
        if n % f == 0:
            n = n/f
            lf = f
            while n % f == 0:
                n = n/f
            mf=np.sqrt(n)
        f += 2

    if n == 1:
        return lf
    else:
        return n

if __name__ == '__main__':
    print factor(int(sys.argv[1]))
