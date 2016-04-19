#!/usr/bin/env python3

number = 100
sum_of_powers = 0
sum_of_numbers = ((number+1)*number)/2
for i in range(1, number+1):
    sum_of_powers += i*i

print (sum_of_numbers*sum_of_numbers - sum_of_powers)
