#!/usr/bin/env python3
import math

def is_prime(x):
    output = True;
    for j in range(2,int(math.floor(math.sqrt(x))+1)):
        if (x%j == 0):
            output = False
    return output

def prime_factors(n):
    factors = set()
    i = 2
    m = n
    while (i <= m):
        if ((is_prime(i)) & (m%i == 0)):
            factors.add(i)
            m /= i
        i += 1
    return factors

for i in range(134000, 300000):
    first = prime_factors(i)
    if len(first) == 4:
        #print("first was 4")
        o = 0
        for k in range(1, 4):
            #print("k ", k)
            other = prime_factors(i+k)
            #print(other)
            #print("other prime factors", other)
            if (len(other) == 4):
                o += 1
        if (o == 3):
            print("TUUUUUUUUUUUUUUUUUUUUuuuuuuuuuuuuuuuuuuuuuu",i)
