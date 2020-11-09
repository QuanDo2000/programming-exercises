"""
CodeChef Problem: HMAPPY2
https://www.codechef.com/problems/HMAPPY2
"""

import math  # gcd()

# Loop test cases
for _ in range(int(input())):
    # Input
    # n for number of problems
    # Appy can solve problem % a == 0 but not % b == 0
    # Chef can solve problem % b == 0 but not % a == 0
    # k for number of problems needed to win
    n, a, b, k = map(int, input().split())
    # Amount of questions solved
    # Calculate lcm(a, b)
    lcm = a * b / math.gcd(a, b)

    # Get amount of problems divisible by a and
    # minus the amount divisible by both a and b
    # to get amount divisible by a but not b.

    # Appy can solve n / a - n / lcm(a, b)
    # Chef can solve n / b - n / lcm(a, b)
    count = (n // a) + (n // b) - (2 * (n // lcm))
    # Check if number problems solved is higher than needed to win
    if (count >= k):
        print("Win")
    else:
        print("Lose")
