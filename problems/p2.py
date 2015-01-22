#!/bin/env python

# Even Fibonacci numbers

def get_even_num(number):
    return number % 2 == 0;

fib = [1, 2];
new_number = fib[0] + fib[1];

while new_number <= 4000000:
    fib.append(new_number);
    new_number = fib[-1] + fib[-2];

print( sum( filter(get_even_num, fib) ) );
