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
    coin_dict = [float('inf')] * (total + 1)  # initialize dynamic programming list with inf values
    coin_dict = {i: float('inf') for i in range(total + 1)}  # initialize dynamic programming dict with inf values
    coin_dict[0] = 0  # set first value to 0 (no coins needed to make 0 change)
    for i in range(total + 1):  # iterate through each total value from 0 to total
        for coin in coins:
            if coin > i:
                break
            if coin_dict[i - coin] != -1:
                coin_dict[i] = min(coin_dict[i - coin] + 1, coin_dict[i])
    if coin_dict[total] == float('inf'):
        return -1
    return coin_dict[total]  # return total number of coins needed to make change
