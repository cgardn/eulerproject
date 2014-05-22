# Project Euler Problem 7
# Created 5-7-2014

import numpy as np
import p3

current = 3
count = 1
primes = np.array([2])

try:
    while len(primes) < 10001:

        if (current % np.array(primes)).all() == False:
            pass
        else:
            primes = np.hstack([primes, current])

        current += 2

    print primes[-1]
    print len(primes)
        
except:
    print "Last checked number: " + str(current)
    print "Prime count: " + str(len(primes))
