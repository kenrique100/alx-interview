#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
"""


def minOperations(n):
    if n <= 1:
        return n

    # Initialize an array to store the minimum operations needed for each index
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed to reach 1 character
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:  # Check if i is divisible by j
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0

# Example usage:
n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
