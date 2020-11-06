"""
ID: 15
Name: Lattice Paths
Description:
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?
Link: https://projecteuler.net/problem=15
Help:
- https://en.wikipedia.org/wiki/Lattice_path
"""

import sys


def factorial(n):
    """Return the equivalent of n! (factorial of number n)."""
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret


def binomial_coefficient(n, k):
    """Return the equivalent of nCk."""
    return factorial(n) / (factorial(k) * factorial(n - k))


def lattic_paths(size):
    """Take in size of grid and return the amount of paths to traverse the grid."""
    return binomial_coefficient(2 * size, size)


# Check number input
try:
    size = int(input("Enter size of grid: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()
# Output
res = lattic_paths(size)
print("Amount of paths is: {:,.0f}".format(res))
