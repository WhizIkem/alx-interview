#!/usr/bin/python3

def isWinner(x, nums):
  def isPrime(num):
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
        if n == 1:
            return "Ben"
        elif is_prime(n):
            return "Maria"
        else:
            return "Ben"
      
    winner_counts = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = can_win(n)
        winner_counts[winner] += 1

    if winner_counts["Maria"] > winner_counts["Ben"]:
        return "Maria"
    elif winner_counts["Maria"] < winner_counts["Ben"]:
        return "Ben"
    else:
        return None
