"""
ID: 14
Name: Longest Collatz sequence
Description:
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
Link: https://projecteuler.net/problem=14
Help: 014_overview.pdf from https://projecteuler.net/problem=14
"""


import time


def len_collatz_gen(num):
    """Return the lengths of the Collatz sequence of num."""
    try:
        return(values[num])
    except:
        if (num % 2 == 0):
            values[num] = 1 + len_collatz_gen(int(num / 2))
        else:
            values[num] = 2 + len_collatz_gen(int((3 * num + 1) / 2))
        return values[num]


def longest_chain(limit):
    """Return longest chain from limit to limit / 2."""
    longest = 0
    ans = -1
    for i in range(limit, int(limit / 2) - 1, -1):
        if len_collatz_gen(i) > longest:
            longest = len_collatz_gen(i)
            ans = i
    return ans


if __name__ == "__main__":
    # Dict storing already calculated lengths
    values = {1: 1}
    limit = int(input("Enter limit: "))

    start = time.time_ns()

    res = longest_chain(limit)
    print("The starting number with the longest chain is: {}".format(res))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
