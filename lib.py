# Utility functions for Project Euler
# Created 5-16-2014

def _isprime(num):
    """
    Returns True if num is prime
    """

    if num == 2:
        return True
    elif num == 3:
        return True

    for i in range(2,num):
        if num % i == 0:
            return False
    return True
        

def nextprime():
    """
    Returns next prime number in order from 2 to maxnum
    Passing True to reset will set next prime to 2
    """

    i = 3
    yield 2
    while True:
        if _isprime(i):
            yield i
        i += 2
