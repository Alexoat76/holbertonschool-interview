#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """Clasic Bottom-Up dynamic programming"""
    tmp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            tmp_value += total // coin
            total = total % coin

    return tmp_value if total == 0 else -1
