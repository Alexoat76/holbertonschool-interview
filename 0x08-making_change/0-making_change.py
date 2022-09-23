#!/usr/bin/python3
"""
Defines function that determines the fewest number of coins to make change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total
    parameters:
        coins [list or positive ints]:
            the values of the coins in your possession
            you can assume you have an infinite number of coins of all values
        total [int]:
            total amount of change to make
            if total is 0 or less, return 0
    returns:
        the fewest number of coins to make the change
        or -1 if the total change cannot be made with the given coins
    """
    if total <= 0:
        return 0

    placeholder = total + 1

    memo = {0: 0}

    for i in range(1, total + 1):
        memo[i] = placeholder

        for coin in coins:
            current = i - coin
            if current < 0:
                continue

            memo[i] = min(memo[current] + 1, memo[i])

    if memo[total] == total + 1:
        return -1

    return memo[total]
