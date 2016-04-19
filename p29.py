#!/usr/bin/env python3
import math

numbers =set()
for a in range(2, 101):
    for b in range(2, 101):
        numbers.add(math.pow(a, b))
print(len(numbers))
