#!/bin/env python

# Sum square difference

def get_sum_of_square(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i * i
    return sum

def get_square_of_sum(number):
    val = sum(range(1, number + 1))
    return val * val

if __name__ == "__main__":
    result = abs(get_sum_of_square(100) - get_square_of_sum(100))
    print(result)
