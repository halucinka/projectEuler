#!/usr/bin/env python3
import math

phi = (1 + math.sqrt(5)) / 2
def n_fib(n):
    f = math.floor(pow(phi, n)/math.sqrt(5) + 1 / 2)
    return f

def figures(n):
    n = str(n)
    output = 0
    for i in range (0, len(n)):
        output += int(n[i])
    return output
n = 1
while (figures(n_fib(n)) < 1000):
    n += 40

while (figures(n_fib(n)) < 1000):
    n += 1

print (n_fib(n))
