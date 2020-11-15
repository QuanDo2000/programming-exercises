"""
ID: 5
Name: Smallest multiple
Description:
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Link: https://projecteuler.net/problem=5
Help:
- https://codereview.stackexchange.com/questions/75092/project-euler-5-lowest-common-multiple-of-1-through-20?noredirect=1&lq=1
"""


import time
import math


# Function smallest_multiple()
#   Find smallest multiple from 1 to number by multiplying the LCM of 1 to number
def smallest_multiple(number):
    """Return smallest multiple from 1 to number by multiplying the LCM of 1 to number."""
    num = 1
    for i in range(1, number + 1):
        # Find the LCM of num and i
        num = (num * i) // (math.gcd(num, i))
    return num


if __name__ == "__main__":
    num_in = int(input("Enter number: "))

    start = time.time_ns()

    print("\nFinding smallest multiple of 1 to {}".format(num_in))
    print("The smallest multiple is: {:}".format(smallest_multiple(num_in)))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
