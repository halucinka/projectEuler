#!/usr/bin/env python3
import math


output = 1
i = 3
lu = 7
ru = 9
ld = 5
rd = 3
diag = 1+3+5+7+9
while i < 1001:
    i += 2
    rd = ru + i-1
    ld = rd + i-1
    lu = ld + i-1
    ru = lu + i-1
    diag += ru + rd + lu + ld
print(diag)
