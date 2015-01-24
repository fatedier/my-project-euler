#!/bin/env python

# Largest palindrome product

def is_palindrome(number):
    str_num = str(number)
    left = 0
    right = len(str_num) - 1
    while left < right:
        if str_num[left] != str_num[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

if __name__ == "__main__":
    digit_of_number = 3
    max_number = ["0"] * (digit_of_number + 1)
    max_number[0] = "1"
    max_number = int("".join(max_number))
    max_palindrome = 0
        
    for i in range(max_number/2, max_number)[::-1]:
        for j in range(max_number/10, i)[::-1]:
            if (is_palindrome(i * j) == True) and (i * j > max_palindrome):
                max_palindrome = i * j
                break

    print(max_palindrome)
