#!/usr/bin/env python3
import math

s = 1
for i in range(2, 1001):
    a = i
    for j in range(2, i+1):
        a *= i
        if (len(str(a))>12):
            a = int(str(a)[-12:])
    s += a

print(str(s)[-10:])
