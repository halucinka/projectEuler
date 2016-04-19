#!/usr/bin/env python3
import math

number = 2
power = 1
while (power < 1000):
    number = pow(number, 2)
    power *= 2

number = str(number//pow(2, 24))

output = 0
for i in range(0, len(number)):
    output += int(number[i])

print(output)
