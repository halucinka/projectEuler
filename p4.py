#!/usr/bin/env python3
import math

def size(n):
    output = -1
    if (n <= 0):
                output = 0
    else:
        output = int(math.log(n,10)+1)
    return output

def is_palindrome(n):
    str_n = str(n)
    output = True
    for i in range (0, int(math.floor(len(str_n)/2))):
        if str_n[i] != str_n[len(str_n)-i-1]:
            output = False
    return output

output = 1;
for i in range(100, 1000):
    for j in range(i, 1000):
        if (is_palindrome(i*j) & (i*j>output)):
            output = i*j

print(output)
