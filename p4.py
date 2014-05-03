# Project Euler Problem 4
# Created 5-2-2014

import numpy as np

def pdetect(n):
    n = str(n)
    l = len(n)
    if l%2 == 0:
        if n[l/2:] == n[:l/2][::-1]:
            return True
    else:
        if n[:l/2] == n[l/2+1:][::-1]:
            return True
    return False

def main():
    for i in range(900,1000)[::-1]:
        for j in range(900,1000)[::-1]:
            if pdetect(i*j):
                print i*j
                return

if __name__ == '__main__':
    main()
