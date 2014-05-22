# Project Euler Problem 2
# Created 5-2-2014

f = 0
s = 1
t = 0
sums = 0

while (s <= 4000000):
    if (s % 2) == 0:
        sums += s

    t = f + s
    f = s
    s = t

print sums
