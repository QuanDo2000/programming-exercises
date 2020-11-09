"""
ID: 20
Name: Factorial digit sum
Description:
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
Link: https://projecteuler.net/problem=20
"""


def factorial(n):
    """Return the equivalent of n! (factorial of number n)."""
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret
