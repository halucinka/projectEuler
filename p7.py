#!/usr/bin/env python3
import math

def is_prime(n):
    output = True;
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if (n%i == 0):
            output = False
    return output

counter = 0
prime = 1
while (counter < 10001):
    prime += 1
    while (is_prime(prime) == False):
        prime += 1
    counter += 1

print(prime)
