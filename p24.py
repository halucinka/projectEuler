#!/usr/bin/env python3
import math


def find_minimum(x, n):
    output = -1
    i = 0
    poc = 0
    while poc < n:
        if (x[i] == -1):
            poc += 1
        i +=1

    return i-1

number = 1000000
i = 10
a = [-1 for i in range(0, 10)]
b = [-1 for i in range(0, 10)]
'''while (number > 1):
    factorial = math.factorial(i-1)
    while factorial >= number:
        c = find_minimum(b)
        print("c ", c)
        a[10-i] = c
        b[c] = 1
        factorial //= i
        i -=1
    print(a)
    print("fac ", factorial)
    figure = number // factorial
    print(figure)
    number -= figure * factorial
    print(number)
    a[10-i] = find_minimum(b)+figure
    print(find_minimum(b) + figure)
    b[find_minimum(b)+figure] = 1

'''

i = 9
while number > 0:
    factorial = math.factorial(i)
    c = find_minimum(b, math.ceil(number/factorial))

    a[9-i] = c
    b[c] = 1

    number = number - (number//factorial) * factorial
    i -=1

for j in range(9, -1, -1):
    if (b[j] == -1 ):
        a[9-i] = j
        i-=1

print(a)
