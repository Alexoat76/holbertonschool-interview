#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """ Returns fewest number of coins needed to meet total
    """
    total = [int(total)]
    if total[0] <= 0:
        return 0
    coins.sort(reverse=True)
    coins = [int(i) for i in coins]
    coins = [i for i in coins if i <= total[0]]
    if not coins:
        return -1
    count = 0
    for i in coins:
        count += total[0] // i
        total[0] = total[0] % i
        if total[0] == 0:
            return count
    return -1
