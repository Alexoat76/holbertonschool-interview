#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """ Returns fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    else:
        if coins is None or len(coins) == 0:
            return -1
        else:
            coins = sorted(coins, reverse=True)
            count = 0
            for i in coins:
                if total >= i:
                    count += total // i
                    total = total % i
            if total == 0:
                return count
            else:
                return -1
