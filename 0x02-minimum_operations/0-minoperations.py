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


def minOperations(n):
    """
    This is a method that calculates the fewest number of
    operations needed to result in exactly n H characters
    in the file.
    """
    result = 0
    i = 2

    if isinstance(n, int) and n < 2:
        return 0

    while i <= n + 1:
        if n % i == 0:
            result += i
            n //= i
            i = 2
        else:
            i += 1

    return result
