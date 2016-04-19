#!/usr/bin/env python3
from math import log, floor, sqrt

f0=0
f1=1

while (f0 < 4000000):
    f1 = f0+f1
    f0 = f1-f0
    print(f1)

print(floor((f1-1)/2))
