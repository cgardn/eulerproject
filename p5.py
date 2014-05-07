# Project Euler Problem 5
# Created 5-2-2014
# Finds the highest common multiple from a given range

import sys
import p3
import numpy as np


def highmult(lowend, highend):

    s = []
    a = np.arange(int(lowend), int(highend))

    # Finding primes in the given range
    for i in a:
        if p3.factor(i) == i:
            s += [i]
    # including non-prime squares
        if (i**2 <= max(a)):
            s += [i]

    s = np.array(s)
    return np.prod(s)

if __name__ == '__main__':
    print highmult(sys.argv[1], sys.argv[2])
