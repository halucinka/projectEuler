#!/usr/bin/env python3
import math

def is_prime(n):
    output = True;
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if (n%i == 0):
            output = False
    return output

output = 0
number = 2000000
array = [1] * number
for i in range(2, number):
    if array[i] == 1:
        if (i%10000 == 0):
            print(i)
        if (is_prime(i)):
            output += i
            j = 2
            while (j*i < number):
                array[j*i] = 0 #it is not prime number
                j += 1
                
print(output)
