#!/usr/bin/env python3
output = 0
for a in range(1, 1000):
    for b in range(a, 1000 - a):
        if (a*a+b*b == (1000 - a - b)*(1000 - a - b)):
            output =  a*b*(1000 - a - b) #we assume thet there is exactly one solution
print(output)
