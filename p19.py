#!/usr/bin/env python3

nl = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5, 1]   #cez 31 to je +3, cez 30 to je +2
l = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6, 2]
#Jan 1, 1990 = Monday, so Jan 1, 1991 = Tuesday
x = 1
output = 0
for i in range (1901, 2001):
    if (((i%4 == 0) & (i%100 != 0)) | (i%4 == 0) & (i%400 == 0)): #leap
        for j in range(0, len(l)-1):
            if ((x + l[j])%7 == 6):
                output += 1
        x += l[len(l)-1]
    else:#non-leap
        for j in range(0, len(nl)-1):
            if ((x + nl[j])%7 == 6):
                output += 1
        x += nl[len(nl)-1]

print(output)
