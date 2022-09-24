#!/usr/bin/python3
"""
Defines function that determines the fewest number of coins to make change
"""


def makeChange(coins: int, amount: int) -> int:
    """
    Returns the fewest number of coins to make change
    """
    dynamic = [float('inf') for _ in range(amount + 1)]
    dynamic[0] = 0
    for coin in coins:
        for i in range(len(dynamic)):
            if i-coin >= 0:
                dynamic[i] = min(dynamic[i], dynamic[i-coin] + 1)
    return dynamic[-1] if dynamic[-1] != float('inf') else -1
