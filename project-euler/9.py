"""
ID: 9
Name: Special Pythagorean triplet
Description:
    A Pythagorean triplet is a set of three natural numbers,
    a < b < c, for which, a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which
    a + b + c = 1000.
    Find the product a*b*c.
Link: https://projecteuler.net/problem=9
Help:
- https://codereview.stackexchange.com/questions/37398/finding-the-pythagorean-triplet-that-sums-to-1000
- https://codereview.stackexchange.com/questions/163599/project-euler-problem-9-special-pythagorean-triplet
- 009_overview.pdf from https://projecteuler.net/problem=9
"""


import sys
import math


def special_pythagorean(s):
    """Return special pythagorean triplet that satisfies a^2 + b^2 = c^2 and a + b + c = number."""
    limit = math.ceil(math.sqrt(s / 2))
    for m in range(2, limit):
        if ((s / 2) % m == 0):
            sm = (s / 2) / m
            while (sm % 2 == 0):
                sm /= 2
            if (m % 2 == 1):
                k = m + 2
            else:
                k = m + 1
            while (k < 2 * m and k <= sm):
                if (sm % k == 0 and math.gcd(k, m) == 1):
                    d = (s / 2) / (k * m)
                    n = k - m
                    a = d * (m**2 - n**2)
                    b = 2 * d * m * n
                    c = d * (m**2 + n**2)
                    return (a, b, c)
                k += 2


# Check Input
try:
    limit = int(input("Enter the sum: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

# Print result
print("\nThe sum is: {}".format(limit))
x = special_pythagorean(limit)
y = x[0] * x[1] * x[2]
print("The triplet is ({:.0f}, {:.0f}, {:.0f})".format(x[0], x[1], x[2]))
print("The product is: {:.0f}".format(y))
