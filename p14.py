#!/usr/bin/env python3
big_number = 1000001
a = [0 for i in range(0,big_number)]
a[1] = 1
for i in range(1, big_number):
    n = i
    counter = 1
    while (n > 1):
        if (int(n)%2 == 0):
            n /= 2
            if (int(n)<big_number):
                if (a[int(n)] > 0):
                    a[i] = a[int(n)] + counter
                    n = 1
                else:
                    counter += 1
            else: counter += 1
        else:
            n = 3 * n + 1
            counter += 1


output = -1
max = -1
for i in range(1, big_number):
    if (a[i] > max):
        max = a[i]
        output = i
#print(a)
print(output)
