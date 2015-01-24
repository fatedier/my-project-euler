#!/bin/env python

# 10001st prime

import math

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = 1
    prime_index = 1
    while prime_index < 10001:
        number += 2
        if is_prime(number):
            prime_index += 1
    
    print(number)
