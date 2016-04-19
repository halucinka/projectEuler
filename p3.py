#!/usr/bin/env python3
import math

def is_prime(n):
    output = True;
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if (n%i == 0):
            output = False
    return output

output = 0;
number = 600851475143
i = int(math.floor(math.sqrt(number)+1))
prime_factor = False
while ((i>0) & (prime_factor == False)):
    if (is_prime(i) & (number%i == 0)):
        prime_factor = True
        output = i
    if (i%10000 == 0):
        print(i)
    i = i-1
print(output)
