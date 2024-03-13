#!/usr/bin/python3
"""
Prime Game module optimized for Python 3.8 to Python 10.1 with PEP 8 standards.
"""

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))

def count_primes(n: int) -> int:
    """Count prime numbers up to n using Sieve of Eratosthenes."""
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return sum(is_prime)

def isWinner(x: int, nums: list) -> str:
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list[int]): List of integers representing n for each round.

    Returns:
        str: Name of the player that won the most rounds. Returns None if a winner cannot be determined.
    """
    if not nums or x <= 0:
        return None
    
    ben_wins = sum(count_primes(n) % 2 == 0 for n in nums)

    if ben_wins > x // 2:
        return "Ben"
    elif ben_wins < x // 2:
        return "Maria"
    else:
        return None

if __name__ == "__main__":
    print(isWinner(3, [4, 5, 1]))
    print(isWinner(5, [2, 5, 1, 4, 3]))
