#!/usr/bin/python3
"""
Module for solving the minimum coins problem using dynamic programming.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to achieve.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins required for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make a total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be achieved
    return dp[total] if dp[total] != float('inf') else -1
