#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    # Returns fewest number of coins needed to meet total
    """Clasic Bottom-Up dynamic programming"""
    tmp_value = 0  # temporary value to store the value of the coin being used
    # sort the coins in descending order to make the algorithm more efficient
    coins.sort(reverse=True)

    if total < 0:  # if the total is negative, return -1 (no solution)
        return 0

    for coin in coins:  # iterate through the coins list
        # if the remainder is less than the total amount of change
        if total % coin <= total:
            # add the number of coins to the tmp_value variable
            tmp_value += total // coin
            total = total % coin  # update the total amount of change

    return tmp_value if total == 0 else -1  # return the number of coins used
