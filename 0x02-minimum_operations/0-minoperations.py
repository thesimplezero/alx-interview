#!/usr/bin/python3
"""
Module to calculate the fewest number of operations needed to
result in exactly n 'H' characters in a text file. The two
allowed operations are Copy All and Paste.
"""


def min_operations(n):
    """
    Calculate Minimum Operations.
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    divisor = 1
    i = n - 1
    while i > 0:
        if n % i == 0:
            divisor = i if i != 0 else 1
            break
        i -= 1
    result = int((min_operations(divisor) if divisor != 1 else 0) + n / divisor)
    return result
