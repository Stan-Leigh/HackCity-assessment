"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

"""

import re


def nsteps(num):
    number = num
    steps = 0
    
    while number > 0:
        # check if number is even
        if number % 2 == 0:
            number = number / 2
            steps += 1
        # else it is odd
        else:
            number -= 1
            steps += 1
    
    return steps

# Test function with test cases
test1 = nsteps(14)
test2 = nsteps(8)
test3 = nsteps(123)

print(test1)
print(test2)
print(test3)
