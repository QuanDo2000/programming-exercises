"""
ID: 16
Name: Power Digit Sum
Description: 
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
Link: https://projecteuler.net/problem=16
"""


import time


def power_digit_sum(base, exp):
    """Return the digit sum of a base raised to a power."""
    return sum([int(i) for i in str(pow(base, exp))])


if __name__ == "__main__":
    base = int(input("Enter base: "))
    exp = int(input("Enter exponent: "))

    start = time.time_ns()

    print("The digit sum is: {}".format(power_digit_sum(base, exp)))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
