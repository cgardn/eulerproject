# Project Euler Problem 9
# Created 5-8-2014

import numpy as np
import sys

def isTrip(a,b,c):
    return a**2 + b**2 == c**2


def euclidTriples(m,n):

    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2

    return a,b,c


def sumSolve(a,b,c):
    
    if len(a) != len(b) or len(b) != len(c):
        print "Inputs must be same length"
        sys.exit(0)
           
    for i in np.arange(len(a)):
        for item in np.arange(1,201):
            if 1000. / (np.sum([a[i],b[i],c[i]]) * item) == 1:
                return (a[i],b[i],c[i]), item
    return None, None


def main():

    m = np.arange(4,54)
    n = np.arange(1,51)

    a,b,c = euclidTriples(m,n)

    (asolve, bsolve, csolve), k = sumSolve(a,b,c)

    if k is None:
        sys.exit(0)

    if isTrip(asolve*k, bsolve*k, csolve*k):
        if (asolve*k)**2 + (bsolve*k)**2 == (csolve*k)**2:
            s = "a = " + str(asolve*k) + '\n'
            s += "b = " + str(bsolve*k) + '\n'
            s += "c = " + str(csolve*k) + '\n'
            s += "k = " + str(k) + '\n'
            s += "\nabc = " + str(asolve*bsolve*csolve*(k**3))
            return s

if __name__ == '__main__':
    print main()
