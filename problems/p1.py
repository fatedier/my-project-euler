#!/bin/env python

# Multiples of 3 and 5

sum = 0;
i = 1;
while i < 1000:
    if i%3 == 0 or i%5 == 0:
        sum += i;
    i += 1;

print(sum);
