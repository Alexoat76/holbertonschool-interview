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
    if len(coins) == 0:
        return -1
    else:
        from math import trunc
        """
        sort coins in ascending order (smallest to largest)
        """
    coins = sorted(coins, reverse=True)
    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0
    while total is not None:
        for coin in coins:
            if total % coin == 0:
                dynamic[total] = total // coin
                return(dynamic[total])
            else:
                dynamic[total] = trunc(total / coin)
                total -= (dynamic[total] * (coin - 1))
        return -1
