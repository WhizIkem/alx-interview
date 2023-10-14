#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def prime_numbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime_nos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if filtered[prime]:
            prime_nos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return prime_nos


def is_winner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria = ben = 0
    for i in range(x):
        prime_nos = prime_numbers(nums[i])
        if len(prime_nos) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    return None
