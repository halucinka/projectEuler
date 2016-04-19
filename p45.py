#!/usr/bin/env python3
import math

triangle = set()
pentagonal = set()
hexagonal = set()
big_number = 10000000000
i = 1
while (i*(i+1)/2 < big_number):
    triangle.add(i*(i+1)/2)
    if (i*(3*i-1)/2 < big_number):
        pentagonal.add(i*(3*i-1)/2)
    if (i*(2*i-1) < big_number):
        hexagonal.add(i*(2*i-1))
    i += 1
for a in hexagonal:
    if ((a in triangle) & (a in pentagonal)):
        print(a)
