#!/usr/bin/python3
"""
Prime Game - Determine the winner after playing x rounds of the game.
"""

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_counts(limit):
    """Generate a list of prime counts up to the limit."""
    primes = [0] * (limit + 1)
    prime_count = 0

    for i in range(1, limit + 1):
        if is_prime(i):
            prime_count += 1
        primes[i] = prime_count

    return primes

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None if a tie.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = generate_prime_counts(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
