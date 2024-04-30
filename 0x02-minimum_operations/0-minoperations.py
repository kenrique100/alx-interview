#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve
    a given number of H characters.

    Parameters:
    - n (int): The target number of H characters.

    Returns:
    - int: The minimum number of operations.
    If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    i = 2
    count = 0

    while i <= n:
        if n % i == 0:
            count += i
            n /= i
        else:
            i += 1

    return count


if __name__ == '__main__':
    n = 4
    print("Min # of operations to reach {} characters: {}"
          .format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} characters: {}"
          .format(n, minOperations(n)))
