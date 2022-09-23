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
    if total == 0:
        return 0
    if total < 0 or len(coins) == 0:
        return -1
    if len(coins) == 1 and total in coins:
        return 1

    nums = [float('inf') for x in range(total+1)]
    nums[0] = 0
    for denom in coins:
        for amount in range(len(nums)):
            if denom <= amount:
                nums[amount] = min(nums[amount], 1 + nums[amount - denom])
    return nums[total] if nums[total] != float('inf') else -1
