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
    if total <= 0:  # if total is 0 or less, return 0 coins needed
        return 0
    if len(coins) == 0:  # if no coins, return -1 (can't make change)
        return -1
    coins = sorted(coins, reverse=True)  # sort coins in descending order
    dynamic = [float('inf')] * (total + 1)
    dynamic = {}  # initialize dynamic programming dictionary
    while total is not None:
        for coin in coins:
            if total % coin == 0:
                dynamic[coin] = total / coin
                return(int(sum(dynamic.values())))
            else:
                dynamic[coin] = total // float(coin)
                total -= (coin * dynamic[coin])
        return -1
