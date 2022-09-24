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
    for i in range(len(dynamic)):
        for coin in coins:
            if i-coin >= 0:
                dynamic[i] = min(dynamic[i], dynamic[i-coin] + 1)
    return dynamic[amount] if dynamic[amount] != float('inf') else -1
