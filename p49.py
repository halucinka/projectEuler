#!/usr/bin/env python3
import math

def is_prime(x):
    output = True;
    for j in range(2,int(math.floor(math.sqrt(x))+1)):
        if (x%j == 0):
            output = False
    return output

big_number = 10000
array = [1] * big_number
for i in range(2, big_number):
    if (i%10000 == 0):print(i)
    if (is_prime(i)):
        j = 2
        while (j*i < big_number):
            array[j*i] = 0
            j += 1
ones = 0
for i in range(2, big_number):
    if ((array[i] == 1) & (i>999)):
        ones +=1
primes = [0 for i in range(ones)]
p = 0
for i in range(2, big_number):
    if ((array[i] == 1) & (i>999)):
        primes[p] = i
        p +=1

print(primes)

set_primes = set()
for i in range(1, len(primes)):
    set_primes.add(primes[i])

for i in range(0, len(primes)-1):
    for j in range(i+1, len(primes)):
            if (primes[j]+primes[j]-primes[i] in set_primes):
                digits1 = set()
                digits2 = set()
                digits3 = set()
                for k in range(0, 4):
                    digits1.add(str(primes[j])[k])
                for k in range(0, 4):
                    digits2.add(str(primes[i])[k])
                for k in range(0, 4):
                    digits3.add(str(2*primes[j]-primes[i])[k])
                if ((digits1 == digits2) & (digits2 == digits3)):
                    print(primes[i], primes[j], primes[j]+primes[j]-primes[i])
