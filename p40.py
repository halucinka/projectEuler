#!/usr/bin/env python3
import math

mul = 1

i = 0

def z(a):
    return (int(math.log10(a))+1)
dig = 1

output = 1
for p in range(1, 7):
    add = 0
    index = pow(10, p)
    print("index ", index)
    add = (pow(10, dig) - pow(10, dig-1))*dig
    while (i + add < index):
        #print("som so while: i ", i, "add ", add)
        i += add
        #print("pricitane add k i", i)
        dig += 1
        add = pow(10, dig) - pow(10, dig-1)
        #print("nove add ", add)
        #print("dig ", dig)
    output *= int(str((index - i)//dig + pow(10, dig-1))[(index - i) % dig -1])
    #print("index-i)//dig ", (index-i)//dig)
print(output)
