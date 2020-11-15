"""
ID: 23
Name: Non-abundant sums
Description:
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
Link: https://projecteuler.net/problem=23
"""


import time


def sum_divisors(num):
    """Return a list of all proper divisors for input number."""
    ret_num = 0
    for idx in range(1, (num // 2) + 1):
        if num % idx == 0:
            ret_num += idx
    return ret_num


def find_abundants(limit):
    """Return a list of all abundant numbers below a limit."""
    ret_list = set()
    for num in range(1, limit + 1):
        sum_divs = sum_divisors(num)
        if sum_divs > num:
            ret_list.add(num)
    return ret_list


def check_sum_abundants(abundants, num):
    """Return a boolean whether the input num is a sum of two abundant numbers."""
    if num % 2 == 0 and num > 46:
        return True
    elif num > 20161:
        return True

    return any(num - a in abundants for a in abundants)


if __name__ == "__main__":
    limit = int(input('Input limit number: '))

    start = time.time_ns()

    abundants = find_abundants(limit)

    total = 0
    for num in range(1, limit + 1):
        if not check_sum_abundants(abundants, num):
            total += num
            # print(total)
    print('The sum of all non-abundants is {}'.format(total))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
