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
        # sort coins in ascending order (smallest to largest)
    coins = sorted(coins)
    # initialize dynamic programming list with inf values
    dynamic = [float('inf')] * (total + 1)
    # set first value to 0 (no coins needed to make 0 change)
    dynamic[0] = 0
    # iterate through each total value from 0 to total
    while dynamic[total] == float('inf'):
        for i in range(total + 1):
            # iterate through each coin value
            for coin in coins:
                # if coin value is less than or equal to total value
                if coin > i:
                    break
                # if coin value is less than or equal to total value
                if dynamic[i - coin] != -1:
                    # set dynamic value to min of current value and
                    #   previous value + 1
                    dynamic[i] = min(dynamic[i], dynamic[i - coin] + 1)
        # if no change can be made, return -1
        if dynamic[total] == float('inf'):
            return -1
    return dynamic[total]
