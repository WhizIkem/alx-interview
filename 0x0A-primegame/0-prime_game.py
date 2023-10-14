#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""

def isWinner(x, nums):
    """
    Determines the winner of a game based on a set of rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers repesenting 'n' for each round.
    Returns:
        str: The name of the player who won the most rounds
        (either Maria or Ben)
        if the winner cannot be determined, it returns None.
    """


    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def can_win(n):
        if n <= 1:
            return "Ben"
        # If n is even or prime, Maria wins; otherwise, Ben wins.
        if n % 2 == 0 or is_prime(n):
            return "Ben"
        else:
            return "Maria"

    maria_wins = 0
    ben_wins = 0
      
    for n in nums:
        winner = can_win(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
