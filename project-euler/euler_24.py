"""
ID: 24
Name: Lexicographic permutations
Description:
    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
Link: https://projecteuler.net/problem=24
"""


import time


def get_factorial_map(n):
    """Return a dictionary of factorial results from 1 to n"""
    ret_map = {0: 1, 1: 1}
    for i in range(2, n + 1):
        ret_map[i] = ret_map[i - 1] * i
    return ret_map


if __name__ == "__main__":
    idx = int(input('Enter lexicographic index: '))

    start = time.time_ns()

    fact_map = get_factorial_map(10)
    # print(fact_map)

    if idx > fact_map[10]:
        print('Index out of range.')
        exit()

    ans = []
    curr_sum = 0
    for pos in range(10):
        for num in range(10):
            # print(pos, num, curr_sum)
            if num not in ans and fact_map[9 - pos] + curr_sum >= idx:
                ans.append(num)
                break
            elif num not in ans:
                curr_sum += fact_map[9 - pos]
    ans = ''.join([str(num) for num in ans])
    print('The {}th lexicographical permutation is {}'.format(idx, ans))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
