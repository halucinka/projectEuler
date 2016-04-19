#!/usr/bin/env python3
mul = 1
for i in range(1, 101):
    mul *= i

mul = str(mul)
output = 0
for i in range (0, len(mul)):
    output += int(mul[i])

print(output)
