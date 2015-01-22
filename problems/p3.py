#!/bin/env python

# Largest prime factor

"""
# method 1
import math;

def get_prime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False;
    return True;

def get_max_prime_factor(number, prime_num_list):
    for i in prime_num_list:
        while number % i == 0 and number != i:
            number = number / i;
        if number == i:
            return number;

number = 600851475143;
prime_num_list = filter(get_prime, range(2, int(math.sqrt(number) + 1)));

print(get_max_prime_factor(number, prime_num_list));
"""

# method 2
import math;

number = 600851475143;
factor = 3;
last_factor = 2;
max_factor = int(math.sqrt(number));

while number % 2 == 0 and number != 2:
    number = number / 2;
if number == 1:
    last_factor = 1;

while number > 1 and factor <= max_factor:
    if number % factor == 0:
        number = number / factor;
        last_factor = factor;
        while number % factor == 0:
            number = number / factor;
        max_factor = int(math.sqrt(number));
    factor += 2;

if number == 1:
    print(last_factor);
else:
    print(number);
