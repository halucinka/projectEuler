#!/usr/bin/env python3
import math
# max 6 digits
output = 0
for i in range(2, 1000000):
    s = 0
    for j in range(0, len(str(i))):
        s += (math.pow(int(str(i)[j]), 5))
    if (i == s):
        output += i

print(output)
