#!/usr/bin/env python3
import math
output = 0
max = 0
for p in range (1, 1001):
    c = 0
    for a in range(1, p):
        for b in range(1, p-a):
            if (a*a + b*b == (p-b-a)*(p-b-a)):
                c += 1
    if (c > max):
        max = c
        output = p
print (output)
