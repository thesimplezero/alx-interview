#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determines fewest number of coins needed to meet given amount total
    Args:
        coins (list): A list of values of coins in your possession
        total (int): The target amount total
    Returns:
        int: Fewest number of coins needed to meet total
    """
    if total < 1:
        return 0
    # Initialize dynamic programming array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    # Iterate over each coin
    for coin in coins:
        # Update dp array for all values >= coin
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    # Return minimum coins needed
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Test case 1
    print(makeChange([1, 2, 25], 37))  # Output: 7
    # Test case 2
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
