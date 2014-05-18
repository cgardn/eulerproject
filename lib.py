# Utility functions for Project Euler
# Created 5-16-2014
# TODO make it work for 3,5
# TODO modify to use sieve of eratosthenes

import numpy as np

def nextprime(maxnum):
    """
    Returns next prime number in order from 2 to maxnum
    """

    sumrange = np.arange(7,maxnum,2)
    testrange = np.arange(3,maxnum,2)

    yield 2
    yield 3
    yield 5
    for i in sumrange:
        
        spot = np.floor(np.sqrt(i))
        if spot % 2 == 0:
            adjust = 1
        else:
            adjust = 0

        loc = np.where(testrange==(spot+adjust))
            
        if len(testrange[i % testrange[:loc[0]+1] == 0]) > 0:
            continue
        else:
            yield i
