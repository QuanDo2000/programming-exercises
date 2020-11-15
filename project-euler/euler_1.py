"""
ID: 1
Name: Multiples of 3 and 5
Description:
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
Link: https://projecteuler.net/problem=1
Help:
- https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000
"""


import time
import math


def sum_of_multiples(upper_bound, number):
    """Return the sum of all the multiples of a number below an upper bound (not inclusive)."""
    n = (upper_bound - 1) // number
    return (number * 1 / 2 * n * (n + 1))


def lcm(a, b):
    """Return the lowest common multiple of a and b."""
    return (a * b) // math.gcd(a, b)


def sum_of_all_multiples(upper_bound, num_in):
    """Return the sum of all the multiples of all numbers in a list of numbers."""
    total = 0
    # Sum of all the multiples
    for i in num_in:
        total += sum_of_multiples(upper_bound, i)
    # Minus all the duplicate multiples
    for i in range(len(num_in)):
        for j in range(i + 1, len(num_in)):
            total -= sum_of_multiples(upper_bound, lcm(num_in[i], num_in[j]))
    return total


if __name__ == "__main__":
    upper_bound = int(input("Enter upper bound: "))
    num_in = list(map(int, input('Enter list of numbers: ').split(' ')))

    start = time.time_ns()

    print("\nUpper Bound: {}".format(upper_bound))
    print("Calculating for multiples of: {}".format(num_in))
    res = int(sum_of_all_multiples(upper_bound, num_in))
    print("The sum is: {}".format(res))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
