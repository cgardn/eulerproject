# Project Euler Problem 10
# Created 5-16-2014

import lib
import sys
import numpy as np

def main(maxnum):

    s = 0
    arr = np.arange(2,maxnum)

    for prime in lib.nextprime(maxnum):
        s += prime
    print(s)

if __name__ == '__main__':
    main(int(sys.argv[1]))
