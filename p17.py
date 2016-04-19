#!/usr/bin/env python3

a1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
a10 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
a20 = ['twenty', 'thirty', 'forty','fifty','sixty', 'seventy', 'eighty', 'ninety']
hundred = 7
thousand = 8
anditko = 3
one_to_9 = 0
one_to_99 = 0
ty = 0
teen = 0
output = 0
for i in range(1, 20):
    if i < 10:
        one_to_9 += len(a1[i])
    else:
        teen += (len(a10[i-10]))
for i in range(0, len(a20)):
    ty += len(a20[i])
one_to_99 = ty * 10 + 8 * one_to_9 + + one_to_9 + teen
print(one_to_9)
print(one_to_99)
output = one_to_99 + 100 * (one_to_9  + 9 * hundred) + (900-9)*anditko + 9 * (one_to_99) + 3 + thousand

print(output)
