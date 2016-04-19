#!/usr/bin/env python3
import math

i = 0
flag = False
while (flag == False):
    c = True
    i += 1
    first = set()
    for j in range(0, len(str(i))):
        first.add(str(i)[j])
    k = 1
#    print("i je teraaaaz ", i)
#    print("first ", first)
    while (k < 6):
        k += 1
        if (len(str(i)) == len(str(k*i))):
#            print("dlzky sedia pre k ", k)
            for j in range(0, len(str(k*i))):
#                print("str k*i j ", str(k*i)[j])
                if ((str(k*i)[j] in first) == False):
                    c = False
        else:
            c = False
    if (c == True):
        flag = True
        print(i)
