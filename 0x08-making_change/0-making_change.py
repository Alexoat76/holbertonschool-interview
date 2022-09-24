#!/usr/bin/python3
"""
Defines function that determines the fewest number of coins to make change
"""


from re import I


def makeChange(coins: int, amount: int) -> int:
    """
    Returns the fewest number of coins to make change
    """
    dynamic = [float('inf') for _ in range(amount + 1)]
    dynamic[0] = 0
    for i in range(len(dynamic)):
        for coin in coins:
            if coin > i:
                break
            if i - coin >= 0:
                dynamic[i] = min(dynamic[i - coin] + 1, dynamic[i])
    return -1 if dynamic[amount] == float('inf') else dynamic[amount]
