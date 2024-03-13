#!/usr/bin/python3
"""
Prime Game module
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str: Name of the player that won the most rounds.
             If the winner cannot be determined, returns None.
    """
    if not nums or x <= 0:
        return None

    # Optimize by pre-calculating primes up to the maximum value in nums
    # This avoids recalculating primes for each n in nums
    max_num = max(nums)
    primes = [False, False] + [True] * (max_num - 1)
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    prime_counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_counts[i] = prime_counts[i-1] + (1 if primes[i] else 0)

    ben_wins = 0
    # Determine the winner for each round
    for n in nums:
        if (prime_counts[n] % 2 == 0):
            ben_wins += 1

    # Determine the overall winner
    if ben_wins > x // 2:
        return "Ben"
    elif ben_wins < x // 2:
        return "Maria"
    else:
        return None

if __name__ == "__main__":
    print(isWinner(3, [4, 5, 1]))
    print(isWinner(5, [2, 5, 1, 4, 3]))
