"""
ID: 3
Name: Largest prime factor
Description:
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
Link: https://projecteuler.net/problem=3
Help:
- https://codereview.stackexchange.com/questions/104381/prime-factorization-for-integers-with-up-to-9-digit-long-prime-factors/104386#104386
- https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm#Python_code_sample
"""


import sys
import math


def get_factor(number):
    """Return the next prime factor using Pollard's rho.
    Can fail!!!
    """
    x_fixed = 2
    x = 3
    cycle_size = 2
    factor = 1
    while factor == 1:
        for _ in range(cycle_size):
            if factor > 1:
                break
            x = (x * x + 1) % number
            factor = math.gcd((x - x_fixed), number)
        cycle_size *= 2
        x_fixed = x
    return factor


def prime_factors(number):
    """Return prime factors of a number by using Pollard's rho."""
    factors = []
    while number > 1:
        next_factor = get_factor(number)
        factors.append(next_factor)
        number //= next_factor
    return factors


# Check for input error
try:
    number = int(input("Enter number: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

# Print the result
print("\nThe number is: {0:,}".format(number))
factors = sorted(prime_factors(number))
print("The factors are {0}".format(factors))
print("The largest prime factor is: {0}".format(factors[-1]))
