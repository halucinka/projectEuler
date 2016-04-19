#!/usr/bin/env python3
import math

def is_prime(x):
    output = True;
    for j in range(2,int(math.floor(math.sqrt(x))+1)):
        if (x%j == 0):
            output = False
    return output


'''big_number = 10000000
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

print(primes)
'''
primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
counter = -1
old_n = 0
add = 1
while (counter < 500):
    number = old_n + add
    old_n = number
    if (add % 1000== 0):
        print (old_n)
    #print ("nove ", number)
    prime_divisors = {}
    for i in primes:
        if ((i <= number) & (int(number)%i == 0)): #because number 2*3*5*7*11*13*17*19*23 has 2^9 = 512 divisors
            prime_divisors[i] = 1
            number /= i
            #print("i ", i)
            #print('number ', number)
            while (int(number)%i == 0):
                prime_divisors[i] += 1
                number /= i
                #print('number ', number)
            #print(prime_divisors)
    counter = 1
    #print(prime_divisors)
    for a in prime_divisors:
        #print("a", a)
        counter *= (prime_divisors[a]+1)
    add += 1
    #print("tu")
    #print(old_n)
        #print(counter)
        #print(prime_divisors)

print(old_n)
print(counter)
