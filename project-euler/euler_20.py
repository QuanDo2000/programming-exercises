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


import time


def factorial(n):
    """Return the equivalent of n! (factorial of number n)."""
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret


def sum_of_digits(num):
    """Return the sum of the digits of the input."""
    return sum(list(map(int, list(str(num)))))


if __name__ == "__main__":
    n = int(input('Enter number: '))

    start = time.time_ns()

    ans = sum_of_digits(factorial(n))
    print('The factorial digit sum of {}! is {}'.format(n, ans))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
