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


big_number = 10000
array = [1] * big_number
for i in range(2, big_number):
    if (i%1000 == 0):print(i)
    if (is_prime(i)):
        j = 2
        while (j*i < big_number):
            array[j*i] = 0
            j += 1
ones = 0
for i in range(2, big_number):
    if (array[i] == 1):
        ones +=1
primes = [0 for i in range(ones)]
p = 0
for i in range(2, big_number):
    if array[i] == 1:
        primes[p] = i
        p +=1

#    print(primes)

i = 1
flag = False
while flag == False:
    #if (i%100 == 0): print(i)
    i += 1
    ok = False
    p = 0
    if (is_prime(i) | (i % 2 == 0)):
        ok = True
    else:
        while (primes[p] < i):
            if (math.sqrt((i-primes[p])/2)== math.floor(math.sqrt((i-primes[p])/2))):
                ok = True
                #print("OKKKKKKKKKKKKKK")
            p += 1
    if (ok == False):
        print(i)
        flag = True
