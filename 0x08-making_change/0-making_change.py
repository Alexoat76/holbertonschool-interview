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
            coin_dict = {}
            while total is not None:
                for c in coins:
                    if total % c == 0:
                        coin_dict[c] = total / c
                        return(int(sum(coin_dict.values())))
                    else:
                        coin_dict[c] = total // c
                        total -= (c * coin_dict[c])

                return -1
