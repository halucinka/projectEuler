#!/usr/bin/env python3
import itertools
import math
pandig = list(itertools.permutations([7, 6, 5, 4, 3, 2, 1]))

def is_prime(n):
    output = True;
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if (n%i == 0):
            output = False
    return output

k = 0
for i in pandig:
    j = i[0]*1000000 + i[1]*100000  + i[2]*10000 + i[3]*1000+ i[4] *100 +i[5]*10 +i[6]
    if is_prime(j):
        print(j) # answer is the first one
    k +=1
