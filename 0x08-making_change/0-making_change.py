#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""
import time


def makeChange(coins, total):
    start = time.time()

    if total <= 0:
        return 0

    # Initialize a list to store the fewest coins
    # Initialize with a value higher than the maximum possibel.
    dp = [total + 1] * (total + 1)

    # There are 0 ways to make change for 0
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == total + 1:
        result = -1
    else:
        result = dp[total]

    end = time.time()

    avg = (end - start) / 10
    print("Average runtime for {}: {:.6f}".format(total, avg))

    return result
