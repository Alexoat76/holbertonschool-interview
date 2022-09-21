#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """ Returns fewest number of coins needed to meet total
    """

    if total <= 0:  # If total is 0 or less, return 0
        return 0
        # If total is greater than 0 and coins is empty, return -1 (impossible)
    else:
        from math import trunc
        """ Import trunc function from math module to round down
            to nearest integer
        """
        # Sort coins in descending order (largest to smallest)
        coins = sorted(coins, reverse=True)
        coin_dict = {}  # Create empty dictionary to store coin values
        while total is not None:  # While total is not None (empty)
            for c in coins:  # For each coin in coins list
                if total % c == 0:  # If total is divisible by coin value
                    coin_dict[c] = total / c  # Add coin value to dictionary
                    return(int(sum(coin_dict.values())))  # Return sum of val.
                else:
                    coin_dict[c] = trunc(total / float(c))  # Add coin value
                    total -= (c * coin_dict[c])  # Subt. coin value from total
            return -1  # If total is not None, return -1
