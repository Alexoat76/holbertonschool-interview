#!/usr/bin/python3

# set recursion limit
from sys import setrecursionlimit

"""
This module contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
Prototype: `minOperations(n)`
Returns: integer
if n is impossible to achieve, returns 0
"""


# Function to calculate the fewest number of operations
def minOperations(n):  # n is the number of H characters in the file

    setrecursionlimit(10**6)  # set recursion limit to 10^6

    operations = 0  # number of operations given the current number of H characters
    inc = 2   # 3 4 5 6 etc. are the possible values of n

    # factor = 2
    # no even division (prime) inc = n

    if type(n) is not int or n < 2:
        return 0  # n is not a valid input (not an integer or less than 2)

    while n != 1:
        if n % inc == 0:
            operations += inc  # 1
            n /= inc
            inc = 1  # resets for next loop
        inc = inc + 1

    return operations # number of operations needed to achieve n H characters
