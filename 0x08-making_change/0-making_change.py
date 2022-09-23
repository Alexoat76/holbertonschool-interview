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
    # initialize dynamic programming list with inf values
    dynamic = [float('inf') for _ in range(total + 1)]
    dynamic[0] = 0  # base case: 0 coins needed to make 0 change
    for i in range(len(dynamic)):
        for coin in coins:
            if i - coin >= 0:
                dynamic[i] = min(dynamic[i], dynamic[i - coin] + 1)
    if dynamic[-1] == float('inf'):
        return -1
    return dynamic[-1]
