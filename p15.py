#!/usr/bin/env python3

#40 over 20
mul = 1
for i in range (40, 20, -1):
    mul *= i
for i in range(1, 21):
    mul //= i

print(mul)
