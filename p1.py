#!/usr/bin/env python3

output = 0
for i in range(1,1000):
	if (i%3 == 0) | (i%5 == 0):
		output = output + i

print(output)
