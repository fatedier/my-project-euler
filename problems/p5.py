#!/bin/env python

# Smallest multiple

div_num = [11, 12, 13, 14, 15, 16, 17, 18, 19]
increase = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

def is_valid(number):
    for i in div_num:
        if number % i != 0:
            return False
    return True

if __name__ == "__main__":
    number = increase
    while True:
        if is_valid(number):
            print(number)
            break
        else:
            number += increase
