"""
ID: 6
Name: Sum square difference
Description:
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
Link: https://projecteuler.net/problem=6
Help:
- https://math.stackexchange.com/questions/1166027/prove-that-1222-cdotsn2-fracnn12n16-for-n-in-mathbbn
- https://codereview.stackexchange.com/questions/58460/sum-of-squares-square-of-sum-difference?rq=1
"""


import time


def sum_of_square(lim):
    """Return the sum of all the square from 0 to lim."""
    total = (lim * (lim + 1) * (2 * lim + 1)) / 6
    return total


def square_of_sum(lim):
    """Return the square of the sum from 0 to lim."""
    total = (lim * (lim + 1)) / 2
    return (total ** 2)


if __name__ == "__main__":
    limit = int(input("Enter limit: "))

    start = time.time_ns()

    print("\nThe limit is: {}".format(limit))
    sum_square = int(sum_of_square(limit))
    square_sum = int(square_of_sum(limit))
    result = int(abs(sum_square - square_sum))
    print("The sum of square is: {}".format(sum_square))
    print("The square of sum is: {}".format(square_sum))
    print("The difference is: {}".format(result))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
