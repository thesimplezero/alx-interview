#!/usr/bin/python3
"""
Prime Game module optimized for Python 3.8 to Python 10.1 with PEP 8 standards.
"""

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def simulate_game(n: int) -> str:
    """Simulate a game to determine the winner."""
    primes = [is_prime(i) for i in range(n + 1)]
    prime_counts = [0] * (n + 1)
    for i in range(2, n + 1):
        prime_counts[i] = prime_counts[i-1] + (1 if primes[i] else 0)

    # The player who starts the last move wins. If the number of primes
    # up to n is even, Maria wins; otherwise, Ben wins.
    return 'Maria' if prime_counts[n] % 2 == 0 else 'Ben'

def isWinner(x: int, nums: list) -> str:
    """Determine the overall winner of x rounds."""
    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = simulate_game(n)
        wins[winner] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
