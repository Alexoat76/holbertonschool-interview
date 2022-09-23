#!/usr/bin/python3
"""
Defines function that determines the fewest number of coins to make change
"""


def makeChange(coins: int, total: int) -> int:
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
    dynamic = [0] + [float('inf')] * total
    for coin in coins:
        for i in range(coin, total + 1):
            dynamic[i] = min(dynamic[i], dynamic[i - coin] + 1)
    return dynamic[total] if dynamic[total] != float('inf') else -1
