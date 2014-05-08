# Project Euler Problem 8
# Created 5-8-2014
#
# The data file referenced here is the problem number set as a text file

import numpy as np

def main():
    # Reading data file
    with open('data') as f:
        a = f.read().strip()

    # Any 5 consecutive numbers containing a 0 will multiply to 0.
    # Therefore, we can split the number set by 0's and throw away any
    # resulting sets that have less than 5 numbers, as they would have
    # contained a 0

    # Splitting by 0
    a = a.split('0')

    # Sorting by length
    a.sort(key=lambda x: len(x))

    # Throwing away sets with length < 5
    for item in range(len(a)):
        if len(a[item]) < 5:
            ind = item
    del a[:ind+1]

    # Mapping each set to a list of ints
    for i in range(len(a)):
        a[i] = map(int, a[i])

    # Finding the max 5-number product
    maxprod = 0
    for numlist in a:
        rounds = len(numlist)-4
        b = np.array(numlist)
        for i in range(rounds):
            if maxprod < np.cumprod(b[i:i+5])[-1]:
                maxprod = np.cumprod(b[i:i+5])[-1]

    return maxprod

if __name__ == '__main__':
    print main()
