#!/usr/bin/env python3
import math

big_number = 100000000
pentagonal = set()
i = 1
while (i*(3*i-1)/2 < big_number):
    pentagonal.add(i*(3*i-1)/2)
    i += 1

for a in pentagonal:
    for b in pentagonal:
        if ((a+b in pentagonal) & (abs(a-b) in pentagonal)):
            print("a ", a)
            print("b ", b)
            print("a-b ", abs(a-b))
